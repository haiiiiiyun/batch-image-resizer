# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:/workspace/batch-image-resizer/aboutwidget.ui'
#
# Created: Mon Feb 10 13:01:29 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName(_fromUtf8("aboutDialog"))
        aboutDialog.resize(277, 398)
        self.gridLayout_2 = QtGui.QGridLayout(aboutDialog)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 0, 2, 2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.mainFrame = QtGui.QFrame(aboutDialog)
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
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.imageLabel = QtGui.QLabel(self.mainFrame)
        self.imageLabel.setText(_fromUtf8(""))
        self.imageLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/images/logo.png")))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName(_fromUtf8("imageLabel"))
        self.verticalLayout.addWidget(self.imageLabel)
        self.versionLabel = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setBold(False)
        font.setWeight(50)
        self.versionLabel.setFont(font)
        self.versionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.versionLabel.setObjectName(_fromUtf8("versionLabel"))
        self.verticalLayout.addWidget(self.versionLabel)
        self.websiteLabel = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.websiteLabel.setFont(font)
        self.websiteLabel.setObjectName(_fromUtf8("websiteLabel"))
        self.verticalLayout.addWidget(self.websiteLabel)
        self.emailLabel = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.emailLabel.setFont(font)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.verticalLayout.addWidget(self.emailLabel)
        self.copyrightLabel = QtGui.QLabel(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.copyrightLabel.setFont(font)
        self.copyrightLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.copyrightLabel.setObjectName(_fromUtf8("copyrightLabel"))
        self.verticalLayout.addWidget(self.copyrightLabel)
        self.buttonsFrame = QtGui.QFrame(self.mainFrame)
        self.buttonsFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.buttonsFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.buttonsFrame.setObjectName(_fromUtf8("buttonsFrame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout.setContentsMargins(-1, 9, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(self.buttonsFrame)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        spacerItem1 = QtGui.QSpacerItem(71, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.buttonsFrame)
        self.gridLayout_2.addWidget(self.mainFrame, 0, 0, 1, 1)

        self.retranslateUi(aboutDialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), aboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        aboutDialog.setWindowTitle(QtGui.QApplication.translate("aboutDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("aboutDialog", "V3.1", None, QtGui.QApplication.UnicodeUTF8))
        self.websiteLabel.setText(QtGui.QApplication.translate("aboutDialog", "<html><head/><body><p align=\"center\"><a href=\"http://www.hibosoft.com\"><span style=\" font-size:11pt; text-decoration: underline; color:#0070BC;\">www.hibosoft.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.emailLabel.setText(QtGui.QApplication.translate("aboutDialog", "<html><head/><body><p align=\"center\"><a href=\"mailto:support@hibosoft.com\"><span style=\"text-decoration: underline; color:#409E3F;\">Email:support@hibosoft.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.copyrightLabel.setText(QtGui.QApplication.translate("aboutDialog", "© 2009-2014, Hibosoft Software", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("aboutDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

import prog_rc
