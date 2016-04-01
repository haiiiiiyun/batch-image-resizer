# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/KP/batch-image-resizer/messagewidget.ui'
#
# Created: Sat Mar 31 16:35:07 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_messageDialog(object):
    def setupUi(self, messageDialog):
        messageDialog.setObjectName(_fromUtf8("messageDialog"))
        messageDialog.resize(226, 95)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        messageDialog.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(messageDialog)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mainFrame = QtGui.QFrame(messageDialog)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.mainFrame.setFont(font)
        self.mainFrame.setStyleSheet(_fromUtf8("#mainFrame{\n"
"    /*background-color: rgb(214, 214, 214);\n"
"    border-image: url(:/images/metal-background.jpg);*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(226, 230, 231, 255), stop:1 rgba(196, 201, 204, 255));\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"#buttonsFrame{\n"
"    margin-bottom: 2px;\n"
"    border: none;\n"
"    padding: 0px;\n"
"    border-image: url(:/images/top-line-bg.png) repeat top;\n"
"}"))
        self.mainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.mainFrame.setLineWidth(5)
        self.mainFrame.setObjectName(_fromUtf8("mainFrame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.messageLabel = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageLabel.sizePolicy().hasHeightForWidth())
        self.messageLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setOpenExternalLinks(True)
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.verticalLayout.addWidget(self.messageLabel)
        self.buttonsFrame = QtGui.QFrame(self.mainFrame)
        self.buttonsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonsFrame.setObjectName(_fromUtf8("buttonsFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(52, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.buttonsFrame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtGui.QSpacerItem(51, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.buttonsFrame)
        self.gridLayout_2.addWidget(self.mainFrame, 0, 0, 1, 1)

        self.retranslateUi(messageDialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), messageDialog.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), messageDialog.close)
        QtCore.QMetaObject.connectSlotsByName(messageDialog)

    def retranslateUi(self, messageDialog):
        messageDialog.setWindowTitle(QtGui.QApplication.translate("messageDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.messageLabel.setText(QtGui.QApplication.translate("messageDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\"><center>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">message here.</p><p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">message here.</p></center></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("messageDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

import prog_rc
