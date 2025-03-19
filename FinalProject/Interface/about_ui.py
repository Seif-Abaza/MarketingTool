# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
    QFrame, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(668, 338)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(570, 10, 81, 31))
        self.buttonBox.setOrientation(Qt.Orientation.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 291, 51))
        font = QFont()
        font.setPointSize(31)
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 70, 111, 18))
        font1 = QFont()
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 100, 521, 101))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_4.setFont(font2)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 200, 641, 76))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setTextFormat(Qt.TextFormat.PlainText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setTextFormat(Qt.TextFormat.PlainText)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setTextFormat(Qt.TextFormat.PlainText)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label_10)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label_13)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label_14)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 280, 469, 46))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setOpenExternalLinks(True)
        self.label_21.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_3.addWidget(self.label_21)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setOpenExternalLinks(True)
        self.label_22.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_3.addWidget(self.label_22)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setOpenExternalLinks(True)
        self.label_23.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_3.addWidget(self.label_23)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"About", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"MarketMiner", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Version 1.0.0", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>The best software for marketing and advertising services.</p><p>Custom modifications are available. </p><p align=\"center\"><span style=\" font-weight:700;\">just contact us</span>.</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"For English-speaking", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0644\u0645\u062a\u062d\u062f\u064a\u062b\u064a\u0646 \u0627\u0644\u0644\u063a\u0629 \u0627\u0644\u0639\u0631\u0628\u064a\u0629", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u0440\u0443\u0441\u0441\u043a\u043e\u044f\u0437\u044b\u0447\u043d\u044b\u0445", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/7p817s\"><span style=\" text-decoration: underline; color:#12a75d;\">Support</span></a></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/4y01cz\"><span style=\" text-decoration: underline; color:#12a75d;\">\u0627\u0644\u062f\u0639\u0645 \u0627\u0644\u0641\u0646\u064a</span></a></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/aij342\"><span style=\" text-decoration: underline; color:#12a75d;\">\u0442\u0435\u0445\u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430</span></a></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://www.binance.com/en/square/post/15833955645849\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">How you can buy USDT</span></a></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://www.facebook.com/people/MarketMiner/61574189555294/\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">Follow us</span></a></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://t.me/marketminer25\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">Telegram</span></a></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://wa.link/g6uu40\"><span style=\" font-weight:700; text-decoration: underline; color:#99c1f1;\">Technical Support</span></a></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://usdtfreelancer.com\"><span style=\" font-weight:700; text-decoration: underline; color:#1a5fb4;\">Support By USDTFreelancer.com</span></a></p></body></html>", None))
    # retranslateUi

