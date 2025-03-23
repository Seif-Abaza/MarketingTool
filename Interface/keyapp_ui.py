# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyapp.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(689, 684)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setBaseSize(QSize(524, 205))
        Dialog.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        Dialog.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogPassword))
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 10, 291, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(31)
        self.label_5.setFont(font)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 60, 111, 18))
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(100, 80, 521, 101))
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(15)
        self.label_16.setFont(font2)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 490, 651, 116))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_3.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.txtAppID = QLineEdit(self.layoutWidget)
        self.txtAppID.setObjectName(u"txtAppID")
        sizePolicy1.setHeightForWidth(self.txtAppID.sizePolicy().hasHeightForWidth())
        self.txtAppID.setSizePolicy(sizePolicy1)
        self.txtAppID.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.txtAppID)

        self.txtMail = QLineEdit(self.layoutWidget)
        self.txtMail.setObjectName(u"txtMail")
        sizePolicy1.setHeightForWidth(self.txtMail.sizePolicy().hasHeightForWidth())
        self.txtMail.setSizePolicy(sizePolicy1)
        self.txtMail.setClearButtonEnabled(True)

        self.horizontalLayout_3.addWidget(self.txtMail)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_20)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.txtKey = QLineEdit(self.layoutWidget)
        self.txtKey.setObjectName(u"txtKey")
        sizePolicy1.setHeightForWidth(self.txtKey.sizePolicy().hasHeightForWidth())
        self.txtKey.setSizePolicy(sizePolicy1)
        self.txtKey.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.txtKey)

        self.txtTxid = QLineEdit(self.layoutWidget)
        self.txtTxid.setObjectName(u"txtTxid")
        sizePolicy1.setHeightForWidth(self.txtTxid.sizePolicy().hasHeightForWidth())
        self.txtTxid.setSizePolicy(sizePolicy1)
        self.txtTxid.setClearButtonEnabled(True)

        self.horizontalLayout_4.addWidget(self.txtTxid)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 408, 651, 61))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_4.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(102, 16777215))

        self.horizontalLayout_8.addWidget(self.label_15)

        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_8.addWidget(self.label_11)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.lineEdit = QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.lineEdit.setFont(font3)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.lineEdit)

        self.layoutWidget2 = QWidget(Dialog)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 610, 651, 54))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_5.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.label_21 = QLabel(self.layoutWidget2)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setOpenExternalLinks(True)
        self.label_21.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_7.addWidget(self.label_21)

        self.line = QFrame(self.layoutWidget2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.label_22 = QLabel(self.layoutWidget2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setOpenExternalLinks(True)
        self.label_22.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_7.addWidget(self.label_22)

        self.line_2 = QFrame(self.layoutWidget2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_2)

        self.label_24 = QLabel(self.layoutWidget2)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_24.setOpenExternalLinks(True)
        self.label_24.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_7.addWidget(self.label_24)

        self.line_3 = QFrame(self.layoutWidget2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line_3)

        self.label_23 = QLabel(self.layoutWidget2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setOpenExternalLinks(True)
        self.label_23.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_7.addWidget(self.label_23)

        self.buttonBox = QDialogButtonBox(self.layoutWidget2)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.horizontalLayout_7.addWidget(self.buttonBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.verticalLayout_5.addWidget(self.label_4)

        self.layoutWidget3 = QWidget(Dialog)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 180, 651, 219))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.verticalLayout_6.setContentsMargins(4, 0, 4, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.label_7 = QLabel(self.layoutWidget3)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setTextFormat(Qt.TextFormat.PlainText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget3)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setTextFormat(Qt.TextFormat.PlainText)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget3)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setTextFormat(Qt.TextFormat.PlainText)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy3.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy3)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label_10)

        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.layoutWidget3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label_14)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.label_12.setFont(font4)

        self.verticalLayout_6.addWidget(self.label_12)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.label_17 = QLabel(self.layoutWidget3)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.label_17)

        self.label_18 = QLabel(self.layoutWidget3)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignJustify)

        self.verticalLayout_2.addWidget(self.label_18)

        self.label_19 = QLabel(self.layoutWidget3)
        self.label_19.setObjectName(u"label_19")
        sizePolicy3.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy3)
        self.label_19.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_19)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Key", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"MarketMiner", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Version 2.0.1", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>The best software for marketing and advertising services.</p><p>Custom modifications are available. </p><p align=\"center\"><span style=\" font-weight:700;\">just contact us</span>.</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Your Name", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Mail", None))
        self.txtAppID.setPlaceholderText(QCoreApplication.translate("Dialog", u"account name", None))
        self.txtMail.setPlaceholderText(QCoreApplication.translate("Dialog", u"mail@mail.com", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Phone", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Txid", None))
        self.txtKey.setPlaceholderText(QCoreApplication.translate("Dialog", u"+000...", None))
        self.txtTxid.setPlaceholderText(QCoreApplication.translate("Dialog", u"0x47a7...d93dd7", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"USDT Address", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Binance : <span style=\" font-weight:700; color:#ed333b;\">Only BUSD-T (BNB Smart Chain (BEP20))</span></p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"0x47a7b312093304d536b376b9b8057317a7d93dd7", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://www.binance.com/en/square/post/15833955645849\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">How you can buy USDT</span></a></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://www.facebook.com/people/MarketMiner/61574189555294/\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">Follow us</span></a></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://t.me/marketminer25\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">Telegram</span></a></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/g6uu40\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">Technical Support</span></a></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://usdtfreelancer.com\"><span style=\" font-weight:700; text-decoration: underline; color:#1a5fb4;\">Support By USDTFreelancer.com</span></a></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"For English-speaking", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0644\u0645\u062a\u062d\u062f\u064a\u062b\u064a\u0646 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u0440\u0443\u0441\u0441\u043a\u043e\u044f\u0437\u044b\u0447\u043d\u044b\u0445", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/7p817s\"><span style=\" text-decoration: underline; color:#12a75d;\">Support</span></a></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/4y01cz\"><span style=\" text-decoration: underline; color:#12a75d;\">\u0627\u0644\u062f\u0639\u0645 \u0627\u0644\u0641\u0646\u064a</span></a></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/aij342\"><span style=\" text-decoration: underline; color:#12a75d;\">\u0442\u0435\u0445\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430</span></a></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" color:#e01b24;\">Only 300 USDT for End-User Full Version</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>Paste the Transaction Hash (Txid), your account will be activated within 12 hours.</p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"<html><head/><body dir=\"rtl\"><p align=\"center\">\u0642\u0645 \u0628\u0644\u0635\u0642 \u0627\u0644 (Txid) Transaction Hash , \u0641\u064a \u062e\u0644\u0627\u0644 12 \u0633\u0627\u0639\u0629 \u0633\u064a\u062a\u0645 \u062a\u0641\u0639\u064a\u0644 \u062d\u0633\u0627\u0628\u0643 </p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u0412\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0445\u044d\u0448 \u0442\u0440\u0430\u043d\u0437\u0430\u043a\u0446\u0438\u0438 (Txid), \u0432\u0430\u0448\u0430 \u0443\u0447\u0435\u0442\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c \u0431\u0443\u0434\u0435\u0442 \u0430\u043a\u0442\u0438\u0432\u0438\u0440\u043e\u0432\u0430\u043d\u0430 \u0432 \u0442\u0435\u0447\u0435\u043d\u0438\u0435 12 \u0447\u0430\u0441\u043e\u0432.</p></body></html>", None))
    # retranslateUi

