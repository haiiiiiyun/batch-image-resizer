# -*- coding: utf-8 -*-

import os

from PyQt4 import QtCore, QtGui
import pickle

import config
import common
from dialogs import *
from ui_mainwidget import Ui_mainWidget
import prog_rc

class MainWidget(QtGui.QWidget, Ui_mainWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.infoLabel.setText(QtGui.QApplication.translate("mainwidget", "  Ctrl / Shift / Apple key for multi-selections", None, QtGui.QApplication.UnicodeUTF8))
        #self.logoLabel.setPixmap(QtGui.QPixmap(":/images/page1.png"))
        #self.helpButton.setIcon(QtGui.QIcon(":/images/help_button.png"))
        #self.helpButton.setAutoRaise(True)
        #self.doButton.setText("Extract")

        self.openOutputCheckBox.setChecked(True)
        self.modeFrame.setVisible(False)

        self.addFilesButton.setEnabled(True)
        self.addFolderButton.setEnabled(True)
        # self.upButton.setVisible(False)
        # self.downButton.setVisible(False)
        self.deleteButton.setEnabled(False)
        self.clearButton.setEnabled(False)

        self.doButton.setEnabled(False)
        self.openOutputButton.setEnabled(True)
        
        self.outputComboBox.setEditable(False)
        if os.path.exists(config.recent_output_dir_list_holder_file):
            dirList = pickle.load(open(config.recent_output_dir_list_holder_file, 'r'))
        else:
            dirList = []
        self.initOutputsList(dirList)
        self.connect(self.outputComboBox, QtCore.SIGNAL("currentIndexChanged(int)"),
                self.selectNewFolder)

        self.data = []
        self.size = None

        self.setAcceptDrops(True)
        
        s = self.filesTable
        s.setAutoFillBackground(True)
        s.setUniformRowHeights(True)
        newPalette = s.palette()
        newPalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(0xEF, 0xF4, 0xFA))
        #newPalette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(0xEF, 0xF4, 0xFA))
        s.setPalette(newPalette)

        #s.setHeaderHidden(True)
        s.setIndentation(0)

        s.updateValue([])

        self.connect(self.clearButton, QtCore.SIGNAL("clicked()"), self.clearTable)
        self.connect(self.deleteButton, QtCore.SIGNAL("clicked()"), self.deleteItem)
        # self.connect(self.upButton, QtCore.SIGNAL("clicked()"), self.upItem)
        # self.connect(self.downButton, QtCore.SIGNAL("clicked()"), self.downItem)
        self.connect(self.addFilesButton, QtCore.SIGNAL("clicked()"), self.browserFiles)
        self.connect(self.addFolderButton, QtCore.SIGNAL("clicked()"), self.browserFolder)

        self.connect(self.quitButton, QtCore.SIGNAL("clicked()"), self._emitDoQuit)
        self.connect(self.settingsButton, QtCore.SIGNAL("clicked()"), self._emitDoSettings)
        self.connect(self.aboutButton, QtCore.SIGNAL("clicked()"), self._emitDoAbout)
        self.connect(self.registerButton, QtCore.SIGNAL("clicked()"), self._emitDoRegister)
        self.connect(self.helpButton, QtCore.SIGNAL("clicked()"), self._emitDoHelp)
        self.connect(self.doButton, QtCore.SIGNAL("clicked()"), self._emitDoIt)

        self.connect(self.openOutputButton, QtCore.SIGNAL("clicked()"), self.openOutput)

        self.connect(self.filesTable, QtCore.SIGNAL("tablecleared()"),
                self.tableCleared)
        self.connect(self.filesTable, QtCore.SIGNAL("browserfiles()"),
                self.browserFiles)

    def initOutputsList(self, dirList=[]):
        self.outputComboBox.clear()
        self.outputComboBox.addItem(config.default_output_dir, QtCore.QVariant(config.default_output_dir))
        self.outputComboBox.addItem(QtGui.QApplication.translate("mainwidget", "Add Folder ...", None, QtGui.QApplication.UnicodeUTF8), QtCore.QVariant("Add Folder ..."))
        self.outputComboBox.addItem(QtGui.QApplication.translate("mainwidget", "Clear List", None, QtGui.QApplication.UnicodeUTF8), QtCore.QVariant("Clear List"))
        for d in dirList:
            self.outputComboBox.addItem(d, QtCore.QVariant(d))
        self.outputComboBox.setCurrentIndex(0)

    def selectNewFolder(self, i):
        idx = self.outputComboBox.currentIndex()
        text = unicode(self.outputComboBox.itemData(idx).toString())
        if text == u'Clear List':
            if os.path.exists(config.recent_output_dir_list_holder_file):
                os.remove(config.recent_output_dir_list_holder_file)
            self.initOutputsList()
        elif text == u'Add Folder ...':
            directory = QtGui.QFileDialog.getExistingDirectory(self, self.tr("Select Output Folder"),
                           QtCore.QDir.currentPath())
            if directory:
                directory = os.path.normpath(unicode(directory))
                if not os.path.exists(config.recent_output_dir_list_holder_file):
                    dirList = []
                else:
                    dirList = pickle.load(open(config.recent_output_dir_list_holder_file, 'r'))
                if directory not in dirList:
                    dirList.append(directory)
                    pickle.dump(dirList, open(config.recent_output_dir_list_holder_file, 'w'))
                self.initOutputsList(dirList)
                self.outputComboBox.setCurrentIndex(dirList.index(directory)+3)

    def openOutput(self):
        idx = self.outputComboBox.currentIndex()
        path = unicode(self.outputComboBox.itemText(idx))
        if os.path.exists(path):
            common.open_folder(path)

    def tableCleared(self):
        # self.upButton.setEnabled(False)
        # self.downButton.setEnabled(False)
        self.deleteButton.setEnabled(False)
        self.clearButton.setEnabled(False)
        self.doButton.setEnabled(False)

    def _emitDoHelp(self):
        self.emit(QtCore.SIGNAL("helpclicked"))

    def _emitDoQuit(self):
        self.emit(QtCore.SIGNAL("quitclicked"))

    def _emitDoSettings(self):
        self.emit(QtCore.SIGNAL("settingsclicked"))

    def _emitDoAbout(self):
        self.emit(QtCore.SIGNAL("aboutclicked"))

    def _emitDoRegister(self):
        self.emit(QtCore.SIGNAL("registerclicked"))

    def _emitDoIt(self):
        self.emit(QtCore.SIGNAL("doclicked"))

    def clearTable(self):
        self.filesTable.updateValue([])

    def deleteItem(self):
        selected = self.filesTable.selectedIndexes()
        if len(selected)>0:
            selected = [i.row() for i in selected]
            selected.sort()
            selected.reverse()
            data = self.filesTable.data[:]
            for idx in selected:
                try:
                    del data[idx]
                except IndexError:
                    pass
            self.filesTable.data = []
            self.filesTable.updateValue(data)

    def upItem(self):
        pass

    def downItem(self):
        pass

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/uri-list"):
            event.acceptProposedAction()

    def _addFilesFromDir(self, dirFullPath):
        d = []
        #os.chdir(dirFullPath)
        dirFullPath = os.path.normpath(dirFullPath)
        try:
            names = os.listdir(dirFullPath)
        except: # may raise WindowsError 5, access denied
            print 'passed for dirFullPath, ', dirFullPath
        else:
            for name in names:
                fullPath = os.path.join(dirFullPath, name)
                if os.path.isfile(fullPath):
                    if os.path.splitext(name)[1].lower() in config.supported_formats["image"]:
                        d.append(fullPath)
                elif os.path.isdir(fullPath):
                    d += self._addFilesFromDir(fullPath)
        return d

    def _change_btns_state(self):
        enableButton = False
        if self.filesTable.data:
            enableButton = True

        # self.upButton.setEnabled(enableButton)
        # self.downButton.setEnabled(enableButton)
        self.deleteButton.setEnabled(enableButton)
        self.clearButton.setEnabled(enableButton)
        self.doButton.setEnabled(enableButton)

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if not urls:
            return
        urls = [os.path.normpath(unicode(url.toLocalFile())) for url in urls]
        #d = self.filesTable.data
        d = []
        d_len = len(d)
        for fileFullPath in urls:
            if not fileFullPath:
                continue
            if os.path.isfile(fileFullPath):
                if fileFullPath not in d:
                    d.append(fileFullPath)
            elif os.path.isdir(fileFullPath):
                tmp_d = self._addFilesFromDir(fileFullPath)
                for f in tmp_d:
                    if f not in d:
                        d.append(f)

        if d == []:
            d = [''] # this will create a alert dialog
        self.filesTable.updateValue(d)

        self._change_btns_state()

    def addFiles(self, urls):
        if not urls:
            return
        urls = [os.path.normpath(unicode(url)) for url in urls]
        #d = self.filesTable.data
        d = []
        d_len = len(d)
        for fileFullPath in urls:
            if not fileFullPath:
                continue
            if os.path.isfile(fileFullPath):
                if fileFullPath not in d:
                    d.append(fileFullPath)
            elif os.path.isdir(fileFullPath):
                tmp_d = self._addFilesFromDir(fileFullPath)
                for f in tmp_d:
                    if f not in d:
                        d.append(f)

        self.filesTable.updateValue(d)
        self._change_btns_state()

    def browserFiles(self):
        files = QtGui.QFileDialog.getOpenFileNames(self, QtGui.QApplication.translate("mainwidget", "Select files to resize", None, QtGui.QApplication.UnicodeUTF8),
                os.path.expanduser("~"), QtGui.QApplication.translate("mainwidget", "Image Files (*.jpg *.jpeg *.jpe *.png *.tiff *.bmp *.gif)", None, QtGui.QApplication.UnicodeUTF8))
        self.addFiles(files)

    def browserFolder(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self, QtGui.QApplication.translate("mainwidget", "Select folder to resize", None, QtGui.QApplication.UnicodeUTF8),
                           os.path.expanduser("~"))
        if directory:
            directory = os.path.normpath(unicode(directory))
            if os.path.exists(directory):
                d = self._addFilesFromDir(directory)
                if len(d)<=0:
                    dlg = MessageDialog(self.parentWidget())
                    dlg.setText(QtGui.QApplication.translate("config", "Selected folder does not have any image files.", None, QtGui.QApplication.UnicodeUTF8))
                    common.show_dialog_on_top(dlg, self.parentWidget())
                    return
                else:
                    self.filesTable.updateValue(d)
                    self._change_btns_state()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())
