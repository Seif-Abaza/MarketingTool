from PySide6.QtCore import (
    QLocale,
    QSettings,
    QStringListModel,
    Qt,
    QThread,
    QTranslator,
    Signal,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QFileDialog,
    QLineEdit,
    QListView,
    QMainWindow,
    QMessageBox,
    QProgressDialog,
    QWidget,
)

from Interface.about_ui import Ui_Dialog as AboutDialog


class about(AboutDialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("About MarketingTools")
        self.buttonBox.accepted.connect(self.accept())
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint & ~Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        
        self.label_10.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_10.setOpenExternalLinks(True)
        
        self.label_13.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_13.setOpenExternalLinks(True)
        
        self.label_14.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label_14.setOpenExternalLinks(True)
        
        self.label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.label.setOpenExternalLinks(True)
        self.show()
