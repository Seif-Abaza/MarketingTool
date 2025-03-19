import os
import sys

from PySide6.QtCore import (
    QLocale,
    QSettings,
    QStringListModel,
    Qt,
    QThread,
    QTranslator,
    Signal,
)
from PySide6.QtWidgets import QDialog

from Interface.generate_mail_ui import Ui_Dialog as MailGeneratorDialog

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class MailGenerator(MailGeneratorDialog, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        pass
