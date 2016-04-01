# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/KP/batch-image-resizer/wronglicensewidget.ui'
#
# Created: Sat Mar 31 16:29:55 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_wrongLicenseDialog(object):
    def setupUi(self, wrongLicenseDialog):
        wrongLicenseDialog.setObjectName(_fromUtf8("wrongLicenseDialog"))
        wrongLicenseDialog.resize(374, 112)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        wrongLicenseDialog.setFont(font)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(wrongLicenseDialog)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.mainFrame = QtGui.QFrame(wrongLicenseDialog)
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
        self.label = QtGui.QLabel(self.mainFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonsFrame = QtGui.QFrame(self.mainFrame)
        self.buttonsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonsFrame.setObjectName(_fromUtf8("buttonsFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(106, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.yesButton = QtGui.QPushButton(self.buttonsFrame)
        self.yesButton.setDefault(True)
        self.yesButton.setObjectName(_fromUtf8("yesButton"))
        self.horizontalLayout.addWidget(self.yesButton)
        self.noButton = QtGui.QPushButton(self.buttonsFrame)
        self.noButton.setObjectName(_fromUtf8("noButton"))
        self.horizontalLayout.addWidget(self.noButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.buttonsFrame)
        self.horizontalLayout_2.addWidget(self.mainFrame)

        self.retranslateUi(wrongLicenseDialog)
        QtCore.QObject.connect(self.yesButton, QtCore.SIGNAL(_fromUtf8("clicked()")), wrongLicenseDialog.accept)
        QtCore.QObject.connect(self.noButton, QtCore.SIGNAL(_fromUtf8("clicked()")), wrongLicenseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(wrongLicenseDialog)
        wrongLicenseDialog.setTabOrder(self.yesButton, self.noButton)

    def retranslateUi(self, wrongLicenseDialog):
        wrongLicenseDialog.setWindowTitle(QtGui.QApplication.translate("wrongLicenseDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("wrongLicenseDialog", "Sorry, you have entered an invalid  license key.\n"
"Would you like to try again?", None, QtGui.QApplication.UnicodeUTF8))
        self.yesButton.setText(QtGui.QApplication.translate("wrongLicenseDialog", "Yes", None, QtGui.QApplication.UnicodeUTF8))
        self.noButton.setText(QtGui.QApplication.translate("wrongLicenseDialog", "Later", None, QtGui.QApplication.UnicodeUTF8))

import prog_rc
