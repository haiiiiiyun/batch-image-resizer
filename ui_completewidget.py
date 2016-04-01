# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/workspace/batch-image-resizer/completewidget.ui'
#
# Created: Wed Feb 12 11:34:04 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_completeDialog(object):
    def setupUi(self, completeDialog):
        completeDialog.setObjectName(_fromUtf8("completeDialog"))
        completeDialog.resize(525, 183)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        completeDialog.setFont(font)
        self.gridLayout_2 = QtGui.QGridLayout(completeDialog)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mainFrame = QtGui.QFrame(completeDialog)
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
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.completeLabel = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.completeLabel.sizePolicy().hasHeightForWidth())
        self.completeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.completeLabel.setFont(font)
        self.completeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.completeLabel.setOpenExternalLinks(True)
        self.completeLabel.setObjectName(_fromUtf8("completeLabel"))
        self.verticalLayout.addWidget(self.completeLabel)
        self.demoAlertLabel = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.demoAlertLabel.sizePolicy().hasHeightForWidth())
        self.demoAlertLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.demoAlertLabel.setFont(font)
        self.demoAlertLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.demoAlertLabel.setOpenExternalLinks(True)
        self.demoAlertLabel.setObjectName(_fromUtf8("demoAlertLabel"))
        self.verticalLayout.addWidget(self.demoAlertLabel)
        self.buttonsFrame = QtGui.QFrame(self.mainFrame)
        self.buttonsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonsFrame.setObjectName(_fromUtf8("buttonsFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(52, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.buttonsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.licenseButton = QtGui.QPushButton(self.buttonsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.licenseButton.sizePolicy().hasHeightForWidth())
        self.licenseButton.setSizePolicy(sizePolicy)
        self.licenseButton.setObjectName(_fromUtf8("licenseButton"))
        self.horizontalLayout.addWidget(self.licenseButton)
        self.buyButton = QtGui.QPushButton(self.buttonsFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buyButton.sizePolicy().hasHeightForWidth())
        self.buyButton.setSizePolicy(sizePolicy)
        self.buyButton.setObjectName(_fromUtf8("buyButton"))
        self.horizontalLayout.addWidget(self.buyButton)
        spacerItem1 = QtGui.QSpacerItem(51, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.buttonsFrame)
        self.gridLayout_2.addWidget(self.mainFrame, 0, 0, 1, 1)

        self.retranslateUi(completeDialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), completeDialog.close)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), completeDialog.close)
        QtCore.QMetaObject.connectSlotsByName(completeDialog)

    def retranslateUi(self, completeDialog):
        completeDialog.setWindowTitle(QtGui.QApplication.translate("completeDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.completeLabel.setText(QtGui.QApplication.translate("completeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:14pt;\"><span style=\" font-size:18pt; font-weight:600;\">Your extraction is complete!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.demoAlertLabel.setText(QtGui.QApplication.translate("completeDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<hr />\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The evaluation version of Hibosoft Batch Image Resizer only can resize max 3 files. </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To run unlimited resizing, enter a valid license key, which you may order</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> from our web store by clicking the order button below.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("completeDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.licenseButton.setText(QtGui.QApplication.translate("completeDialog", "Enter license ...", None, QtGui.QApplication.UnicodeUTF8))
        self.buyButton.setText(QtGui.QApplication.translate("completeDialog", "Order online now...", None, QtGui.QApplication.UnicodeUTF8))

import prog_rc
