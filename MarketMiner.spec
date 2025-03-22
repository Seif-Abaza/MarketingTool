# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
import PySide6
import os

datas = [
    ('run_debug.sh', '.'),
    ('requirements.txt', '.'),
    ('Resource/countries.json', '.'),
    ('images/MM_Logo.ico', 'images')
]

binaries = [
    ('locat/*.qm', 'locat'),
    ('/usr/lib/x86_64-linux-gnu/libxkbcommon.so.0', '.'),
    ('/usr/lib/x86_64-linux-gnu/libEGL.so.1', '.'),
]
hiddenimports = [
    'beautifulsoup4', 'cryptography', 'Flask', 'flask_limiter', 'googletrans',
    'langcodes', 'langdetect', 'py-cpuinfo', 'openpyxl',
    'phonenumbers', 'pillow','python-magic', 'playwright', 'psutil', 'pymongo', 'pyperclip',
    'pyqrcode', 'PySide6', 'python_magic', 'pytz', 'qrcode', 'requests',
    'smsactivate', 'telethon',
    'torch', 'transformers', 'urllib3', 'numpy'
]

tmp_ret = collect_all('PySide6'); datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('PyNaCl'); datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('playwright'); datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('openpyxl'); datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('numpy'); datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter', 'unittest', 'numpy.testing'],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MarketMiner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch=None,
    icon=['images/MM_Logo.ico'],
    hide_console='hide-early',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MarketMiner'
)