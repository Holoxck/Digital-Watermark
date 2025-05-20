# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwin1.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.shipin = QPushButton(self.centralwidget)
        self.shipin.setObjectName(u"shipin")
        self.shipin.setGeometry(QRect(190, 220, 141, 81))
        self.tupian = QPushButton(self.centralwidget)
        self.tupian.setObjectName(u"tupian")
        self.tupian.setGeometry(QRect(430, 220, 141, 80))
        self.tupian.setAutoRepeatDelay(295)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u89c6\u9891\u6570\u5b57\u6c34\u5370", None))
        self.shipin.setText(QCoreApplication.translate("mainWindow", u"\u5d4c\u5165\u89c6\u9891\u6c34\u5370", None))
        self.tupian.setText(QCoreApplication.translate("mainWindow", u"\u6d4b\u8bd5\u56fe\u7247\u6c34\u5370", None))
    # retranslateUi

