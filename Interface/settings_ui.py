# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(449, 382)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 431, 341))
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.tabWTFram = QTabWidget(self.frame)
        self.tabWTFram.setObjectName(u"tabWTFram")
        self.tabWTFram.setEnabled(True)
        self.tabWTFram.setGeometry(QRect(0, 170, 421, 151))
        self.tabWTFram.setTabletTracking(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 401, 98))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.txtTG_ID = QLineEdit(self.layoutWidget)
        self.txtTG_ID.setObjectName(u"txtTG_ID")

        self.horizontalLayout_6.addWidget(self.txtTG_ID)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.txtTG_Hash = QLineEdit(self.layoutWidget)
        self.txtTG_Hash.setObjectName(u"txtTG_Hash")

        self.horizontalLayout_7.addWidget(self.txtTG_Hash)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_8.addWidget(self.label_6)

        self.txtTG_Phone = QLineEdit(self.layoutWidget)
        self.txtTG_Phone.setObjectName(u"txtTG_Phone")

        self.horizontalLayout_8.addWidget(self.txtTG_Phone)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tabWTFram.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.layoutWidget1 = QWidget(self.tab_2)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 391, 81))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)

        self.txtFB_User = QLineEdit(self.layoutWidget1)
        self.txtFB_User.setObjectName(u"txtFB_User")

        self.horizontalLayout_4.addWidget(self.txtFB_User)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.txtFB_Pass = QLineEdit(self.layoutWidget1)
        self.txtFB_Pass.setObjectName(u"txtFB_Pass")

        self.horizontalLayout_5.addWidget(self.txtFB_Pass)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.tabWTFram.addTab(self.tab_2, "")
        self.layoutWidget2 = QWidget(self.frame)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 401, 141))
        self.verticalLayout = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.txtOutput = QLineEdit(self.layoutWidget2)
        self.txtOutput.setObjectName(u"txtOutput")

        self.horizontalLayout.addWidget(self.txtOutput)

        self.btnOutput = QToolButton(self.layoutWidget2)
        self.btnOutput.setObjectName(u"btnOutput")

        self.horizontalLayout.addWidget(self.btnOutput)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.comLang = QComboBox(self.layoutWidget2)
        self.comLang.setObjectName(u"comLang")

        self.horizontalLayout_3.addWidget(self.comLang)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(5, 340, 431, 27))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        QWidget.setTabOrder(self.txtOutput, self.btnOutput)
        QWidget.setTabOrder(self.btnOutput, self.tabWTFram)
        QWidget.setTabOrder(self.tabWTFram, self.txtTG_Hash)
        QWidget.setTabOrder(self.txtTG_Hash, self.txtTG_Phone)
        QWidget.setTabOrder(self.txtTG_Phone, self.txtFB_User)
        QWidget.setTabOrder(self.txtFB_User, self.txtFB_Pass)
        QWidget.setTabOrder(self.txtFB_Pass, self.txtTG_ID)

        self.retranslateUi(Dialog)

        self.tabWTFram.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"App ID", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Hash", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Phone", None))
        self.tabWTFram.setTabText(self.tabWTFram.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Telegram", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.tabWTFram.setTabText(self.tabWTFram.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Facebook", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Default Output", None))
        self.btnOutput.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Language", None))
    # retranslateUi

