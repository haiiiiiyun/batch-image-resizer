# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/workspace/batch-image-resizer/processingwidget.ui'
#
# Created: Thu Apr 05 16:25:07 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_processingDialog(object):
    def setupUi(self, processingDialog):
        processingDialog.setObjectName(_fromUtf8("processingDialog"))
        processingDialog.resize(349, 110)
        self.gridLayout_2 = QtGui.QGridLayout(processingDialog)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 0, 2, 2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mainFrame = QtGui.QFrame(processingDialog)
        self.mainFrame.setStyleSheet(_fromUtf8("#mainFrame{\n"
"    /*background-color: rgb(214, 214, 214);\n"
"    border-image: url(:/images/metal-background.jpg);*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(226, 230, 231, 255), stop:1 rgba(196, 201, 204, 255));\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"    font-family:Arial,Helvetica,sans-serif;\n"
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
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setMargin(5)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.messageLabel = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageLabel.sizePolicy().hasHeightForWidth())
        self.messageLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setOpenExternalLinks(True)
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.verticalLayout.addWidget(self.messageLabel)
        self.progressBar = QtGui.QProgressBar(self.mainFrame)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.buttonsFrame = QtGui.QFrame(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.buttonsFrame.setFont(font)
        self.buttonsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonsFrame.setObjectName(_fromUtf8("buttonsFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(119, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(self.buttonsFrame)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem1 = QtGui.QSpacerItem(119, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.buttonsFrame)
        self.gridLayout_2.addWidget(self.mainFrame, 0, 0, 1, 1)

        self.retranslateUi(processingDialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), processingDialog.close)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), processingDialog.close)
        QtCore.QMetaObject.connectSlotsByName(processingDialog)

    def retranslateUi(self, processingDialog):
        processingDialog.setWindowTitle(QtGui.QApplication.translate("processingDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.messageLabel.setText(QtGui.QApplication.translate("processingDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Processing filename.jpg</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar.setFormat(QtGui.QApplication.translate("processingDialog", "%p% complete", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("processingDialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))

import prog_rc
