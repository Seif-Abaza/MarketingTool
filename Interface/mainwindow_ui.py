# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        MainWindow.resize(1044, 857)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ContactNew))
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowNestedDocks|QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionExplor = QAction(MainWindow)
        self.actionExplor.setObjectName(u"actionExplor")
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionCreator = QAction(MainWindow)
        self.actionCreator.setObjectName(u"actionCreator")
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.action_Settings = QAction(MainWindow)
        self.action_Settings.setObjectName(u"action_Settings")
        self.actionAllow_Access = QAction(MainWindow)
        self.actionAllow_Access.setObjectName(u"actionAllow_Access")
        self.actionNetwork_Settings = QAction(MainWindow)
        self.actionNetwork_Settings.setObjectName(u"actionNetwork_Settings")
        self.actionGet_Mobile_Number = QAction(MainWindow)
        self.actionGet_Mobile_Number.setObjectName(u"actionGet_Mobile_Number")
        self.actionCheck_Update = QAction(MainWindow)
        self.actionCheck_Update.setObjectName(u"actionCheck_Update")
        self.actionSearch_By_Phone_Number = QAction(MainWindow)
        self.actionSearch_By_Phone_Number.setObjectName(u"actionSearch_By_Phone_Number")
        self.actionSearch_By_Email = QAction(MainWindow)
        self.actionSearch_By_Email.setObjectName(u"actionSearch_By_Email")
        self.actionSearch_By_Account = QAction(MainWindow)
        self.actionSearch_By_Account.setObjectName(u"actionSearch_By_Account")
        self.actionGet_Temp_Mail = QAction(MainWindow)
        self.actionGet_Temp_Mail.setObjectName(u"actionGet_Temp_Mail")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(9, 9, 1031, 800))
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QFrame.Shape.NoFrame)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.groupBox = QGroupBox(self.splitter)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setSizeIncrement(QSize(0, 50))
        self.pushButton.setBaseSize(QSize(0, 50))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setSizeIncrement(QSize(0, 50))
        self.pushButton_2.setBaseSize(QSize(0, 50))
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(0, 50))
        self.pushButton_3.setSizeIncrement(QSize(0, 50))
        self.pushButton_3.setBaseSize(QSize(0, 50))
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QSize(0, 50))

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(0, 50))
        self.pushButton_4.setSizeIncrement(QSize(0, 50))
        self.pushButton_4.setBaseSize(QSize(0, 50))
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setAutoDefault(True)
        self.pushButton_4.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(0, 50))
        self.pushButton_5.setSizeIncrement(QSize(0, 50))
        self.pushButton_5.setBaseSize(QSize(0, 50))
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setAutoDefault(True)
        self.pushButton_5.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        self.pushButton_6.setSizeIncrement(QSize(0, 50))
        self.pushButton_6.setBaseSize(QSize(0, 50))
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setAutoDefault(True)
        self.pushButton_6.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QSize(0, 50))
        self.pushButton_7.setSizeIncrement(QSize(0, 50))
        self.pushButton_7.setBaseSize(QSize(0, 50))
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setAutoDefault(True)
        self.pushButton_7.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(False)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QSize(0, 50))
        self.pushButton_9.setSizeIncrement(QSize(0, 50))
        self.pushButton_9.setBaseSize(QSize(0, 50))
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setAutoDefault(True)
        self.pushButton_9.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_9)

        self.lblStatus = QLabel(self.groupBox)
        self.lblStatus.setObjectName(u"lblStatus")
        sizePolicy.setHeightForWidth(self.lblStatus.sizePolicy().hasHeightForWidth())
        self.lblStatus.setSizePolicy(sizePolicy)
        self.lblStatus.setMinimumSize(QSize(0, 100))
        self.lblStatus.setSizeIncrement(QSize(0, 100))
        self.lblStatus.setBaseSize(QSize(0, 100))
        self.lblStatus.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.lblStatus.setScaledContents(True)
        self.lblStatus.setWordWrap(True)
        self.lblStatus.setMargin(0)

        self.verticalLayout.addWidget(self.lblStatus)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label_3.setFrameShape(QFrame.Shape.NoFrame)
        self.label_3.setFrameShadow(QFrame.Shadow.Plain)
        self.label_3.setLineWidth(0)

        self.verticalLayout.addWidget(self.label_3)

        self.lblmsg = QLabel(self.groupBox)
        self.lblmsg.setObjectName(u"lblmsg")
        sizePolicy.setHeightForWidth(self.lblmsg.sizePolicy().hasHeightForWidth())
        self.lblmsg.setSizePolicy(sizePolicy)
        self.lblmsg.setMinimumSize(QSize(0, 50))
        self.lblmsg.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setFamilies([u"DejaVu Serif Condensed"])
        font.setPointSize(20)
        font.setBold(True)
        self.lblmsg.setFont(font)
        self.lblmsg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblmsg)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.label.setFrameShape(QFrame.Shape.NoFrame)
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setLineWidth(0)

        self.verticalLayout.addWidget(self.label)

        self.lblusers = QLabel(self.groupBox)
        self.lblusers.setObjectName(u"lblusers")
        sizePolicy.setHeightForWidth(self.lblusers.sizePolicy().hasHeightForWidth())
        self.lblusers.setSizePolicy(sizePolicy)
        self.lblusers.setMinimumSize(QSize(0, 50))
        self.lblusers.setMaximumSize(QSize(16777215, 60))
        font1 = QFont()
        font1.setFamilies([u"DejaVu Serif Condensed"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.lblusers.setFont(font1)
        self.lblusers.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lblusers)

        self.splitter.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView = QListView(self.groupBox_2)
        self.listView.setObjectName(u"listView")
        self.listView.setAutoScrollMargin(5)
        self.listView.setTabKeyNavigation(True)
        self.listView.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.listView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.verticalLayout_2.addWidget(self.listView)

        self.btnClear = QPushButton(self.groupBox_2)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayout_2.addWidget(self.btnClear)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.line_2 = QFrame(self.groupBox_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.splitter.addWidget(self.groupBox_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1044, 23))
        self.menuDatabase = QMenu(self.menubar)
        self.menuDatabase.setObjectName(u"menuDatabase")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuNetwork = QMenu(self.menubar)
        self.menuNetwork.setObjectName(u"menuNetwork")
        self.menuPhone_Number = QMenu(self.menubar)
        self.menuPhone_Number.setObjectName(u"menuPhone_Number")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy1.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy1)
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.pushButton_7)

        self.menubar.addAction(self.menuNetwork.menuAction())
        self.menubar.addAction(self.menuDatabase.menuAction())
        self.menubar.addAction(self.menuPhone_Number.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuDatabase.addAction(self.actionExplor)
        self.menuDatabase.addAction(self.actionSearch)
        self.menuDatabase.addAction(self.actionSearch_By_Phone_Number)
        self.menuDatabase.addAction(self.actionSearch_By_Email)
        self.menuDatabase.addAction(self.actionSearch_By_Account)
        self.menuAbout.addAction(self.actionCreator)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.action_Settings)
        self.menuAbout.addAction(self.actionCheck_Update)
        self.menuNetwork.addAction(self.actionAllow_Access)
        self.menuNetwork.addAction(self.actionNetwork_Settings)
        self.menuPhone_Number.addAction(self.actionGet_Mobile_Number)
        self.menuPhone_Number.addAction(self.actionGet_Temp_Mail)

        self.retranslateUi(MainWindow)

        self.pushButton_3.setDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_5.setDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_9.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MarketMiner", None))
        self.actionExplor.setText(QCoreApplication.translate("MainWindow", u"Explor", None))
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.actionCreator.setText(QCoreApplication.translate("MainWindow", u"Support", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.action_Settings.setText(QCoreApplication.translate("MainWindow", u"&Settings", None))
        self.actionAllow_Access.setText(QCoreApplication.translate("MainWindow", u"Allow Access", None))
        self.actionNetwork_Settings.setText(QCoreApplication.translate("MainWindow", u"Network Settings", None))
        self.actionGet_Mobile_Number.setText(QCoreApplication.translate("MainWindow", u"Get Mobile Number", None))
        self.actionCheck_Update.setText(QCoreApplication.translate("MainWindow", u"Check Update", None))
        self.actionSearch_By_Phone_Number.setText(QCoreApplication.translate("MainWindow", u"Search By Phone Number", None))
        self.actionSearch_By_Email.setText(QCoreApplication.translate("MainWindow", u"Search By Email", None))
        self.actionSearch_By_Account.setText(QCoreApplication.translate("MainWindow", u"Search By Account", None))
        self.actionGet_Temp_Mail.setText(QCoreApplication.translate("MainWindow", u"Get Temp Mail", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Media", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Telegram", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Facebook", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Tiktok", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Instegram", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"VK", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Odnoklassniki", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Twitter (X)", None))
        self.lblStatus.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Number of Messages today", None))
        self.lblmsg.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Number of users", None))
        self.lblusers.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://usdtfreelancer.com/\"><span style=\" text-decoration: underline; color:#12a75d;\">Sponsor: USDTFreelancer.com</span></a></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.facebook.com/people/MarketMiner/61574189555294/\"><span style=\" text-decoration: underline; color:#12a75d;\">Follow us</span></a></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://wa.link/hawg4s\"><span style=\" text-decoration: underline; color:#12a75d;\">Technical Support</span></a></p></body></html>", None))
        self.menuDatabase.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuNetwork.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.menuPhone_Number.setTitle(QCoreApplication.translate("MainWindow", u"Phone Number", None))
    # retranslateUi

