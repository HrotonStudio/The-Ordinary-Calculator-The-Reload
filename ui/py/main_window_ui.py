# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet(u"")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_settings = QAction(MainWindow)
        self.action_settings.setObjectName(u"action_settings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButtonNum1 = QPushButton(self.centralwidget)
        self.pushButtonNum1.setObjectName(u"pushButtonNum1")
        self.pushButtonNum1.setGeometry(QRect(10, 370, 75, 75))
        self.pushButtonNum7 = QPushButton(self.centralwidget)
        self.pushButtonNum7.setObjectName(u"pushButtonNum7")
        self.pushButtonNum7.setGeometry(QRect(10, 190, 75, 75))
        self.pushButtonNum5 = QPushButton(self.centralwidget)
        self.pushButtonNum5.setObjectName(u"pushButtonNum5")
        self.pushButtonNum5.setGeometry(QRect(100, 280, 75, 75))
        self.pushButtonNum8 = QPushButton(self.centralwidget)
        self.pushButtonNum8.setObjectName(u"pushButtonNum8")
        self.pushButtonNum8.setGeometry(QRect(100, 190, 75, 75))
        self.pushButtonNum3 = QPushButton(self.centralwidget)
        self.pushButtonNum3.setObjectName(u"pushButtonNum3")
        self.pushButtonNum3.setGeometry(QRect(190, 370, 75, 75))
        self.pushButtonNum9 = QPushButton(self.centralwidget)
        self.pushButtonNum9.setObjectName(u"pushButtonNum9")
        self.pushButtonNum9.setGeometry(QRect(190, 190, 75, 75))
        self.pushButtonNum2 = QPushButton(self.centralwidget)
        self.pushButtonNum2.setObjectName(u"pushButtonNum2")
        self.pushButtonNum2.setGeometry(QRect(100, 370, 75, 75))
        self.pushButtonNum6 = QPushButton(self.centralwidget)
        self.pushButtonNum6.setObjectName(u"pushButtonNum6")
        self.pushButtonNum6.setGeometry(QRect(190, 280, 75, 75))
        self.pushButtonNum4 = QPushButton(self.centralwidget)
        self.pushButtonNum4.setObjectName(u"pushButtonNum4")
        self.pushButtonNum4.setGeometry(QRect(10, 280, 75, 75))
        self.pushButtonPoint = QPushButton(self.centralwidget)
        self.pushButtonPoint.setObjectName(u"pushButtonPoint")
        self.pushButtonPoint.setGeometry(QRect(10, 460, 75, 75))
        self.pushButtonNum0 = QPushButton(self.centralwidget)
        self.pushButtonNum0.setObjectName(u"pushButtonNum0")
        self.pushButtonNum0.setGeometry(QRect(100, 460, 75, 75))
        self.pushButtonEquals = QPushButton(self.centralwidget)
        self.pushButtonEquals.setObjectName(u"pushButtonEquals")
        self.pushButtonEquals.setGeometry(QRect(190, 460, 75, 75))
        self.pushButtonTruediv = QPushButton(self.centralwidget)
        self.pushButtonTruediv.setObjectName(u"pushButtonTruediv")
        self.pushButtonTruediv.setGeometry(QRect(280, 460, 75, 75))
        self.pushButtonMul = QPushButton(self.centralwidget)
        self.pushButtonMul.setObjectName(u"pushButtonMul")
        self.pushButtonMul.setGeometry(QRect(280, 370, 75, 75))
        self.pushButtonSub = QPushButton(self.centralwidget)
        self.pushButtonSub.setObjectName(u"pushButtonSub")
        self.pushButtonSub.setGeometry(QRect(280, 280, 75, 75))
        self.pushButtonAdd = QPushButton(self.centralwidget)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setGeometry(QRect(280, 190, 75, 75))
        self.pushButtonClear = QPushButton(self.centralwidget)
        self.pushButtonClear.setObjectName(u"pushButtonClear")
        self.pushButtonClear.setGeometry(QRect(370, 190, 75, 75))
        self.TextBrowserMainDisplayer = QTextBrowser(self.centralwidget)
        self.TextBrowserMainDisplayer.setObjectName(u"TextBrowserMainDisplayer")
        self.TextBrowserMainDisplayer.setGeometry(QRect(10, 0, 571, 191))
        font = QFont()
        font.setPointSize(20)
        font.setItalic(False)
        self.TextBrowserMainDisplayer.setFont(font)
        self.textBrowserTips = QTextBrowser(self.centralwidget)
        self.textBrowserTips.setObjectName(u"textBrowserTips")
        self.textBrowserTips.setGeometry(QRect(740, 0, 381, 91))
        self.pushButtonReloadTips = QPushButton(self.centralwidget)
        self.pushButtonReloadTips.setObjectName(u"pushButtonReloadTips")
        self.pushButtonReloadTips.setGeometry(QRect(670, 0, 64, 64))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"exit", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.action_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.pushButtonNum1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButtonNum7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButtonNum5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButtonNum8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButtonNum3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButtonNum9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButtonNum2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButtonNum6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButtonNum4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButtonPoint.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButtonNum0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButtonEquals.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.pushButtonTruediv.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.pushButtonMul.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButtonSub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButtonClear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.pushButtonReloadTips.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
    # retranslateUi

