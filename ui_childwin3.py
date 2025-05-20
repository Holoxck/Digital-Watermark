# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'childwin3.ui'
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
    QProgressBar, QPushButton, QSizePolicy, QWidget)
import tupian

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(818, 475)
        self.play = QPushButton(dialog)
        self.play.setObjectName(u"play")
        self.play.setGeometry(QRect(350, 290, 41, 24))
        self.label = QLabel(dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 50, 131, 16))
        self.showvedio = QLabel(dialog)
        self.showvedio.setObjectName(u"showvedio")
        self.showvedio.setGeometry(QRect(350, 30, 421, 281))
        self.showvedio.setPixmap(QPixmap(u":/1/akl.jpg"))
        self.showvedio.setScaledContents(True)
        self.setwater = QPushButton(dialog)
        self.setwater.setObjectName(u"setwater")
        self.setwater.setGeometry(QRect(120, 220, 141, 24))
        self.label_3 = QLabel(dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(510, 10, 101, 16))
        self.shuiyin = QPushButton(dialog)
        self.shuiyin.setObjectName(u"shuiyin")
        self.shuiyin.setGeometry(QRect(120, 180, 141, 24))
        self.comboBox = QComboBox(dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(180, 50, 111, 22))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.shipin = QPushButton(dialog)
        self.shipin.setObjectName(u"shipin")
        self.shipin.setGeometry(QRect(120, 140, 141, 24))
        self.label_2 = QLabel(dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 350, 61, 16))
        self.progressBar = QProgressBar(dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(170, 350, 551, 23))
        self.progressBar.setValue(0)
        self.stop = QPushButton(dialog)
        self.stop.setObjectName(u"stop")
        self.stop.setGeometry(QRect(730, 290, 41, 24))
        self.showvedio.raise_()
        self.play.raise_()
        self.label.raise_()
        self.setwater.raise_()
        self.label_3.raise_()
        self.shuiyin.raise_()
        self.comboBox.raise_()
        self.shipin.raise_()
        self.label_2.raise_()
        self.progressBar.raise_()
        self.stop.raise_()

        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u89c6\u9891\u6570\u5b57\u6c34\u5370", None))
        self.play.setText(QCoreApplication.translate("dialog", u"\u5f00\u59cb", None))
        self.label.setText(QCoreApplication.translate("dialog", u"\u9009\u62e9\u5d4c\u5165\u6c34\u5370\u7684\u65b9\u5f0f\uff1a", None))
        self.showvedio.setText("")
        self.setwater.setText(QCoreApplication.translate("dialog", u"\u5d4c\u5165\u6c34\u5370", None))
        self.label_3.setText(QCoreApplication.translate("dialog", u"\u5d4c\u5165\u540e\u7684\u89c6\u9891\u5c55\u793a", None))
        self.shuiyin.setText(QCoreApplication.translate("dialog", u"\u9009\u62e9\u6c34\u5370\u56fe\u7247", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("dialog", u"LSB\u5d4c\u5165", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("dialog", u"DWT\u666e\u901a\u5d4c\u5165", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("dialog", u"DWT\u5168\u606f\u5d4c\u5165", None))

#if QT_CONFIG(accessibility)
        self.comboBox.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.comboBox.setPlaceholderText("")
        self.shipin.setText(QCoreApplication.translate("dialog", u"\u9009\u62e9\u8981\u5d4c\u5165\u6c34\u5370\u7684\u89c6\u9891", None))
        self.label_2.setText(QCoreApplication.translate("dialog", u"\u5b8c\u6210\u8fdb\u5ea6\uff1a", None))
        self.stop.setText(QCoreApplication.translate("dialog", u"\u6682\u505c", None))
    # retranslateUi

