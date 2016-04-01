# -*- coding: utf-8 -*-

import os
import config
import common

from PyQt4 import QtCore, QtGui

from dialogs import *
from promptwidget import PromptWidget

class MyTreeWidget(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        QtGui.QTreeWidget.__init__(self, parent)
        self.linePerPage = 2
        self.lineHeight = 0
        self.pageWidth = 1
        self.data = []

        self.dragText = None

        self.PROMPT_HEIGHT = 120
        self.PROMPT_WIDTH = 364
        self.promptWidget = PromptWidget(self)
        self.promptWidget.setFixedHeight(self.PROMPT_HEIGHT)
        self.promptWidget.setFixedWidth(self.PROMPT_WIDTH)
        self.connect(self.promptWidget, QtCore.SIGNAL("clicked()"), self._emitClicked)


    def resizeEvent(self, event):
        self.size = event.size()
        font = self.fontMetrics()
        linePerPage = self.size.height()/font.lineSpacing()
        #linePerPage = (self.size.height()-125)/font.lineSpacing()
        pageWidth = event.oldSize().width()
        self.pageWidth = event.size().width()
        self.lineHeight = font.lineSpacing()
        if (linePerPage-1 != self.linePerPage) or ( pageWidth!=self.pageWidth):
            self.linePerPage = linePerPage-1
            self.updateValue(self.data)
            self.pageWidth = pageWidth


    def dragEnterEvent(self, event):
        i = self.itemAt(event.pos())
        if not i or (not i.data(0, QtCore.Qt.ToolTipRole).toString()):
            self.dragText = None
            event.ignore()
        else:
            i = self.itemAt(event.pos())
            self.dragText = unicode(i.data(0, QtCore.Qt.ToolTipRole).toString())
            event.accept()

    def dropEvent(self, event):
        i = self.itemAt(event.pos())
        if not i or (not self.dragText):
            self.dragText = None
            event.ignore()
        else:
            dropText = unicode(i.data(0, QtCore.Qt.ToolTipRole).toString())
            event.accept()

            if self.dragText and dropText:
                try:
                    i1 = self.data.index(self.dragText)
                    i2 = self.data.index(dropText)
                    self.data[i1], self.data[i2] = self.data[i2], self.data[i1]
                    self.updateValue(self.data)
                except ValueError:
                    pass
                self.dragText = None
            elif self.dragText:
                try:
                    i1 = self.data.index(self.dragText)
                    v = self.data.pop(i1)
                    self.data.append(v)
                    self.updateValue(self.data)
                except ValueError:
                    pass
                self.dragText = None

    def centerPrompt(self, showPrompt=True):
        prompt_geometry = self.promptWidget.geometry()
        parent_geometry = self.geometry()
        y_inc = ((parent_geometry.height()-self.lineHeight)-prompt_geometry.height())/2
        if y_inc<0: y_inc = 0
        y = parent_geometry.y()+y_inc
        prompt_geometry.setY(self.lineHeight+y_inc)
        x_inc = (parent_geometry.width()-prompt_geometry.width())/2
        if x_inc<0: x_inc=0
        x = parent_geometry.x()+x_inc
        prompt_geometry.setX(x)
        self.promptWidget.setGeometry(prompt_geometry)
        self.promptWidget.setVisible(showPrompt)

    def updateValue(self, lst):
        if not lst:
            showPrompt = True
            self.clear()
            self.data = []
            self.emit(QtCore.SIGNAL("tablecleared()"))
            x=1
            font = self.fontMetrics()
            PROMPT_HEIGHT = 120
            promptLines = int(PROMPT_HEIGHT/font.lineSpacing())
            prompt_pos= (self.linePerPage-promptLines)/2 + 1
            while x<=self.linePerPage:
                if x==prompt_pos:
                    i = QtGui.QTreeWidgetItem([""])
                    i.setData(0, QtCore.Qt.ToolTipRole, QtCore.QVariant(""))
                    self.addTopLevelItem(i)
                else:
                    i = QtGui.QTreeWidgetItem([""])
                    i.setData(0, QtCore.Qt.ToolTipRole, QtCore.QVariant(""))
                    self.addTopLevelItem(i)
                x+=1
            self.centerPrompt(showPrompt)
        else:
            supportedList = []
            supported_types = config.supported_formats['image']
            for fullFilePath in lst:
                ext = os.path.splitext(os.path.basename(fullFilePath))[1].lower()
                if ext in supported_types:
                    if fullFilePath not in supportedList:
                        supportedList.append(fullFilePath)

            if self.data:
                self.centerPrompt(False)
                if supportedList:
                    for p in supportedList:
                        if p not in self.data:
                            self.data.append(p)
                else:
                    centerWidget = self.parentWidget().parentWidget().parentWidget().parentWidget()
                    dlg = MessageDialog(centerWidget)
                    dlg.setText(QtGui.QApplication.translate("mytreewidget", "Please drag JPEG, PNG, TIFF, BMP, GIF files/folders.", None, QtGui.QApplication.UnicodeUTF8))
                    common.show_dialog_on_top(dlg, centerWidget)
                    return
            else:
                if not supportedList:
                    centerWidget = self.parentWidget().parentWidget().parentWidget().parentWidget()
                    dlg = MessageDialog(centerWidget)
                    dlg.setText(QtGui.QApplication.translate("mytreewidget", "Please drag JPEG, PNG, TIFF, BMP, GIF files/folders.", None, QtGui.QApplication.UnicodeUTF8))
                    common.show_dialog_on_top(dlg, centerWidget)
                    self.centerPrompt(True)
                    return
                else:
                    self.data = supportedList
                    self.centerPrompt(False)

            self.clear()
            for itm in self.data:
                base_itm = os.path.basename(itm)
                i = QtGui.QTreeWidgetItem([base_itm])
                i.setData(0, QtCore.Qt.ToolTipRole, QtCore.QVariant(itm))
                #i.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled)
                self.addTopLevelItem(i)
            if len(lst)<self.linePerPage:
                for x in xrange(self.linePerPage-len(lst)-1):
                    i = QtGui.QTreeWidgetItem([""])
                    i.setData(0, QtCore.Qt.ToolTipRole, QtCore.QVariant(""))
                    #i.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled)
                    self.addTopLevelItem(i)

    def _emitClicked(self):
        self.emit(QtCore.SIGNAL("browserfiles()"))
