import multiprocessing
import threading
import os
import psutil
import torch  # لاستخدام GPU إذا كان متاحًا


class SuperFast:
    def __init__(self,
                 num_cpus: int=os.cpu_count(),  # عدد الأنوية المتاحة
                 run_on_cpu: bool=True,  # اختيار التشغيل على CPU أو GPU
                 num_threads_per_task: int=1,  # عدد الـ Threads لكل وظيفة
                 callback_funcs=None,  # قائمة بالوظائف المراد تشغيلها
                 callback_args=None):  # قائمة بالمعاملات لكل وظيفة
        self.num_cpus = min(num_cpus, psutil.cpu_count(logical=False))  # عدد الأنوية الحقيقية
        self.run_on_cpu = run_on_cpu
        self.num_threads_per_task = num_threads_per_task
        self.callback_funcs = callback_funcs if isinstance(callback_funcs, list) else [callback_funcs]
        self.callback_args = callback_args if isinstance(callback_args, list) else [callback_args] * len(self.callback_funcs)
        self.processes = []
        self.threads = []

    def run(self):
        if self.run_on_cpu:
            # print(f"Running on CPU with {self.num_cpus} processes.")
            self._run_on_cpu()
        else:
            # print("Running on GPU")
            self._run_on_gpu()

    def _run_on_cpu(self):
        for i, func in enumerate(self.callback_funcs):
            process = multiprocessing.Process(target=self._run_threads, args=(func, self.callback_args[i], i))
            self.processes.append(process)
            process.start()

        for process in self.processes:
            process.join()

        # print("All CPU processes are done.")

    def _run_threads(self, func, args, process_id):
        threads = []
        for i in range(self.num_threads_per_task):
            thread = threading.Thread(target=func, args=(args,))
            threads.append(thread)
            thread.start()
            # print(f"Process {process_id} - Thread {i} is running")

        for thread in threads:
            thread.join()

        # print(f"All threads in process {process_id} are done.")

    def _run_on_gpu(self):
        if not torch.cuda.is_available():
            # print("CUDA is not available. Falling back to CPU.")
            self.run_on_cpu = True
            self.run()
            return

        device = torch.device("cuda")
        # print(f"Running on GPU: {torch.cuda.get_device_name(0)}")

        for func, args in zip(self.callback_funcs, self.callback_args):
            func(args, device)

        # print("All GPU tasks are done.")
