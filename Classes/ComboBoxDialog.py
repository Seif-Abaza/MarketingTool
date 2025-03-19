from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QComboBox, QPushButton

class ComboBoxDialog(QDialog):
    def __init__(self,parent,Items):
        super().__init__(parent)

        self.setWindowTitle("Select an Item")
        self.setFixedSize(300, 150)

        # Layout
        layout = QVBoxLayout(self)

        # ComboBox with items
        self.combo_box = QComboBox()
        self.combo_box.addItems(Items)
        layout.addWidget(self.combo_box)

        # OK Button
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)  # Close dialog when clicked
        layout.addWidget(self.ok_button)

    def get_selected_text(self):
        """Return selected text from combo box"""
        return self.combo_box.currentText()
    
    