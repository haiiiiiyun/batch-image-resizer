# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/browserwidget.ui'
#
# Created: Tue Aug 02 16:10:56 2011
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_browserDialog(object):
    def setupUi(self, browserDialog):
        browserDialog.setObjectName("browserDialog")
        browserDialog.resize(836,614)
        self.verticalLayout = QtGui.QVBoxLayout(browserDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtGui.QPushButton(browserDialog)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.forwardButton = QtGui.QPushButton(browserDialog)
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout.addWidget(self.forwardButton)
        self.stopButton = QtGui.QPushButton(browserDialog)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout.addWidget(self.stopButton)
        self.urlEdit = QtGui.QLineEdit(browserDialog)
        self.urlEdit.setObjectName("urlEdit")
        self.horizontalLayout.addWidget(self.urlEdit)
        self.reloadButton = QtGui.QPushButton(browserDialog)
        self.reloadButton.setObjectName("reloadButton")
        self.horizontalLayout.addWidget(self.reloadButton)
        self.purchaseButton = QtGui.QPushButton(browserDialog)
        self.purchaseButton.setObjectName("purchaseButton")
        self.horizontalLayout.addWidget(self.purchaseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.webView = QtWebKit.QWebView(browserDialog)
        self.webView.setUrl(QtCore.QUrl("http://www.google.com.hk/"))
        self.webView.setObjectName("webView")
        self.verticalLayout.addWidget(self.webView)

        self.retranslateUi(browserDialog)
        QtCore.QObject.connect(self.webView,QtCore.SIGNAL("linkClicked(QUrl)"),browserDialog.update)
        QtCore.QMetaObject.connectSlotsByName(browserDialog)

    def retranslateUi(self, browserDialog):
        browserDialog.setWindowTitle(QtGui.QApplication.translate("browserDialog", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("browserDialog", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.forwardButton.setText(QtGui.QApplication.translate("browserDialog", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("browserDialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setText(QtGui.QApplication.translate("browserDialog", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.purchaseButton.setText(QtGui.QApplication.translate("browserDialog", "Purchase Now!", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
