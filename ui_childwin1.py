# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'childwin1.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)
import tupian

class Ui_dialog1(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(795, 569)
        dialog.setAcceptDrops(False)
        self.comboBox = QComboBox(dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(190, 40, 111, 22))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 40, 131, 16))
        self.zaiti = QPushButton(dialog)
        self.zaiti.setObjectName(u"zaiti")
        self.zaiti.setGeometry(QRect(100, 130, 111, 24))
        self.shuiyin = QPushButton(dialog)
        self.shuiyin.setObjectName(u"shuiyin")
        self.shuiyin.setGeometry(QRect(100, 170, 111, 24))
        self.setwater = QPushButton(dialog)
        self.setwater.setObjectName(u"setwater")
        self.setwater.setGeometry(QRect(100, 210, 111, 24))
        self.get = QPushButton(dialog)
        self.get.setObjectName(u"get")
        self.get.setGeometry(QRect(100, 360, 121, 24))
        self.getwater = QPushButton(dialog)
        self.getwater.setObjectName(u"getwater")
        self.getwater.setGeometry(QRect(120, 400, 75, 24))
        self.MPN = QPushButton(dialog)
        self.MPN.setObjectName(u"MPN")
        self.MPN.setGeometry(QRect(570, 440, 91, 24))
        self.show1 = QLabel(dialog)
        self.show1.setObjectName(u"show1")
        self.show1.setGeometry(QRect(260, 80, 421, 181))
        self.show1.setPixmap(QPixmap(u":/1/akl.jpg"))
        self.show1.setScaledContents(True)
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 270, 101, 16))
        self.show2 = QLabel(dialog)
        self.show2.setObjectName(u"show2")
        self.show2.setGeometry(QRect(260, 290, 201, 151))
        self.show2.setPixmap(QPixmap(u":/1/akl.jpg"))
        self.show2.setScaledContents(True)
        self.label_5 = QLabel(dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 450, 101, 16))
        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(560, 350, 54, 16))
        self.label_4 = QLabel(dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, 380, 54, 16))
        self.label_6 = QLabel(dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(560, 410, 54, 16))
        self.MSE = QLabel(dialog)
        self.MSE.setObjectName(u"MSE")
        self.MSE.setGeometry(QRect(620, 350, 54, 16))
        self.PSNR = QLabel(dialog)
        self.PSNR.setObjectName(u"PSNR")
        self.PSNR.setGeometry(QRect(620, 380, 54, 16))
        self.NC = QLabel(dialog)
        self.NC.setObjectName(u"NC")
        self.NC.setGeometry(QRect(620, 410, 54, 16))

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u56fe\u7247\u6570\u5b57\u6c34\u5370", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("dialog", u"LSB\u5d4c\u5165", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("dialog", u"DWT\u666e\u901a\u5d4c\u5165", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("dialog", u"DWT\u5168\u606f\u5d4c\u5165", None))

#if QT_CONFIG(accessibility)
        self.comboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.comboBox.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("dialog", u"\u9009\u62e9\u5d4c\u5165\u6c34\u5370\u7684\u65b9\u5f0f\uff1a", None))
        self.zaiti.setText(QCoreApplication.translate("dialog", u"\u9009\u62e9\u8f7d\u4f53\u56fe\u7247", None))
        self.shuiyin.setText(QCoreApplication.translate("dialog", u"\u9009\u62e9\u6c34\u5370\u56fe\u7247", None))
        self.setwater.setText(QCoreApplication.translate("dialog", u"\u5d4c\u5165\u6c34\u5370", None))
        self.get.setText(QCoreApplication.translate("dialog", u"\u9009\u62e9\u5f85\u63d0\u53d6\u7684\u56fe\u7247", None))
        self.getwater.setText(QCoreApplication.translate("dialog", u"\u63d0\u53d6\u6c34\u5370", None))
        self.MPN.setText(QCoreApplication.translate("dialog", u"\u67e5\u770b\u5d4c\u5165\u53c2\u6570", None))
        self.show1.setText("")
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u5d4c\u5165\u6c34\u5370\u540e\u7684\u56fe\u7247", None))
        self.show2.setText("")
        self.label_5.setText(QCoreApplication.translate("dialog", u"\u63d0\u53d6\u51fa\u7684\u6c34\u5370\u56fe\u7247", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"MSE:", None))
        self.label_4.setText(QCoreApplication.translate("dialog", u"PSNR:", None))
        self.label_6.setText(QCoreApplication.translate("dialog", u"NC:", None))
        self.MSE.setText("")
        self.PSNR.setText("")
        self.NC.setText("")
    # retranslateUi

