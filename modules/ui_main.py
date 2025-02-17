# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maintBOzic.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
from . resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_new = QPushButton(self.topMenu)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy)
        self.btn_new.setMinimumSize(QSize(0, 45))
        self.btn_new.setFont(font)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-paper-plane.png);")

        self.verticalLayout_8.addWidget(self.btn_new)

        self.btn_widgets = QPushButton(self.topMenu)
        self.btn_widgets.setObjectName(u"btn_widgets")
        sizePolicy.setHeightForWidth(self.btn_widgets.sizePolicy().hasHeightForWidth())
        self.btn_widgets.setSizePolicy(sizePolicy)
        self.btn_widgets.setMinimumSize(QSize(0, 45))
        self.btn_widgets.setFont(font)
        self.btn_widgets.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets.setAutoFillBackground(False)
        self.btn_widgets.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-action-undo);")

        self.verticalLayout_8.addWidget(self.btn_widgets)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)

        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.student_table = QWidget()
        self.student_table.setObjectName(u"student_table")
        self.gridLayout_4 = QGridLayout(self.student_table)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.welcome = QLabel(self.student_table)
        self.welcome.setObjectName(u"welcome")

        self.gridLayout_4.addWidget(self.welcome, 0, 1, 1, 1)

        self.btn_pwd_change = QPushButton(self.student_table)
        self.btn_pwd_change.setObjectName(u"btn_pwd_change")
        self.btn_pwd_change.setMinimumSize(QSize(150, 30))
        self.btn_pwd_change.setFont(font)
        self.btn_pwd_change.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pwd_change.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-pencil.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pwd_change.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_pwd_change, 1, 0, 1, 1)

        self.btn_course_check = QPushButton(self.student_table)
        self.btn_course_check.setObjectName(u"btn_course_check")
        self.btn_course_check.setMinimumSize(QSize(150, 30))
        self.btn_course_check.setFont(font)
        self.btn_course_check.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_course_check.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-view-quilt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_course_check.setIcon(icon5)

        self.gridLayout_4.addWidget(self.btn_course_check, 1, 2, 1, 1)

        self.btn_course_choose = QPushButton(self.student_table)
        self.btn_course_choose.setObjectName(u"btn_course_choose")
        self.btn_course_choose.setMinimumSize(QSize(150, 30))
        self.btn_course_choose.setFont(font)
        self.btn_course_choose.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_course_choose.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-hand-point-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_course_choose.setIcon(icon6)

        self.gridLayout_4.addWidget(self.btn_course_choose, 2, 0, 1, 1)

        self.btn_info_change = QPushButton(self.student_table)
        self.btn_info_change.setObjectName(u"btn_info_change")
        self.btn_info_change.setMinimumSize(QSize(150, 30))
        self.btn_info_change.setFont(font)
        self.btn_info_change.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_info_change.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_info_change.setIcon(icon7)

        self.gridLayout_4.addWidget(self.btn_info_change, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.student_table)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon8)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon9)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.teacher_table = QWidget()
        self.teacher_table.setObjectName(u"teacher_table")
        self.gridLayout_8 = QGridLayout(self.teacher_table)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.welcome_2 = QLabel(self.teacher_table)
        self.welcome_2.setObjectName(u"welcome_2")

        self.gridLayout_8.addWidget(self.welcome_2, 0, 0, 1, 2)

        self.btn_pwd_change_2 = QPushButton(self.teacher_table)
        self.btn_pwd_change_2.setObjectName(u"btn_pwd_change_2")
        self.btn_pwd_change_2.setMinimumSize(QSize(150, 30))
        self.btn_pwd_change_2.setFont(font)
        self.btn_pwd_change_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pwd_change_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_pwd_change_2.setIcon(icon4)

        self.gridLayout_8.addWidget(self.btn_pwd_change_2, 1, 0, 1, 1)

        self.btn_grade_change = QPushButton(self.teacher_table)
        self.btn_grade_change.setObjectName(u"btn_grade_change")
        self.btn_grade_change.setMinimumSize(QSize(150, 30))
        self.btn_grade_change.setFont(font)
        self.btn_grade_change.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_grade_change.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_grade_change.setIcon(icon6)

        self.gridLayout_8.addWidget(self.btn_grade_change, 1, 1, 1, 1)

        self.btn_course_check_2 = QPushButton(self.teacher_table)
        self.btn_course_check_2.setObjectName(u"btn_course_check_2")
        self.btn_course_check_2.setMinimumSize(QSize(150, 30))
        self.btn_course_check_2.setFont(font)
        self.btn_course_check_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_course_check_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_course_check_2.setIcon(icon5)

        self.gridLayout_8.addWidget(self.btn_course_check_2, 3, 0, 1, 1)

        self.btn_info_change_2 = QPushButton(self.teacher_table)
        self.btn_info_change_2.setObjectName(u"btn_info_change_2")
        self.btn_info_change_2.setMinimumSize(QSize(150, 30))
        self.btn_info_change_2.setFont(font)
        self.btn_info_change_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_info_change_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_info_change_2.setIcon(icon7)

        self.gridLayout_8.addWidget(self.btn_info_change_2, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.teacher_table)
        self.info_page = QWidget()
        self.info_page.setObjectName(u"info_page")
        self.gridLayout_19 = QGridLayout(self.info_page)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.btn_info_change_confirm_3 = QPushButton(self.info_page)
        self.btn_info_change_confirm_3.setObjectName(u"btn_info_change_confirm_3")
        self.btn_info_change_confirm_3.setMinimumSize(QSize(150, 30))
        self.btn_info_change_confirm_3.setFont(font)
        self.btn_info_change_confirm_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_info_change_confirm_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_info_change_confirm_3.setIcon(icon4)

        self.gridLayout_19.addWidget(self.btn_info_change_confirm_3, 3, 2, 1, 1)

        self.welcome_4 = QLabel(self.info_page)
        self.welcome_4.setObjectName(u"welcome_4")

        self.gridLayout_19.addWidget(self.welcome_4, 1, 0, 1, 1)

        self.changed_info = QLineEdit(self.info_page)
        self.changed_info.setObjectName(u"changed_info")
        self.changed_info.setMinimumSize(QSize(0, 30))
        self.changed_info.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_19.addWidget(self.changed_info, 2, 0, 1, 3)

        self.student_info = QTableWidget(self.info_page)
        if (self.student_info.columnCount() < 6):
            self.student_info.setColumnCount(6)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.student_info.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.student_info.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.student_info.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.student_info.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.student_info.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.student_info.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        if (self.student_info.rowCount() < 3):
            self.student_info.setRowCount(3)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font4);
        self.student_info.setVerticalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.student_info.setVerticalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.student_info.setVerticalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.student_info.setItem(0, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.student_info.setItem(0, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.student_info.setItem(0, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.student_info.setItem(0, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.student_info.setItem(0, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.student_info.setItem(0, 5, __qtablewidgetitem38)
        self.student_info.setObjectName(u"student_info")
        sizePolicy3.setHeightForWidth(self.student_info.sizePolicy().hasHeightForWidth())
        self.student_info.setSizePolicy(sizePolicy3)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.NoBrush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.student_info.setPalette(palette1)
        self.student_info.setFrameShape(QFrame.NoFrame)
        self.student_info.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.student_info.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.student_info.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.student_info.setSelectionMode(QAbstractItemView.SingleSelection)
        self.student_info.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.student_info.setShowGrid(True)
        self.student_info.setGridStyle(Qt.SolidLine)
        self.student_info.setSortingEnabled(False)
        self.student_info.horizontalHeader().setVisible(False)
        self.student_info.horizontalHeader().setCascadingSectionResizes(True)
        self.student_info.horizontalHeader().setDefaultSectionSize(200)
        self.student_info.horizontalHeader().setStretchLastSection(True)
        self.student_info.verticalHeader().setVisible(False)
        self.student_info.verticalHeader().setCascadingSectionResizes(False)
        self.student_info.verticalHeader().setHighlightSections(False)
        self.student_info.verticalHeader().setStretchLastSection(True)

        self.gridLayout_19.addWidget(self.student_info, 0, 0, 1, 3)

        self.select_info = QComboBox(self.info_page)
        self.select_info.addItem("")
        self.select_info.addItem("")
        self.select_info.addItem("")
        self.select_info.addItem("")
        self.select_info.setObjectName(u"select_info")
        self.select_info.setFont(font)
        self.select_info.setAutoFillBackground(False)
        self.select_info.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.select_info.setIconSize(QSize(16, 16))
        self.select_info.setFrame(True)

        self.gridLayout_19.addWidget(self.select_info, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.info_page)
        self.agent_table = QWidget()
        self.agent_table.setObjectName(u"agent_table")
        self.gridLayout_9 = QGridLayout(self.agent_table)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.welcome_3 = QLabel(self.agent_table)
        self.welcome_3.setObjectName(u"welcome_3")

        self.gridLayout_9.addWidget(self.welcome_3, 0, 0, 1, 1)

        self.btn_pwd_change_student = QPushButton(self.agent_table)
        self.btn_pwd_change_student.setObjectName(u"btn_pwd_change_student")
        self.btn_pwd_change_student.setMinimumSize(QSize(150, 30))
        self.btn_pwd_change_student.setFont(font)
        self.btn_pwd_change_student.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pwd_change_student.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_pwd_change_student.setIcon(icon4)

        self.gridLayout_9.addWidget(self.btn_pwd_change_student, 2, 1, 1, 1)

        self.btn_pwd_change_teacher = QPushButton(self.agent_table)
        self.btn_pwd_change_teacher.setObjectName(u"btn_pwd_change_teacher")
        self.btn_pwd_change_teacher.setMinimumSize(QSize(150, 30))
        self.btn_pwd_change_teacher.setFont(font)
        self.btn_pwd_change_teacher.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pwd_change_teacher.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_pwd_change_teacher.setIcon(icon4)

        self.gridLayout_9.addWidget(self.btn_pwd_change_teacher, 3, 0, 1, 1)

        self.btn_remove_course = QPushButton(self.agent_table)
        self.btn_remove_course.setObjectName(u"btn_remove_course")
        self.btn_remove_course.setMinimumSize(QSize(150, 30))
        self.btn_remove_course.setFont(font)
        self.btn_remove_course.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remove_course.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_remove_course.setIcon(icon4)

        self.gridLayout_9.addWidget(self.btn_remove_course, 4, 0, 1, 1)

        self.btn_course_info_edit = QPushButton(self.agent_table)
        self.btn_course_info_edit.setObjectName(u"btn_course_info_edit")
        self.btn_course_info_edit.setMinimumSize(QSize(150, 30))
        self.btn_course_info_edit.setFont(font)
        self.btn_course_info_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_course_info_edit.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_course_info_edit.setIcon(icon4)

        self.gridLayout_9.addWidget(self.btn_course_info_edit, 4, 1, 1, 1)

        self.btn_pwd_change_agent = QPushButton(self.agent_table)
        self.btn_pwd_change_agent.setObjectName(u"btn_pwd_change_agent")
        self.btn_pwd_change_agent.setMinimumSize(QSize(150, 30))
        self.btn_pwd_change_agent.setFont(font)
        self.btn_pwd_change_agent.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pwd_change_agent.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_pwd_change_agent.setIcon(icon4)

        self.gridLayout_9.addWidget(self.btn_pwd_change_agent, 2, 0, 1, 1)

        self.btn_add_course = QPushButton(self.agent_table)
        self.btn_add_course.setObjectName(u"btn_add_course")
        self.btn_add_course.setMinimumSize(QSize(150, 30))
        self.btn_add_course.setFont(font)
        self.btn_add_course.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_course.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_add_course.setIcon(icon4)

        self.gridLayout_9.addWidget(self.btn_add_course, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.agent_table)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.verticalLayout_20 = QVBoxLayout(self.login_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame = QFrame(self.login_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.id = QLineEdit(self.frame)
        self.id.setObjectName(u"id")
        self.id.setMinimumSize(QSize(0, 30))
        self.id.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.id, 1, 0, 1, 3)

        self.pwd = QLineEdit(self.frame)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setMinimumSize(QSize(0, 30))
        self.pwd.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_3.addWidget(self.pwd, 2, 0, 1, 3)

        self.btn_student_login = QPushButton(self.frame)
        self.btn_student_login.setObjectName(u"btn_student_login")
        self.btn_student_login.setMinimumSize(QSize(150, 30))
        self.btn_student_login.setFont(font)
        self.btn_student_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_student_login.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_student_login.setIcon(icon10)

        self.gridLayout_3.addWidget(self.btn_student_login, 3, 0, 1, 1)

        self.btn_teacher_login = QPushButton(self.frame)
        self.btn_teacher_login.setObjectName(u"btn_teacher_login")
        self.btn_teacher_login.setMinimumSize(QSize(150, 30))
        self.btn_teacher_login.setFont(font)
        self.btn_teacher_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_teacher_login.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_teacher_login.setIcon(icon11)

        self.gridLayout_3.addWidget(self.btn_teacher_login, 3, 1, 1, 1)

        self.btn_agent_login = QPushButton(self.frame)
        self.btn_agent_login.setObjectName(u"btn_agent_login")
        self.btn_agent_login.setMinimumSize(QSize(150, 30))
        self.btn_agent_login.setFont(font)
        self.btn_agent_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agent_login.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-user-female.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_agent_login.setIcon(icon12)

        self.gridLayout_3.addWidget(self.btn_agent_login, 3, 2, 1, 1)


        self.verticalLayout_20.addWidget(self.frame)

        self.stackedWidget.addWidget(self.login_page)
        self.check_page = QWidget()
        self.check_page.setObjectName(u"check_page")
        self.gridLayout_6 = QGridLayout(self.check_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.course_display = QTableWidget(self.check_page)
        if (self.course_display.columnCount() < 9):
            self.course_display.setColumnCount(9)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(6, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(7, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.course_display.setHorizontalHeaderItem(8, __qtablewidgetitem47)
        if (self.course_display.rowCount() < 16):
            self.course_display.setRowCount(16)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setFont(font4);
        self.course_display.setVerticalHeaderItem(0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(5, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(6, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(7, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(8, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(9, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(10, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(11, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(12, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(13, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(14, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.course_display.setVerticalHeaderItem(15, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.course_display.setItem(0, 0, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.course_display.setItem(0, 1, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.course_display.setItem(0, 2, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.course_display.setItem(0, 3, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.course_display.setItem(0, 4, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.course_display.setItem(0, 5, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.course_display.setItem(0, 6, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.course_display.setItem(0, 7, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.course_display.setItem(0, 8, __qtablewidgetitem72)
        self.course_display.setObjectName(u"course_display")
        sizePolicy3.setHeightForWidth(self.course_display.sizePolicy().hasHeightForWidth())
        self.course_display.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush8)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.course_display.setPalette(palette2)
        self.course_display.setFrameShape(QFrame.NoFrame)
        self.course_display.setLineWidth(1)
        self.course_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.course_display.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.course_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.course_display.setSelectionMode(QAbstractItemView.SingleSelection)
        self.course_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.course_display.setShowGrid(True)
        self.course_display.setGridStyle(Qt.SolidLine)
        self.course_display.setSortingEnabled(False)
        self.course_display.horizontalHeader().setVisible(False)
        self.course_display.horizontalHeader().setCascadingSectionResizes(True)
        self.course_display.horizontalHeader().setDefaultSectionSize(90)
        self.course_display.horizontalHeader().setStretchLastSection(True)
        self.course_display.verticalHeader().setVisible(False)
        self.course_display.verticalHeader().setCascadingSectionResizes(False)
        self.course_display.verticalHeader().setMinimumSectionSize(5)
        self.course_display.verticalHeader().setHighlightSections(False)
        self.course_display.verticalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.course_display, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.check_page)
        self.pwd_change_page = QWidget()
        self.pwd_change_page.setObjectName(u"pwd_change_page")
        self.horizontalLayout_6 = QHBoxLayout(self.pwd_change_page)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_2 = QFrame(self.pwd_change_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pwd_current = QLineEdit(self.frame_2)
        self.pwd_current.setObjectName(u"pwd_current")
        self.pwd_current.setMinimumSize(QSize(0, 30))
        self.pwd_current.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.pwd_current, 0, 0, 1, 1)

        self.pwd_new = QLineEdit(self.frame_2)
        self.pwd_new.setObjectName(u"pwd_new")
        self.pwd_new.setMinimumSize(QSize(0, 30))
        self.pwd_new.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.pwd_new, 1, 0, 1, 1)

        self.pwd_new_check = QLineEdit(self.frame_2)
        self.pwd_new_check.setObjectName(u"pwd_new_check")
        self.pwd_new_check.setMinimumSize(QSize(0, 30))
        self.pwd_new_check.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_5.addWidget(self.pwd_new_check, 2, 0, 1, 1)

        self.btn_pwd_change_confirm = QPushButton(self.frame_2)
        self.btn_pwd_change_confirm.setObjectName(u"btn_pwd_change_confirm")
        self.btn_pwd_change_confirm.setMinimumSize(QSize(150, 30))
        self.btn_pwd_change_confirm.setFont(font)
        self.btn_pwd_change_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pwd_change_confirm.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.btn_pwd_change_confirm.setIcon(icon4)

        self.gridLayout_5.addWidget(self.btn_pwd_change_confirm, 3, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.pwd_change_page)
        self.choose_course_page = QWidget()
        self.choose_course_page.setObjectName(u"choose_course_page")
        self.gridLayout_7 = QGridLayout(self.choose_course_page)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.course_id = QLineEdit(self.choose_course_page)
        self.course_id.setObjectName(u"course_id")
        self.course_id.setMinimumSize(QSize(0, 30))
        self.course_id.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_7.addWidget(self.course_id, 0, 0, 1, 1)

        self.confirm_btn = QPushButton(self.choose_course_page)
        self.confirm_btn.setObjectName(u"confirm_btn")
        self.confirm_btn.setMinimumSize(QSize(150, 30))
        self.confirm_btn.setFont(font)
        self.confirm_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirm_btn.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-check-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.confirm_btn.setIcon(icon13)

        self.gridLayout_7.addWidget(self.confirm_btn, 0, 1, 1, 1)

        self.choose_check_btn = QCheckBox(self.choose_course_page)
        self.choose_check_btn.setObjectName(u"choose_check_btn")
        self.choose_check_btn.setAutoFillBackground(False)
        self.choose_check_btn.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.choose_check_btn, 1, 1, 1, 1)

        self.quit_check_btn = QCheckBox(self.choose_course_page)
        self.quit_check_btn.setObjectName(u"quit_check_btn")
        self.quit_check_btn.setAutoFillBackground(False)
        self.quit_check_btn.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.quit_check_btn, 2, 1, 1, 1)

        self.course_all_display = QTableWidget(self.choose_course_page)
        if (self.course_all_display.columnCount() < 9):
            self.course_all_display.setColumnCount(9)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(4, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(5, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(6, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(7, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.course_all_display.setHorizontalHeaderItem(8, __qtablewidgetitem81)
        if (self.course_all_display.rowCount() < 16):
            self.course_all_display.setRowCount(16)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setFont(font4);
        self.course_all_display.setVerticalHeaderItem(0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(2, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(3, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(4, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(5, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(6, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(7, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(8, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(9, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(10, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(11, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(12, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(13, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(14, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.course_all_display.setVerticalHeaderItem(15, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.course_all_display.setItem(0, 0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.course_all_display.setItem(0, 1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.course_all_display.setItem(0, 2, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.course_all_display.setItem(0, 3, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.course_all_display.setItem(0, 4, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.course_all_display.setItem(0, 5, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.course_all_display.setItem(0, 6, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.course_all_display.setItem(0, 7, __qtablewidgetitem105)
        self.course_all_display.setObjectName(u"course_all_display")
        sizePolicy3.setHeightForWidth(self.course_all_display.sizePolicy().hasHeightForWidth())
        self.course_all_display.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush11 = QBrush(QColor(0, 0, 0, 255))
        brush11.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 255))
        brush12.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.course_all_display.setPalette(palette3)
        self.course_all_display.setFrameShape(QFrame.NoFrame)
        self.course_all_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.course_all_display.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.course_all_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.course_all_display.setSelectionMode(QAbstractItemView.SingleSelection)
        self.course_all_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.course_all_display.setShowGrid(True)
        self.course_all_display.setGridStyle(Qt.SolidLine)
        self.course_all_display.setSortingEnabled(False)
        self.course_all_display.horizontalHeader().setVisible(False)
        self.course_all_display.horizontalHeader().setCascadingSectionResizes(True)
        self.course_all_display.horizontalHeader().setDefaultSectionSize(90)
        self.course_all_display.horizontalHeader().setStretchLastSection(True)
        self.course_all_display.verticalHeader().setVisible(False)
        self.course_all_display.verticalHeader().setCascadingSectionResizes(False)
        self.course_all_display.verticalHeader().setHighlightSections(False)
        self.course_all_display.verticalHeader().setStretchLastSection(True)

        self.gridLayout_7.addWidget(self.course_all_display, 3, 0, 1, 2)

        self.stackedWidget.addWidget(self.choose_course_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setBold(False)
        font5.setItalic(False)
        self.creditsLabel.setFont(font5)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.select_info.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_widgets.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Conver"
                        "t QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Course-Choose-System", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.welcome.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">\u6b22\u8fce\u4f7f\u7528 \u8bf7\u5148\u767b\u5f55</span></p></body></html>", None))
        self.btn_pwd_change.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.btn_course_check.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8bfe\u7a0b", None))
        self.btn_course_choose.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5165\u9009\u8bfe", None))
        self.btn_info_change.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4fe1\u606f", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.welcome_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">\u6b22\u8fce\u4f7f\u7528 \u8bf7\u5148\u767b\u5f55</span></p></body></html>", None))
        self.btn_pwd_change_2.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.btn_grade_change.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5165\u6210\u7ee9", None))
        self.btn_course_check_2.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u8bfe\u7a0b", None))
        self.btn_info_change_2.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u4fe1\u606f", None))
        self.btn_info_change_confirm_3.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4\u4fee\u6539", None))
        self.welcome_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u8bf7\u9009\u62e9\u9700\u8981\u66f4\u6539\u7684\u4fe1\u606f</p></body></html>", None))
        self.changed_info.setText("")
        self.changed_info.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u4fee\u6539\u7684\u4fe1\u606f", None))
        ___qtablewidgetitem24 = self.student_info.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem25 = self.student_info.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.student_info.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.student_info.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem28 = self.student_info.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem29 = self.student_info.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem30 = self.student_info.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.student_info.verticalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem32 = self.student_info.verticalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.student_info.isSortingEnabled()
        self.student_info.setSortingEnabled(False)
        ___qtablewidgetitem33 = self.student_info.item(0, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u53f7", None));
        ___qtablewidgetitem34 = self.student_info.item(0, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u4e1a", None));
        ___qtablewidgetitem35 = self.student_info.item(0, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem36 = self.student_info.item(0, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u9662", None));
        ___qtablewidgetitem37 = self.student_info.item(0, 4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None));
        ___qtablewidgetitem38 = self.student_info.item(0, 5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u51fa\u751f\u65e5\u671f", None));
        self.student_info.setSortingEnabled(__sortingEnabled1)

        self.select_info.setItemText(0, QCoreApplication.translate("MainWindow", u"major", None))
        self.select_info.setItemText(1, QCoreApplication.translate("MainWindow", u"dept", None))
        self.select_info.setItemText(2, QCoreApplication.translate("MainWindow", u"birthday", None))
        self.select_info.setItemText(3, QCoreApplication.translate("MainWindow", u"gender", None))

        self.select_info.setCurrentText(QCoreApplication.translate("MainWindow", u"major", None))
        self.welcome_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700; font-style:italic;\">\u6b22\u8fce\u4f7f\u7528 \u8bf7\u5148\u767b\u5f55</span></p></body></html>", None))
        self.btn_pwd_change_student.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5b66\u751f\u5bc6\u7801", None))
        self.btn_pwd_change_teacher.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u6559\u5e08\u5bc6\u7801", None))
        self.btn_remove_course.setText(QCoreApplication.translate("MainWindow", u"\u5f52\u6863\u8bfe\u7a0b", None))
        self.btn_course_info_edit.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8bfe\u7a0b\u4fe1\u606f", None))
        self.btn_pwd_change_agent.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u7ba1\u7406\u5458\u5bc6\u7801", None))
        self.btn_add_course.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u8bfe\u7a0b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u767b\u5f55-\u9009\u8bfe\u7cfb\u7edf</span></p></body></html>", None))
        self.id.setText("")
        self.id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165ID", None))
        self.pwd.setText("")
        self.pwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.btn_student_login.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u7aef", None))
        self.btn_teacher_login.setText(QCoreApplication.translate("MainWindow", u"\u6559\u5e08\u7aef", None))
        self.btn_agent_login.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u7406\u5458", None))
        ___qtablewidgetitem39 = self.course_display.horizontalHeaderItem(0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u5b66\u53f7", None));
        ___qtablewidgetitem40 = self.course_display.horizontalHeaderItem(1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u59d3\u540d", None));
        ___qtablewidgetitem41 = self.course_display.horizontalHeaderItem(2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u540d\u79f0", None));
        ___qtablewidgetitem42 = self.course_display.horizontalHeaderItem(3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0bID", None));
        ___qtablewidgetitem43 = self.course_display.horizontalHeaderItem(4)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u4ecb\u7ecd", None));
        ___qtablewidgetitem44 = self.course_display.horizontalHeaderItem(5)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u5b66\u5206", None));
        ___qtablewidgetitem45 = self.course_display.horizontalHeaderItem(6)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u65f6\u95f4", None));
        ___qtablewidgetitem46 = self.course_display.horizontalHeaderItem(7)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"\u6388\u8bfe\u6559\u5e08", None));
        ___qtablewidgetitem47 = self.course_display.horizontalHeaderItem(8)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7\u53f7", None));
        ___qtablewidgetitem48 = self.course_display.verticalHeaderItem(0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem49 = self.course_display.verticalHeaderItem(1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem50 = self.course_display.verticalHeaderItem(2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem51 = self.course_display.verticalHeaderItem(3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem52 = self.course_display.verticalHeaderItem(4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem53 = self.course_display.verticalHeaderItem(5)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem54 = self.course_display.verticalHeaderItem(6)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem55 = self.course_display.verticalHeaderItem(7)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem56 = self.course_display.verticalHeaderItem(8)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem57 = self.course_display.verticalHeaderItem(9)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem58 = self.course_display.verticalHeaderItem(10)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem59 = self.course_display.verticalHeaderItem(11)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem60 = self.course_display.verticalHeaderItem(12)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem61 = self.course_display.verticalHeaderItem(13)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem62 = self.course_display.verticalHeaderItem(14)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem63 = self.course_display.verticalHeaderItem(15)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.course_display.isSortingEnabled()
        self.course_display.setSortingEnabled(False)
        ___qtablewidgetitem64 = self.course_display.item(0, 0)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u5b66\u53f7", None));
        ___qtablewidgetitem65 = self.course_display.item(0, 1)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u59d3\u540d", None));
        ___qtablewidgetitem66 = self.course_display.item(0, 2)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u540d\u79f0", None));
        ___qtablewidgetitem67 = self.course_display.item(0, 3)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0bID", None));
        ___qtablewidgetitem68 = self.course_display.item(0, 4)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u4ecb\u7ecd", None));
        ___qtablewidgetitem69 = self.course_display.item(0, 5)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u5b66\u5206", None));
        ___qtablewidgetitem70 = self.course_display.item(0, 6)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u65f6\u95f4", None));
        ___qtablewidgetitem71 = self.course_display.item(0, 7)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"\u6388\u8bfe\u6559\u5e08", None));
        ___qtablewidgetitem72 = self.course_display.item(0, 8)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7\u53f7", None));
        self.course_display.setSortingEnabled(__sortingEnabled2)

        self.pwd_current.setText("")
        self.pwd_current.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u539f\u5bc6\u7801", None))
        self.pwd_new.setText("")
        self.pwd_new.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u65b0\u5bc6\u7801", None))
        self.pwd_new_check.setText("")
        self.pwd_new_check.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u786e\u8ba4\u65b0\u5bc6\u7801", None))
        self.btn_pwd_change_confirm.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u5bc6\u7801", None))
        self.course_id.setText("")
        self.course_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u64cd\u4f5c\u8bfe\u7a0b\u5e8f\u53f7", None))
        self.confirm_btn.setText(QCoreApplication.translate("MainWindow", u"\u786e\u5b9a\u4fee\u6539", None))
        self.choose_check_btn.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u8bfe\u7a0b", None))
        self.quit_check_btn.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u8bfe\u7a0b", None))
        ___qtablewidgetitem73 = self.course_all_display.horizontalHeaderItem(0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem74 = self.course_all_display.horizontalHeaderItem(1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem75 = self.course_all_display.horizontalHeaderItem(2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem76 = self.course_all_display.horizontalHeaderItem(3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem77 = self.course_all_display.horizontalHeaderItem(4)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem78 = self.course_all_display.horizontalHeaderItem(5)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem79 = self.course_all_display.horizontalHeaderItem(6)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem80 = self.course_all_display.horizontalHeaderItem(7)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5217", None));
        ___qtablewidgetitem81 = self.course_all_display.horizontalHeaderItem(8)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem82 = self.course_all_display.verticalHeaderItem(0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem83 = self.course_all_display.verticalHeaderItem(1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem84 = self.course_all_display.verticalHeaderItem(2)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem85 = self.course_all_display.verticalHeaderItem(3)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem86 = self.course_all_display.verticalHeaderItem(4)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem87 = self.course_all_display.verticalHeaderItem(5)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem88 = self.course_all_display.verticalHeaderItem(6)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem89 = self.course_all_display.verticalHeaderItem(7)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem90 = self.course_all_display.verticalHeaderItem(8)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem91 = self.course_all_display.verticalHeaderItem(9)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem92 = self.course_all_display.verticalHeaderItem(10)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem93 = self.course_all_display.verticalHeaderItem(11)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem94 = self.course_all_display.verticalHeaderItem(12)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem95 = self.course_all_display.verticalHeaderItem(13)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem96 = self.course_all_display.verticalHeaderItem(14)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem97 = self.course_all_display.verticalHeaderItem(15)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled3 = self.course_all_display.isSortingEnabled()
        self.course_all_display.setSortingEnabled(False)
        ___qtablewidgetitem98 = self.course_all_display.item(0, 0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u7f16\u53f7", None));
        ___qtablewidgetitem99 = self.course_all_display.item(0, 1)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u540d\u79f0", None));
        ___qtablewidgetitem100 = self.course_all_display.item(0, 2)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u4ecb\u7ecd", None));
        ___qtablewidgetitem101 = self.course_all_display.item(0, 3)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u5b66\u65f6", None));
        ___qtablewidgetitem102 = self.course_all_display.item(0, 4)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u5b66\u5206", None));
        ___qtablewidgetitem103 = self.course_all_display.item(0, 5)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"\u8bfe\u7a0b\u65f6\u95f4", None));
        ___qtablewidgetitem104 = self.course_all_display.item(0, 6)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u8bfe\u6559\u5e08", None));
        ___qtablewidgetitem105 = self.course_all_display.item(0, 7)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"\u73ed\u7ea7\u53f7", None));
        self.course_all_display.setSortingEnabled(__sortingEnabled3)

        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By WinchesterDaw", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

