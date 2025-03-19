# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tab_media.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCalendarWidget, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QTabWidget,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1066, 748)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(1066, 748))
        Dialog.setMaximumSize(QSize(1066, 748))
        self.tabTelegram = QTabWidget(Dialog)
        self.tabTelegram.setObjectName(u"tabTelegram")
        self.tabTelegram.setEnabled(True)
        self.tabTelegram.setGeometry(QRect(0, 0, 1061, 701))
        self.tabTelegram.setMaximumSize(QSize(16777215, 16777215))
        self.tabTelegram.setAutoFillBackground(False)
        self.tabTelegram.setTabPosition(QTabWidget.TabPosition.North)
        self.tabTelegram.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabTelegram.setElideMode(Qt.TextElideMode.ElideLeft)
        self.tabTelegram.setDocumentMode(False)
        self.tabTelegram.setTabsClosable(False)
        self.tabTelegram.setMovable(False)
        self.tabTelegram.setTabBarAutoHide(True)
        self.tab_tg_1 = QWidget()
        self.tab_tg_1.setObjectName(u"tab_tg_1")
        self.groupBox_12 = QGroupBox(self.tab_tg_1)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 440, 1041, 80))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy1)
        self.frmFileList1 = QFrame(self.groupBox_12)
        self.frmFileList1.setObjectName(u"frmFileList1")
        self.frmFileList1.setGeometry(QRect(410, 30, 621, 51))
        sizePolicy1.setHeightForWidth(self.frmFileList1.sizePolicy().hasHeightForWidth())
        self.frmFileList1.setSizePolicy(sizePolicy1)
        self.frmFileList1.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutWidget = QWidget(self.frmFileList1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 601, 28))
        self.horizontalLayout_26 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 0))
        self.lineEdit_3.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_26.addWidget(self.lineEdit_3)

        self.toolButton_3 = QToolButton(self.layoutWidget)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_26.addWidget(self.toolButton_3)

        self.layoutWidget1 = QWidget(self.groupBox_12)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 40, 231, 26))
        self.horizontalLayout_27 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.radDatabase1 = QRadioButton(self.layoutWidget1)
        self.radDatabase1.setObjectName(u"radDatabase1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radDatabase1.sizePolicy().hasHeightForWidth())
        self.radDatabase1.setSizePolicy(sizePolicy2)
        self.radDatabase1.setChecked(True)

        self.horizontalLayout_27.addWidget(self.radDatabase1)

        self.radFileList1 = QRadioButton(self.layoutWidget1)
        self.radFileList1.setObjectName(u"radFileList1")
        sizePolicy2.setHeightForWidth(self.radFileList1.sizePolicy().hasHeightForWidth())
        self.radFileList1.setSizePolicy(sizePolicy2)
        self.radFileList1.setChecked(False)

        self.horizontalLayout_27.addWidget(self.radFileList1)

        self.groupBox_13 = QGroupBox(self.tab_tg_1)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(10, 100, 1041, 271))
        sizePolicy1.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy1)
        self.layoutWidget2 = QWidget(self.groupBox_13)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 30, 1021, 181))
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_28.addWidget(self.label)

        self.textEdit = QTextEdit(self.layoutWidget2)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_28.addWidget(self.textEdit)


        self.verticalLayout_18.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_29.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_29.addWidget(self.label_3)


        self.verticalLayout_18.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lineEdit = QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_30.addWidget(self.lineEdit)

        self.toolButton = QToolButton(self.layoutWidget2)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_30.addWidget(self.toolButton)

        self.lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_30.addWidget(self.lineEdit_2)

        self.toolButton_2 = QToolButton(self.layoutWidget2)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_30.addWidget(self.toolButton_2)


        self.verticalLayout_18.addLayout(self.horizontalLayout_30)

        self.layoutWidget_7 = QWidget(self.groupBox_13)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(10, 210, 1021, 43))
        self.horizontalLayout_39 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_39.setSpacing(6)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 6, 0, 0)
        self.label_20 = QLabel(self.layoutWidget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_39.addWidget(self.label_20)

        self.lineEdit_17 = QLineEdit(self.layoutWidget_7)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.horizontalLayout_39.addWidget(self.lineEdit_17)

        self.comboBox_11 = QComboBox(self.layoutWidget_7)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setMinimumSize(QSize(197, 0))

        self.horizontalLayout_39.addWidget(self.comboBox_11)

        self.layoutWidget3 = QWidget(self.tab_tg_1)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 380, 1041, 61))
        self.verticalLayout_19 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_19.addWidget(self.label_4)

        self.comboBox = QComboBox(self.layoutWidget3)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setEditable(True)

        self.verticalLayout_19.addWidget(self.comboBox)

        self.layoutWidget4 = QWidget(self.tab_tg_1)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 0, 1041, 95))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.groupBox_14 = QGroupBox(self.layoutWidget4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.layoutWidget_4 = QWidget(self.groupBox_14)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(370, 10, 289, 26))
        self.horizontalLayout_31 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.useTGAI = QRadioButton(self.layoutWidget_4)
        self.useTGAI.setObjectName(u"useTGAI")

        self.horizontalLayout_31.addWidget(self.useTGAI)

        self.useTGCompan = QRadioButton(self.layoutWidget_4)
        self.useTGCompan.setObjectName(u"useTGCompan")

        self.horizontalLayout_31.addWidget(self.useTGCompan)

        self.useFP_Nothing_4 = QRadioButton(self.layoutWidget_4)
        self.useFP_Nothing_4.setObjectName(u"useFP_Nothing_4")
        self.useFP_Nothing_4.setChecked(True)

        self.horizontalLayout_31.addWidget(self.useFP_Nothing_4)


        self.verticalLayout_20.addWidget(self.groupBox_14)

        self.gSlogin_4 = QGroupBox(self.layoutWidget4)
        self.gSlogin_4.setObjectName(u"gSlogin_4")
        self.gSlogin_4.setMinimumSize(QSize(1038, 48))
        self.gSlogin_4.setMaximumSize(QSize(1038, 48))
        self.gSlogin_4.setFlat(True)
        self.layoutWidget_5 = QWidget(self.gSlogin_4)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(11, 10, 1021, 28))
        self.horizontalLayout_32 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.layoutWidget_5)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(106, 0))
        self.label_36.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout_32.addWidget(self.label_36)

        self.txtCompName1_2 = QComboBox(self.layoutWidget_5)
        self.txtCompName1_2.setObjectName(u"txtCompName1_2")
        sizePolicy2.setHeightForWidth(self.txtCompName1_2.sizePolicy().hasHeightForWidth())
        self.txtCompName1_2.setSizePolicy(sizePolicy2)
        self.txtCompName1_2.setEditable(True)

        self.horizontalLayout_32.addWidget(self.txtCompName1_2)


        self.verticalLayout_20.addWidget(self.gSlogin_4)

        self.tabTelegram.addTab(self.tab_tg_1, "")
        self.tab_tg_2 = QWidget()
        self.tab_tg_2.setObjectName(u"tab_tg_2")
        self.layoutWidget5 = QWidget(self.tab_tg_2)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(20, 10, 1031, 110))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget5)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.cmdMemCategory2 = QComboBox(self.layoutWidget5)
        self.cmdMemCategory2.setObjectName(u"cmdMemCategory2")
        self.cmdMemCategory2.setEditable(True)

        self.verticalLayout_9.addWidget(self.cmdMemCategory2)

        self.label_7 = QLabel(self.layoutWidget5)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.txtListOfGroup2 = QLineEdit(self.layoutWidget5)
        self.txtListOfGroup2.setObjectName(u"txtListOfGroup2")

        self.horizontalLayout_33.addWidget(self.txtListOfGroup2)

        self.btnBrowser2 = QToolButton(self.layoutWidget5)
        self.btnBrowser2.setObjectName(u"btnBrowser2")

        self.horizontalLayout_33.addWidget(self.btnBrowser2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_33)

        self.tabTelegram.addTab(self.tab_tg_2, "")
        self.tab_tg_3 = QWidget()
        self.tab_tg_3.setObjectName(u"tab_tg_3")
        self.layoutWidget6 = QWidget(self.tab_tg_3)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 10, 1041, 371))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget6)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_23.addWidget(self.label_8)

        self.cmbCpyFrom = QComboBox(self.layoutWidget6)
        self.cmbCpyFrom.setObjectName(u"cmbCpyFrom")
        sizePolicy2.setHeightForWidth(self.cmbCpyFrom.sizePolicy().hasHeightForWidth())
        self.cmbCpyFrom.setSizePolicy(sizePolicy2)

        self.verticalLayout_23.addWidget(self.cmbCpyFrom)

        self.label_9 = QLabel(self.layoutWidget6)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_23.addWidget(self.label_9)

        self.txtCpyTo = QLineEdit(self.layoutWidget6)
        self.txtCpyTo.setObjectName(u"txtCpyTo")

        self.verticalLayout_23.addWidget(self.txtCpyTo)

        self.label_10 = QLabel(self.layoutWidget6)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_23.addWidget(self.label_10)

        self.dateMax = QCalendarWidget(self.layoutWidget6)
        self.dateMax.setObjectName(u"dateMax")
        sizePolicy1.setHeightForWidth(self.dateMax.sizePolicy().hasHeightForWidth())
        self.dateMax.setSizePolicy(sizePolicy1)
        self.dateMax.setGridVisible(False)

        self.verticalLayout_23.addWidget(self.dateMax)

        self.tabTelegram.addTab(self.tab_tg_3, "")
        self.tab_tg_4 = QWidget()
        self.tab_tg_4.setObjectName(u"tab_tg_4")
        self.layoutWidget7 = QWidget(self.tab_tg_4)
        self.layoutWidget7.setObjectName(u"layoutWidget7")
        self.layoutWidget7.setGeometry(QRect(10, 10, 1041, 238))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget7)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_24.addWidget(self.label_11)

        self.txtGroupName4 = QLineEdit(self.layoutWidget7)
        self.txtGroupName4.setObjectName(u"txtGroupName4")

        self.verticalLayout_24.addWidget(self.txtGroupName4)

        self.label_12 = QLabel(self.layoutWidget7)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_24.addWidget(self.label_12)

        self.cmdMemCategory4 = QComboBox(self.layoutWidget7)
        self.cmdMemCategory4.setObjectName(u"cmdMemCategory4")
        sizePolicy2.setHeightForWidth(self.cmdMemCategory4.sizePolicy().hasHeightForWidth())
        self.cmdMemCategory4.setSizePolicy(sizePolicy2)
        self.cmdMemCategory4.setEditable(True)

        self.verticalLayout_24.addWidget(self.cmdMemCategory4)

        self.groupBox_16 = QGroupBox(self.layoutWidget7)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(0, 96))
        self.layoutWidget8 = QWidget(self.groupBox_16)
        self.layoutWidget8.setObjectName(u"layoutWidget8")
        self.layoutWidget8.setGeometry(QRect(10, 40, 281, 26))
        self.horizontalLayout_35 = QHBoxLayout(self.layoutWidget8)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.radDatabase4 = QRadioButton(self.layoutWidget8)
        self.radDatabase4.setObjectName(u"radDatabase4")
        sizePolicy2.setHeightForWidth(self.radDatabase4.sizePolicy().hasHeightForWidth())
        self.radDatabase4.setSizePolicy(sizePolicy2)
        self.radDatabase4.setChecked(True)

        self.horizontalLayout_35.addWidget(self.radDatabase4)

        self.radFileList4 = QRadioButton(self.layoutWidget8)
        self.radFileList4.setObjectName(u"radFileList4")
        sizePolicy2.setHeightForWidth(self.radFileList4.sizePolicy().hasHeightForWidth())
        self.radFileList4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_35.addWidget(self.radFileList4)

        self.frmFileList4 = QFrame(self.groupBox_16)
        self.frmFileList4.setObjectName(u"frmFileList4")
        self.frmFileList4.setGeometry(QRect(340, 30, 691, 51))
        self.frmFileList4.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutWidget9 = QWidget(self.frmFileList4)
        self.layoutWidget9.setObjectName(u"layoutWidget9")
        self.layoutWidget9.setGeometry(QRect(10, 10, 671, 28))
        self.horizontalLayout_34 = QHBoxLayout(self.layoutWidget9)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_7 = QLineEdit(self.layoutWidget9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_34.addWidget(self.lineEdit_7)

        self.toolButton_5 = QToolButton(self.layoutWidget9)
        self.toolButton_5.setObjectName(u"toolButton_5")

        self.horizontalLayout_34.addWidget(self.toolButton_5)


        self.verticalLayout_24.addWidget(self.groupBox_16)

        self.tabTelegram.addTab(self.tab_tg_4, "")
        self.tabWhatsApp = QTabWidget(Dialog)
        self.tabWhatsApp.setObjectName(u"tabWhatsApp")
        self.tabWhatsApp.setGeometry(QRect(0, 0, 1061, 701))
        self.tab_wp_1 = QWidget()
        self.tab_wp_1.setObjectName(u"tab_wp_1")
        self.groupBox_10 = QGroupBox(self.tab_wp_1)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(21, 11, 1030, 43))
        self.groupBox_10.setMinimumSize(QSize(1030, 0))
        self.groupBox_10.setMaximumSize(QSize(1040, 43))
        self.layoutWidget_2 = QWidget(self.groupBox_10)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(370, 10, 291, 26))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.useWPAI_1 = QRadioButton(self.layoutWidget_2)
        self.useWPAI_1.setObjectName(u"useWPAI_1")

        self.horizontalLayout_12.addWidget(self.useWPAI_1)

        self.useWPCompan_1 = QRadioButton(self.layoutWidget_2)
        self.useWPCompan_1.setObjectName(u"useWPCompan_1")

        self.horizontalLayout_12.addWidget(self.useWPCompan_1)

        self.useFP_Nothing_3 = QRadioButton(self.layoutWidget_2)
        self.useFP_Nothing_3.setObjectName(u"useFP_Nothing_3")
        self.useFP_Nothing_3.setChecked(True)

        self.horizontalLayout_12.addWidget(self.useFP_Nothing_3)

        self.layoutWidget10 = QWidget(self.tab_wp_1)
        self.layoutWidget10.setObjectName(u"layoutWidget10")
        self.layoutWidget10.setGeometry(QRect(21, 60, 1031, 601))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gSlogin_3 = QGroupBox(self.layoutWidget10)
        self.gSlogin_3.setObjectName(u"gSlogin_3")
        sizePolicy1.setHeightForWidth(self.gSlogin_3.sizePolicy().hasHeightForWidth())
        self.gSlogin_3.setSizePolicy(sizePolicy1)
        self.gSlogin_3.setMinimumSize(QSize(988, 48))
        self.gSlogin_3.setMaximumSize(QSize(1038, 48))
        self.gSlogin_3.setFlat(True)
        self.layoutWidget_3 = QWidget(self.gSlogin_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 10, 1001, 28))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.layoutWidget_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(102, 0))
        self.label_30.setMaximumSize(QSize(42, 16777215))

        self.horizontalLayout_14.addWidget(self.label_30)

        self.txtWPCompName_1 = QComboBox(self.layoutWidget_3)
        self.txtWPCompName_1.setObjectName(u"txtWPCompName_1")
        self.txtWPCompName_1.setMinimumSize(QSize(771, 0))
        self.txtWPCompName_1.setMaximumSize(QSize(900, 16777215))
        self.txtWPCompName_1.setEditable(True)

        self.horizontalLayout_14.addWidget(self.txtWPCompName_1)


        self.verticalLayout_12.addWidget(self.gSlogin_3)

        self.groupBox_9 = QGroupBox(self.layoutWidget10)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy1.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy1)
        self.groupBox_9.setMaximumSize(QSize(16777215, 239))
        self.layoutWidget11 = QWidget(self.groupBox_9)
        self.layoutWidget11.setObjectName(u"layoutWidget11")
        self.layoutWidget11.setGeometry(QRect(20, 35, 999, 181))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_14 = QLabel(self.layoutWidget11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(69, 0))
        self.label_14.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_18.addWidget(self.label_14)

        self.textEdit_2 = QTextEdit(self.layoutWidget11)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(920, 0))
        self.textEdit_2.setMaximumSize(QSize(1000, 104))

        self.horizontalLayout_18.addWidget(self.textEdit_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_33 = QLabel(self.layoutWidget11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_40.addWidget(self.label_33)

        self.lineEdit_20 = QLineEdit(self.layoutWidget11)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.horizontalLayout_40.addWidget(self.lineEdit_20)

        self.comboBox_12 = QComboBox(self.layoutWidget11)
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setMinimumSize(QSize(197, 0))

        self.horizontalLayout_40.addWidget(self.comboBox_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_17 = QLabel(self.layoutWidget11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(463, 16777215))

        self.horizontalLayout_16.addWidget(self.label_17)

        self.label_16 = QLabel(self.layoutWidget11)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)


        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lineEdit_8 = QLineEdit(self.layoutWidget11)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_17.addWidget(self.lineEdit_8)

        self.toolButton_6 = QToolButton(self.layoutWidget11)
        self.toolButton_6.setObjectName(u"toolButton_6")

        self.horizontalLayout_17.addWidget(self.toolButton_6)

        self.lineEdit_10 = QLineEdit(self.layoutWidget11)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_17.addWidget(self.lineEdit_10)

        self.toolButton_8 = QToolButton(self.layoutWidget11)
        self.toolButton_8.setObjectName(u"toolButton_8")

        self.horizontalLayout_17.addWidget(self.toolButton_8)

        self.chkBoth = QCheckBox(self.layoutWidget11)
        self.chkBoth.setObjectName(u"chkBoth")

        self.horizontalLayout_17.addWidget(self.chkBoth)


        self.verticalLayout_4.addLayout(self.horizontalLayout_17)


        self.verticalLayout_12.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.layoutWidget10)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy1.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy1)
        self.groupBox_8.setMaximumSize(QSize(16777215, 104))
        self.layoutWidget12 = QWidget(self.groupBox_8)
        self.layoutWidget12.setObjectName(u"layoutWidget12")
        self.layoutWidget12.setGeometry(QRect(20, 30, 1001, 61))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget12)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_18 = QLabel(self.layoutWidget12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(500, 0))
        self.label_18.setMaximumSize(QSize(500, 16777215))

        self.horizontalLayout_19.addWidget(self.label_18)

        self.label_34 = QLabel(self.layoutWidget12)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(137, 16777215))

        self.horizontalLayout_19.addWidget(self.label_34)

        self.label_35 = QLabel(self.layoutWidget12)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_19.addWidget(self.label_35)

        self.label_13 = QLabel(self.layoutWidget12)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_19.addWidget(self.label_13)


        self.verticalLayout_10.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.comboBox_5 = QComboBox(self.layoutWidget12)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(500, 0))
        self.comboBox_5.setMaximumSize(QSize(500, 16777215))
        self.comboBox_5.setEditable(True)

        self.horizontalLayout_20.addWidget(self.comboBox_5)

        self.cmbBCountry = QComboBox(self.layoutWidget12)
        self.cmbBCountry.setObjectName(u"cmbBCountry")

        self.horizontalLayout_20.addWidget(self.cmbBCountry)

        self.combTimeZone = QComboBox(self.layoutWidget12)
        self.combTimeZone.setObjectName(u"combTimeZone")

        self.horizontalLayout_20.addWidget(self.combTimeZone)

        self.ckTranslat = QCheckBox(self.layoutWidget12)
        self.ckTranslat.setObjectName(u"ckTranslat")

        self.horizontalLayout_20.addWidget(self.ckTranslat)


        self.verticalLayout_10.addLayout(self.horizontalLayout_20)


        self.verticalLayout_12.addWidget(self.groupBox_8)

        self.groupBox_7 = QGroupBox(self.layoutWidget10)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.groupBox_7.setMinimumSize(QSize(0, 10))
        self.groupBox_7.setMaximumSize(QSize(16777215, 85))
        self.frm_wp_1 = QFrame(self.groupBox_7)
        self.frm_wp_1.setObjectName(u"frm_wp_1")
        self.frm_wp_1.setGeometry(QRect(250, 30, 761, 40))
        self.frm_wp_1.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutWidget13 = QWidget(self.frm_wp_1)
        self.layoutWidget13.setObjectName(u"layoutWidget13")
        self.layoutWidget13.setGeometry(QRect(10, 10, 731, 28))
        self.horizontalLayout_21 = QHBoxLayout(self.layoutWidget13)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_9 = QLineEdit(self.layoutWidget13)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_21.addWidget(self.lineEdit_9)

        self.toolButton_7 = QToolButton(self.layoutWidget13)
        self.toolButton_7.setObjectName(u"toolButton_7")

        self.horizontalLayout_21.addWidget(self.toolButton_7)

        self.layoutWidget14 = QWidget(self.groupBox_7)
        self.layoutWidget14.setObjectName(u"layoutWidget14")
        self.layoutWidget14.setGeometry(QRect(20, 40, 241, 26))
        self.horizontalLayout_22 = QHBoxLayout(self.layoutWidget14)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.radioButton_5 = QRadioButton(self.layoutWidget14)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setChecked(True)

        self.horizontalLayout_22.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.layoutWidget14)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.horizontalLayout_22.addWidget(self.radioButton_6)


        self.verticalLayout_12.addWidget(self.groupBox_7)

        self.tabWhatsApp.addTab(self.tab_wp_1, "")
        self.tab_wp_2 = QWidget()
        self.tab_wp_2.setObjectName(u"tab_wp_2")
        self.layoutWidget15 = QWidget(self.tab_wp_2)
        self.layoutWidget15.setObjectName(u"layoutWidget15")
        self.layoutWidget15.setGeometry(QRect(20, 45, 1021, 52))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.layoutWidget15)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_13.addWidget(self.label_37)

        self.comContactCategory = QComboBox(self.layoutWidget15)
        self.comContactCategory.setObjectName(u"comContactCategory")
        sizePolicy2.setHeightForWidth(self.comContactCategory.sizePolicy().hasHeightForWidth())
        self.comContactCategory.setSizePolicy(sizePolicy2)
        self.comContactCategory.setEditable(True)

        self.verticalLayout_13.addWidget(self.comContactCategory)

        self.layoutWidget16 = QWidget(self.tab_wp_2)
        self.layoutWidget16.setObjectName(u"layoutWidget16")
        self.layoutWidget16.setGeometry(QRect(20, 120, 1021, 221))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget16)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy3)
        self.pushButton.setMinimumSize(QSize(0, 100))

        self.verticalLayout_14.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.layoutWidget16)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(0, 100))
        self.pushButton_2.setSizeIncrement(QSize(0, 100))
        self.pushButton_2.setBaseSize(QSize(0, 100))

        self.verticalLayout_14.addWidget(self.pushButton_2)

        self.tabWhatsApp.addTab(self.tab_wp_2, "")
        self.tab_wp_3 = QWidget()
        self.tab_wp_3.setObjectName(u"tab_wp_3")
        self.layoutWidget17 = QWidget(self.tab_wp_3)
        self.layoutWidget17.setObjectName(u"layoutWidget17")
        self.layoutWidget17.setGeometry(QRect(10, 10, 1041, 251))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget17)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_19 = QLabel(self.layoutWidget17)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_15.addWidget(self.label_19)

        self.lineEdit_12 = QLineEdit(self.layoutWidget17)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_15.addWidget(self.lineEdit_12)


        self.verticalLayout_17.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_21 = QLabel(self.layoutWidget17)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_16.addWidget(self.label_21)

        self.comboBox_6 = QComboBox(self.layoutWidget17)
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy2.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy2)
        self.comboBox_6.setEditable(True)

        self.verticalLayout_16.addWidget(self.comboBox_6)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)

        self.groupBox_11 = QGroupBox(self.layoutWidget17)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.layoutWidget18 = QWidget(self.groupBox_11)
        self.layoutWidget18.setObjectName(u"layoutWidget18")
        self.layoutWidget18.setGeometry(QRect(20, 40, 251, 26))
        self.horizontalLayout_25 = QHBoxLayout(self.layoutWidget18)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.radioButton_8 = QRadioButton(self.layoutWidget18)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setChecked(True)

        self.horizontalLayout_25.addWidget(self.radioButton_8)

        self.radioButton_7 = QRadioButton(self.layoutWidget18)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.horizontalLayout_25.addWidget(self.radioButton_7)

        self.frm_wp_3 = QFrame(self.groupBox_11)
        self.frm_wp_3.setObjectName(u"frm_wp_3")
        self.frm_wp_3.setGeometry(QRect(260, 30, 771, 51))
        sizePolicy1.setHeightForWidth(self.frm_wp_3.sizePolicy().hasHeightForWidth())
        self.frm_wp_3.setSizePolicy(sizePolicy1)
        self.frm_wp_3.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutWidget19 = QWidget(self.frm_wp_3)
        self.layoutWidget19.setObjectName(u"layoutWidget19")
        self.layoutWidget19.setGeometry(QRect(10, 10, 751, 28))
        self.horizontalLayout_24 = QHBoxLayout(self.layoutWidget19)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_11 = QLineEdit(self.layoutWidget19)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_24.addWidget(self.lineEdit_11)

        self.toolButton_9 = QToolButton(self.layoutWidget19)
        self.toolButton_9.setObjectName(u"toolButton_9")

        self.horizontalLayout_24.addWidget(self.toolButton_9)


        self.verticalLayout_17.addWidget(self.groupBox_11)

        self.tabWhatsApp.addTab(self.tab_wp_3, "")
        self.tabFacebook = QTabWidget(Dialog)
        self.tabFacebook.setObjectName(u"tabFacebook")
        self.tabFacebook.setGeometry(QRect(0, 0, 1061, 701))
        self.tab_fb_1 = QWidget()
        self.tab_fb_1.setObjectName(u"tab_fb_1")
        self.layoutWidget20 = QWidget(self.tab_fb_1)
        self.layoutWidget20.setObjectName(u"layoutWidget20")
        self.layoutWidget20.setGeometry(QRect(10, 0, 1050, 452))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 0, 5, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.groupBox_2 = QGroupBox(self.layoutWidget20)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.layoutWidget21 = QWidget(self.groupBox_2)
        self.layoutWidget21.setObjectName(u"layoutWidget21")
        self.layoutWidget21.setGeometry(QRect(330, 10, 289, 26))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget21)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.useFPAI_1 = QRadioButton(self.layoutWidget21)
        self.useFPAI_1.setObjectName(u"useFPAI_1")

        self.horizontalLayout_6.addWidget(self.useFPAI_1)

        self.useCompan_1 = QRadioButton(self.layoutWidget21)
        self.useCompan_1.setObjectName(u"useCompan_1")

        self.horizontalLayout_6.addWidget(self.useCompan_1)

        self.useFP_Nothing_1 = QRadioButton(self.layoutWidget21)
        self.useFP_Nothing_1.setObjectName(u"useFP_Nothing_1")
        self.useFP_Nothing_1.setChecked(True)

        self.horizontalLayout_6.addWidget(self.useFP_Nothing_1)


        self.verticalLayout_21.addWidget(self.groupBox_2)

        self.gSlogin = QGroupBox(self.layoutWidget20)
        self.gSlogin.setObjectName(u"gSlogin")
        sizePolicy1.setHeightForWidth(self.gSlogin.sizePolicy().hasHeightForWidth())
        self.gSlogin.setSizePolicy(sizePolicy1)
        self.gSlogin.setMinimumSize(QSize(1038, 48))
        self.gSlogin.setMaximumSize(QSize(1038, 48))
        self.gSlogin.setFlat(True)
        self.layoutWidget22 = QWidget(self.gSlogin)
        self.layoutWidget22.setObjectName(u"layoutWidget22")
        self.layoutWidget22.setGeometry(QRect(11, 10, 1021, 28))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.layoutWidget22)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(42, 0))
        self.label_23.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout.addWidget(self.label_23)

        self.txtCompName1 = QComboBox(self.layoutWidget22)
        self.txtCompName1.setObjectName(u"txtCompName1")
        self.txtCompName1.setEditable(True)

        self.horizontalLayout.addWidget(self.txtCompName1)


        self.verticalLayout_21.addWidget(self.gSlogin)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.groupBox_3 = QGroupBox(self.layoutWidget20)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(0, 280))
        self.textEdit_3 = QTextEdit(self.groupBox_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(80, 25, 951, 121))
        self.textEdit_3.setMinimumSize(QSize(0, 120))
        self.textEdit_3.setMaximumSize(QSize(16777215, 126))
        self.textEdit_3.setSizeIncrement(QSize(0, 120))
        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(11, 31, 59, 18))
        self.layoutWidget23 = QWidget(self.groupBox_3)
        self.layoutWidget23.setObjectName(u"layoutWidget23")
        self.layoutWidget23.setGeometry(QRect(0, 189, 1031, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget23)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_26 = QLabel(self.layoutWidget23)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 26))
        self.label_26.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_3.addWidget(self.label_26)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(7, -1, 7, -1)
        self.lineEdit_14 = QLineEdit(self.layoutWidget23)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_3.addWidget(self.lineEdit_14)

        self.toolButton_10 = QToolButton(self.layoutWidget23)
        self.toolButton_10.setObjectName(u"toolButton_10")

        self.horizontalLayout_3.addWidget(self.toolButton_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_22 = QLabel(self.layoutWidget23)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 26))
        self.label_22.setMaximumSize(QSize(16777215, 26))

        self.verticalLayout_2.addWidget(self.label_22)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(7, -1, 7, -1)
        self.lineEdit_15 = QLineEdit(self.layoutWidget23)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.horizontalLayout_4.addWidget(self.lineEdit_15)

        self.toolButton_11 = QToolButton(self.layoutWidget23)
        self.toolButton_11.setObjectName(u"toolButton_11")

        self.horizontalLayout_4.addWidget(self.toolButton_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.ckBoth1 = QCheckBox(self.layoutWidget23)
        self.ckBoth1.setObjectName(u"ckBoth1")

        self.horizontalLayout_2.addWidget(self.ckBoth1)

        self.layoutWidget24 = QWidget(self.groupBox_3)
        self.layoutWidget24.setObjectName(u"layoutWidget24")
        self.layoutWidget24.setGeometry(QRect(10, 150, 1021, 28))
        self.horizontalLayout_36 = QHBoxLayout(self.layoutWidget24)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget24)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_36.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.layoutWidget24)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_36.addWidget(self.lineEdit_5)

        self.comboBox_3 = QComboBox(self.layoutWidget24)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(197, 0))

        self.horizontalLayout_36.addWidget(self.comboBox_3)


        self.verticalLayout_22.addWidget(self.groupBox_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_24 = QLabel(self.layoutWidget20)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(135, 18))
        self.label_24.setMaximumSize(QSize(135, 18))
        self.label_24.setSizeIncrement(QSize(135, 18))
        self.label_24.setBaseSize(QSize(135, 18))

        self.verticalLayout.addWidget(self.label_24)

        self.comboBox_7 = QComboBox(self.layoutWidget20)
        self.comboBox_7.setObjectName(u"comboBox_7")
        sizePolicy2.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy2)
        self.comboBox_7.setMinimumSize(QSize(0, 35))
        self.comboBox_7.setMaximumSize(QSize(16777215, 35))
        self.comboBox_7.setEditable(True)

        self.verticalLayout.addWidget(self.comboBox_7)


        self.verticalLayout_22.addLayout(self.verticalLayout)

        self.tabFacebook.addTab(self.tab_fb_1, "")
        self.tab_fb_2 = QWidget()
        self.tab_fb_2.setObjectName(u"tab_fb_2")
        self.groupBox = QGroupBox(self.tab_fb_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 0, 1039, 51))
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.layoutWidget25 = QWidget(self.groupBox)
        self.layoutWidget25.setObjectName(u"layoutWidget25")
        self.layoutWidget25.setGeometry(QRect(330, 10, 289, 26))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget25)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.useFPAI_2 = QRadioButton(self.layoutWidget25)
        self.useFPAI_2.setObjectName(u"useFPAI_2")
        self.useFPAI_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_11.addWidget(self.useFPAI_2)

        self.useCompan_2 = QRadioButton(self.layoutWidget25)
        self.useCompan_2.setObjectName(u"useCompan_2")
        self.useCompan_2.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout_11.addWidget(self.useCompan_2)

        self.useFP_Nothing_2 = QRadioButton(self.layoutWidget25)
        self.useFP_Nothing_2.setObjectName(u"useFP_Nothing_2")
        self.useFP_Nothing_2.setMaximumSize(QSize(86, 16777215))
        self.useFP_Nothing_2.setChecked(True)

        self.horizontalLayout_11.addWidget(self.useFP_Nothing_2)

        self.gSlogin_2 = QGroupBox(self.tab_fb_2)
        self.gSlogin_2.setObjectName(u"gSlogin_2")
        self.gSlogin_2.setGeometry(QRect(10, 40, 1039, 51))
        sizePolicy1.setHeightForWidth(self.gSlogin_2.sizePolicy().hasHeightForWidth())
        self.gSlogin_2.setSizePolicy(sizePolicy1)
        self.gSlogin_2.setFlat(True)
        self.layoutWidget26 = QWidget(self.gSlogin_2)
        self.layoutWidget26.setObjectName(u"layoutWidget26")
        self.layoutWidget26.setGeometry(QRect(11, 10, 1021, 28))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget26)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.layoutWidget26)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(42, 0))
        self.label_38.setMaximumSize(QSize(111, 16777215))

        self.horizontalLayout_5.addWidget(self.label_38)

        self.txtCompName2 = QComboBox(self.layoutWidget26)
        self.txtCompName2.setObjectName(u"txtCompName2")
        self.txtCompName2.setEditable(True)

        self.horizontalLayout_5.addWidget(self.txtCompName2)

        self.groupBox_4 = QGroupBox(self.tab_fb_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(10, 90, 1039, 261))
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.layoutWidget27 = QWidget(self.groupBox_4)
        self.layoutWidget27.setObjectName(u"layoutWidget27")
        self.layoutWidget27.setGeometry(QRect(10, 30, 1021, 128))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget27)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.layoutWidget27)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 20))
        self.label_27.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_7.addWidget(self.label_27)

        self.textEdit_4 = QTextEdit(self.layoutWidget27)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMinimumSize(QSize(0, 126))
        self.textEdit_4.setMaximumSize(QSize(16777215, 126))

        self.horizontalLayout_7.addWidget(self.textEdit_4)

        self.layoutWidget28 = QWidget(self.groupBox_4)
        self.layoutWidget28.setObjectName(u"layoutWidget28")
        self.layoutWidget28.setGeometry(QRect(10, 189, 1021, 61))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget28)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_29 = QLabel(self.layoutWidget28)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_7.addWidget(self.label_29)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_16 = QLineEdit(self.layoutWidget28)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.horizontalLayout_8.addWidget(self.lineEdit_16)

        self.toolButton_15 = QToolButton(self.layoutWidget28)
        self.toolButton_15.setObjectName(u"toolButton_15")

        self.horizontalLayout_8.addWidget(self.toolButton_15)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_39 = QLabel(self.layoutWidget28)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_8.addWidget(self.label_39)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_19 = QLineEdit(self.layoutWidget28)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.horizontalLayout_9.addWidget(self.lineEdit_19)

        self.toolButton_12 = QToolButton(self.layoutWidget28)
        self.toolButton_12.setObjectName(u"toolButton_12")

        self.horizontalLayout_9.addWidget(self.toolButton_12)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_8)

        self.checkBox_2 = QCheckBox(self.layoutWidget28)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.horizontalLayout_10.addWidget(self.checkBox_2)

        self.layoutWidget_6 = QWidget(self.groupBox_4)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 160, 1021, 28))
        self.horizontalLayout_38 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(58, 0))

        self.horizontalLayout_38.addWidget(self.label_15)

        self.lineEdit_13 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_38.addWidget(self.lineEdit_13)

        self.comboBox_10 = QComboBox(self.layoutWidget_6)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMinimumSize(QSize(197, 0))

        self.horizontalLayout_38.addWidget(self.comboBox_10)

        self.layoutWidget29 = QWidget(self.tab_fb_2)
        self.layoutWidget29.setObjectName(u"layoutWidget29")
        self.layoutWidget29.setGeometry(QRect(10, 350, 1041, 71))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget29)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.layoutWidget29)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(108, 16777215))

        self.verticalLayout_6.addWidget(self.label_28)

        self.comboBox_8 = QComboBox(self.layoutWidget29)
        self.comboBox_8.setObjectName(u"comboBox_8")
        sizePolicy2.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy2)
        self.comboBox_8.setMinimumSize(QSize(0, 35))
        self.comboBox_8.setMaximumSize(QSize(16777215, 35))
        self.comboBox_8.setEditable(True)

        self.verticalLayout_6.addWidget(self.comboBox_8)

        self.groupBox_6 = QGroupBox(self.tab_fb_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(40, 430, 961, 61))
        sizePolicy1.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy1)
        self.groupBox_5 = QGroupBox(self.groupBox_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(410, 20, 541, 41))
        self.groupBox_5.setMaximumSize(QSize(600, 16777215))
        self.lineEdit_4 = QLineEdit(self.groupBox_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(13, 9, 500, 26))
        self.lineEdit_4.setMaximumSize(QSize(500, 16777215))
        self.toolButton_13 = QToolButton(self.groupBox_5)
        self.toolButton_13.setObjectName(u"toolButton_13")
        self.toolButton_13.setGeometry(QRect(510, 10, 26, 25))
        self.layoutWidget30 = QWidget(self.groupBox_6)
        self.layoutWidget30.setObjectName(u"layoutWidget30")
        self.layoutWidget30.setGeometry(QRect(10, 30, 371, 26))
        self.horizontalLayout_37 = QHBoxLayout(self.layoutWidget30)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.radioButton_11 = QRadioButton(self.layoutWidget30)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setMinimumSize(QSize(91, 0))
        self.radioButton_11.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_11.setChecked(True)

        self.horizontalLayout_37.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.layoutWidget30)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setMinimumSize(QSize(80, 0))
        self.radioButton_12.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_37.addWidget(self.radioButton_12)

        self.tabFacebook.addTab(self.tab_fb_2, "")
        self.tab_fb_3 = QWidget()
        self.tab_fb_3.setObjectName(u"tab_fb_3")
        self.layoutWidget31 = QWidget(self.tab_fb_3)
        self.layoutWidget31.setObjectName(u"layoutWidget31")
        self.layoutWidget31.setGeometry(QRect(10, 10, 1031, 52))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget31)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.layoutWidget31)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_5.addWidget(self.label_31)

        self.comboBox_2 = QComboBox(self.layoutWidget31)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy2.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy2)
        self.comboBox_2.setEditable(True)

        self.verticalLayout_5.addWidget(self.comboBox_2)

        self.layoutWidget32 = QWidget(self.tab_fb_3)
        self.layoutWidget32.setObjectName(u"layoutWidget32")
        self.layoutWidget32.setGeometry(QRect(10, 80, 1031, 52))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget32)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.layoutWidget32)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_11.addWidget(self.label_32)

        self.comboBox_9 = QComboBox(self.layoutWidget32)
        self.comboBox_9.setObjectName(u"comboBox_9")
        sizePolicy2.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy2)
        self.comboBox_9.setEditable(True)

        self.verticalLayout_11.addWidget(self.comboBox_9)

        self.groupBox_15 = QGroupBox(self.tab_fb_3)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 140, 1031, 91))
        self.frame_3 = QFrame(self.groupBox_15)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(300, 30, 721, 52))
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.layoutWidget33 = QWidget(self.frame_3)
        self.layoutWidget33.setObjectName(u"layoutWidget33")
        self.layoutWidget33.setGeometry(QRect(10, 10, 701, 28))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget33)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_18 = QLineEdit(self.layoutWidget33)
        self.lineEdit_18.setObjectName(u"lineEdit_18")
        self.lineEdit_18.setMinimumSize(QSize(40, 0))
        self.lineEdit_18.setMaximumSize(QSize(664, 16777215))

        self.horizontalLayout_13.addWidget(self.lineEdit_18)

        self.toolButton_14 = QToolButton(self.layoutWidget33)
        self.toolButton_14.setObjectName(u"toolButton_14")

        self.horizontalLayout_13.addWidget(self.toolButton_14)

        self.toolButton_14.raise_()
        self.lineEdit_18.raise_()
        self.layoutWidget34 = QWidget(self.groupBox_15)
        self.layoutWidget34.setObjectName(u"layoutWidget34")
        self.layoutWidget34.setGeometry(QRect(10, 40, 301, 26))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget34)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.radioButton_13 = QRadioButton(self.layoutWidget34)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setMinimumSize(QSize(92, 0))
        self.radioButton_13.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_13.setChecked(True)

        self.horizontalLayout_15.addWidget(self.radioButton_13)

        self.radioButton_14 = QRadioButton(self.layoutWidget34)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_15.addWidget(self.radioButton_14)

        self.tabFacebook.addTab(self.tab_fb_3, "")
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(890, 710, 166, 26))
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.layoutWidget35 = QWidget(Dialog)
        self.layoutWidget35.setObjectName(u"layoutWidget35")
        self.layoutWidget35.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget35)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.tabWhatsApp.raise_()
        self.tabTelegram.raise_()
        self.layoutWidget29.raise_()
        self.buttonBox.raise_()
        self.tabFacebook.raise_()
        QWidget.setTabOrder(self.textEdit_2, self.textEdit_4)
        QWidget.setTabOrder(self.textEdit_4, self.lineEdit_16)
        QWidget.setTabOrder(self.lineEdit_16, self.toolButton_15)
        QWidget.setTabOrder(self.toolButton_15, self.lineEdit_19)
        QWidget.setTabOrder(self.lineEdit_19, self.toolButton_12)
        QWidget.setTabOrder(self.toolButton_12, self.radioButton_11)
        QWidget.setTabOrder(self.radioButton_11, self.radioButton_12)
        QWidget.setTabOrder(self.radioButton_12, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.toolButton_13)
        QWidget.setTabOrder(self.toolButton_13, self.useFPAI_2)
        QWidget.setTabOrder(self.useFPAI_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.cmdMemCategory2)
        QWidget.setTabOrder(self.cmdMemCategory2, self.txtListOfGroup2)
        QWidget.setTabOrder(self.txtListOfGroup2, self.btnBrowser2)
        QWidget.setTabOrder(self.btnBrowser2, self.cmbCpyFrom)
        QWidget.setTabOrder(self.cmbCpyFrom, self.txtCpyTo)
        QWidget.setTabOrder(self.txtCpyTo, self.dateMax)
        QWidget.setTabOrder(self.dateMax, self.txtGroupName4)
        QWidget.setTabOrder(self.txtGroupName4, self.cmdMemCategory4)
        QWidget.setTabOrder(self.cmdMemCategory4, self.radDatabase4)
        QWidget.setTabOrder(self.radDatabase4, self.radFileList4)
        QWidget.setTabOrder(self.radFileList4, self.lineEdit_7)
        QWidget.setTabOrder(self.lineEdit_7, self.toolButton_5)
        QWidget.setTabOrder(self.toolButton_5, self.lineEdit_8)
        QWidget.setTabOrder(self.lineEdit_8, self.toolButton_6)
        QWidget.setTabOrder(self.toolButton_6, self.comboBox_5)
        QWidget.setTabOrder(self.comboBox_5, self.tabTelegram)
        QWidget.setTabOrder(self.tabTelegram, self.lineEdit_10)
        QWidget.setTabOrder(self.lineEdit_10, self.toolButton_8)
        QWidget.setTabOrder(self.toolButton_8, self.cmbBCountry)
        QWidget.setTabOrder(self.cmbBCountry, self.combTimeZone)
        QWidget.setTabOrder(self.combTimeZone, self.tabWhatsApp)
        QWidget.setTabOrder(self.tabWhatsApp, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.comContactCategory)
        QWidget.setTabOrder(self.comContactCategory, self.comboBox_6)
        QWidget.setTabOrder(self.comboBox_6, self.radioButton_7)
        QWidget.setTabOrder(self.radioButton_7, self.radioButton_8)
        QWidget.setTabOrder(self.radioButton_8, self.lineEdit_12)
        QWidget.setTabOrder(self.lineEdit_12, self.toolButton_9)
        QWidget.setTabOrder(self.toolButton_9, self.lineEdit_11)
        QWidget.setTabOrder(self.lineEdit_11, self.useFPAI_1)
        QWidget.setTabOrder(self.useFPAI_1, self.useCompan_1)
        QWidget.setTabOrder(self.useCompan_1, self.useFP_Nothing_1)
        QWidget.setTabOrder(self.useFP_Nothing_1, self.textEdit_3)
        QWidget.setTabOrder(self.textEdit_3, self.lineEdit_14)
        QWidget.setTabOrder(self.lineEdit_14, self.toolButton_10)
        QWidget.setTabOrder(self.toolButton_10, self.lineEdit_15)
        QWidget.setTabOrder(self.lineEdit_15, self.toolButton_11)
        QWidget.setTabOrder(self.toolButton_11, self.ckBoth1)
        QWidget.setTabOrder(self.ckBoth1, self.comboBox_7)
        QWidget.setTabOrder(self.comboBox_7, self.toolButton_3)
        QWidget.setTabOrder(self.toolButton_3, self.useCompan_2)
        QWidget.setTabOrder(self.useCompan_2, self.useFP_Nothing_2)
        QWidget.setTabOrder(self.useFP_Nothing_2, self.tabFacebook)
        QWidget.setTabOrder(self.tabFacebook, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.comboBox_8)
        QWidget.setTabOrder(self.comboBox_8, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.comboBox_9)
        QWidget.setTabOrder(self.comboBox_9, self.radioButton_13)
        QWidget.setTabOrder(self.radioButton_13, self.radioButton_14)
        QWidget.setTabOrder(self.radioButton_14, self.toolButton_14)
        QWidget.setTabOrder(self.toolButton_14, self.lineEdit_18)
        QWidget.setTabOrder(self.lineEdit_18, self.txtCompName1)
        QWidget.setTabOrder(self.txtCompName1, self.txtCompName2)
        QWidget.setTabOrder(self.txtCompName2, self.toolButton_2)
        QWidget.setTabOrder(self.toolButton_2, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.radDatabase1)
        QWidget.setTabOrder(self.radDatabase1, self.radFileList1)

        self.retranslateUi(Dialog)

        self.tabTelegram.setCurrentIndex(0)
        self.comboBox_11.setCurrentIndex(-1)
        self.tabWhatsApp.setCurrentIndex(0)
        self.comboBox_12.setCurrentIndex(-1)
        self.tabFacebook.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(-1)
        self.comboBox_10.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Marketing", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Dialog", u"Data Source", None))
        self.toolButton_3.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.radDatabase1.setText(QCoreApplication.translate("Dialog", u"Database", None))
        self.radFileList1.setText(QCoreApplication.translate("Dialog", u"File List", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Dialog", u"Message Aria", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Message", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Or Path To Message", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Or File To Send", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.toolButton_2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Slogin", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Members Category", None))
        self.groupBox_14.setTitle("")
        self.useTGAI.setText(QCoreApplication.translate("Dialog", u"Use AI", None))
        self.useTGCompan.setText(QCoreApplication.translate("Dialog", u"Use Compan ID", None))
        self.useFP_Nothing_4.setText(QCoreApplication.translate("Dialog", u"Nothing", None))
        self.gSlogin_4.setTitle("")
        self.label_36.setText(QCoreApplication.translate("Dialog", u"Compan Name", None))
        self.tabTelegram.setTabText(self.tabTelegram.indexOf(self.tab_tg_1), QCoreApplication.translate("Dialog", u"Send Message To Members", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Members Category", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Group File List", None))
        self.btnBrowser2.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.tabTelegram.setTabText(self.tabTelegram.indexOf(self.tab_tg_2), QCoreApplication.translate("Dialog", u"Get Members From Groups", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"From :", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"To :", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Only Message Befour this Date", None))
        self.tabTelegram.setTabText(self.tabTelegram.indexOf(self.tab_tg_3), QCoreApplication.translate("Dialog", u"Copy Message to Channel", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Group Name", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Member Category", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Dialog", u"Data Source", None))
        self.radDatabase4.setText(QCoreApplication.translate("Dialog", u"Database", None))
        self.radFileList4.setText(QCoreApplication.translate("Dialog", u"File List", None))
        self.toolButton_5.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.tabTelegram.setTabText(self.tabTelegram.indexOf(self.tab_tg_4), QCoreApplication.translate("Dialog", u"Add Member to Chanel", None))
        self.groupBox_10.setTitle("")
        self.useWPAI_1.setText(QCoreApplication.translate("Dialog", u"Use AI", None))
        self.useWPCompan_1.setText(QCoreApplication.translate("Dialog", u"Use Compan ID", None))
        self.useFP_Nothing_3.setText(QCoreApplication.translate("Dialog", u"Nothing", None))
        self.gSlogin_3.setTitle("")
        self.label_30.setText(QCoreApplication.translate("Dialog", u"Compan Name", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog", u"Message Aria", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"Message", None))
        self.label_33.setText(QCoreApplication.translate("Dialog", u"Slogin", None))
        self.comboBox_12.setCurrentText("")
        self.label_17.setText(QCoreApplication.translate("Dialog", u"Or Path To Message", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"Or File To Send", None))
        self.toolButton_6.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.toolButton_8.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.chkBoth.setText(QCoreApplication.translate("Dialog", u"Both", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dialog", u"Target Members", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"Members Category", None))
        self.label_34.setText(QCoreApplication.translate("Dialog", u"Country", None))
        self.label_35.setText(QCoreApplication.translate("Dialog", u"TimeZone", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Translat Message", None))
        self.ckTranslat.setText(QCoreApplication.translate("Dialog", u"Translat to Other Language", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"Data Source", None))
        self.toolButton_7.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.radioButton_5.setText(QCoreApplication.translate("Dialog", u"Database", None))
        self.radioButton_6.setText(QCoreApplication.translate("Dialog", u"File List", None))
        self.tabWhatsApp.setTabText(self.tabWhatsApp.indexOf(self.tab_wp_1), QCoreApplication.translate("Dialog", u"Send To Members", None))
        self.label_37.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Get My WhatsApp Contact Numbers", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Add Numbers from Excel or CSV File", None))
        self.tabWhatsApp.setTabText(self.tabWhatsApp.indexOf(self.tab_wp_2), QCoreApplication.translate("Dialog", u"Get Numbers from My Contact", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Group Name", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Member Category", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Dialog", u"Data Source", None))
        self.radioButton_8.setText(QCoreApplication.translate("Dialog", u"Database", None))
        self.radioButton_7.setText(QCoreApplication.translate("Dialog", u"File List", None))
        self.toolButton_9.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.tabWhatsApp.setTabText(self.tabWhatsApp.indexOf(self.tab_wp_3), QCoreApplication.translate("Dialog", u"Get Data from Groups", None))
        self.groupBox_2.setTitle("")
        self.useFPAI_1.setText(QCoreApplication.translate("Dialog", u"Use AI", None))
        self.useCompan_1.setText(QCoreApplication.translate("Dialog", u"Use Compan ID", None))
        self.useFP_Nothing_1.setText(QCoreApplication.translate("Dialog", u"Nothing", None))
        self.gSlogin.setTitle("")
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Compan Name", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Message Aria", None))
        self.label_25.setText(QCoreApplication.translate("Dialog", u"Message", None))
        self.label_26.setText(QCoreApplication.translate("Dialog", u"Or Path To Message", None))
        self.toolButton_10.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Or File To Send", None))
        self.toolButton_11.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.ckBoth1.setText(QCoreApplication.translate("Dialog", u"Both", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Slogin", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Members Category", None))
        self.tabFacebook.setTabText(self.tabFacebook.indexOf(self.tab_fb_1), QCoreApplication.translate("Dialog", u"Send To Members", None))
        self.groupBox.setTitle("")
        self.useFPAI_2.setText(QCoreApplication.translate("Dialog", u"Use AI", None))
        self.useCompan_2.setText(QCoreApplication.translate("Dialog", u"Use Compan ID", None))
        self.useFP_Nothing_2.setText(QCoreApplication.translate("Dialog", u"Nothing", None))
        self.gSlogin_2.setTitle("")
        self.label_38.setText(QCoreApplication.translate("Dialog", u"Compan Name", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"Message Aria", None))
        self.label_27.setText(QCoreApplication.translate("Dialog", u"Message", None))
        self.label_29.setText(QCoreApplication.translate("Dialog", u"Or Path To Message", None))
        self.toolButton_15.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_39.setText(QCoreApplication.translate("Dialog", u"Or File To Send", None))
        self.toolButton_12.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Both", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"Slogin", None))
        self.label_28.setText(QCoreApplication.translate("Dialog", u"Group Category", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Data Source", None))
        self.groupBox_5.setTitle("")
        self.toolButton_13.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.radioButton_11.setText(QCoreApplication.translate("Dialog", u"Database", None))
        self.radioButton_12.setText(QCoreApplication.translate("Dialog", u"File List", None))
        self.tabFacebook.setTabText(self.tabFacebook.indexOf(self.tab_fb_2), QCoreApplication.translate("Dialog", u"Post to Groups", None))
        self.label_31.setText(QCoreApplication.translate("Dialog", u"Group Name", None))
        self.label_32.setText(QCoreApplication.translate("Dialog", u"Member Category", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Dialog", u"Data Source", None))
        self.toolButton_14.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.radioButton_13.setText(QCoreApplication.translate("Dialog", u"Database", None))
        self.radioButton_14.setText(QCoreApplication.translate("Dialog", u"File List", None))
        self.tabFacebook.setTabText(self.tabFacebook.indexOf(self.tab_fb_3), QCoreApplication.translate("Dialog", u"Get Members fro Groups", None))
    # retranslateUi

