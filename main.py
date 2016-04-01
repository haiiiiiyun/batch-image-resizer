# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
import os
import time
import pickle
import webbrowser

import config
import common

from PyQt4 import QtCore, QtGui

import prog_rc
from mainwidget import MainWidget
from checkup import CheckupThread
from dialogs import *

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.setWindowIcon(QtGui.QIcon(":/images/Ir_48x48.png"))

        self.centralViewer = MainWidget()
        self.settings = {}
        self.initSettngs()

        self.connect(self.centralViewer, QtCore.SIGNAL("quitclicked"),
                self.close)
        self.connect(self.centralViewer, QtCore.SIGNAL("settingsclicked"),
                self.doSettings)
        self.connect(self.centralViewer, QtCore.SIGNAL("aboutclicked"),
                self.doAbout)
        self.connect(self.centralViewer, QtCore.SIGNAL("registerclicked"),
                self.doRegister)
        self.connect(self.centralViewer, QtCore.SIGNAL("helpclicked"),
                self.doHelp)
        self.connect(self.centralViewer, QtCore.SIGNAL("doclicked"),
                self.doSettingsAndStart)
        self.setCentralWidget(self.centralViewer)
        self.createActions()
        self.createMenus()
        #self.createToolbar()

        self.has_registered = config.is_registered_fun()
        if self.has_registered:
            self.setWindowTitle(QtGui.QApplication.translate("main", "Hibosoft Batch Image Resizer", None, QtGui.QApplication.UnicodeUTF8))
        else:
            self.setWindowTitle(QtGui.QApplication.translate("main", "Hibosoft Batch Image Resizer ( Evaluation Version )", None, QtGui.QApplication.UnicodeUTF8))

    def createActions(self):
        self.licenseAct = QtGui.QAction(QtGui.QIcon(":/images/key.png"), 
                self.tr("&Registration"), self)
        self.connect(self.licenseAct, QtCore.SIGNAL("triggered()"),
                self.doRegister)
        self.settingsAct = QtGui.QAction(QtGui.QIcon(":/images/setting.png"), 
                self.tr("&Settings"), self)
        self.connect(self.settingsAct, QtCore.SIGNAL("triggered()"),
                self.doSettings)
        self.aboutAct = QtGui.QAction(QtGui.QIcon(":/images/info.png"), 
                self.tr("&About"), self)
        self.connect(self.aboutAct, QtCore.SIGNAL("triggered()"),
                self.doAbout)
        self.quitAct = QtGui.QAction(QtGui.QIcon(":/images/exit.png"), 
                self.tr("&Quit"), self)
        self.connect(self.quitAct, QtCore.SIGNAL("triggered()"),
				self.close)
        self.helpAct = QtGui.QAction(QtGui.QIcon(":/images/help_button.png"), 
                self.tr("&Help"), self)
        self.connect(self.helpAct, QtCore.SIGNAL("triggered()"),
				self.doHelp)

    def doHelp(self):
        path = config.help_website
        webbrowser.open_new_tab(path)

    def doAbout(self):
        dlg = AboutDialog(self)
        common.show_dialog_on_top(dlg, self)

    def newVersionAvailable(self, prog_name, version, revision, required_mini_revision, url, download_url):
        dlg = UpdateDialog(self, prog_name, version, download_url)
        common.show_dialog_on_top(dlg, self)

    def doRegister(self):
        dlg = RegisterDialog(self)
        common.show_dialog_on_top(dlg, self)
    
    def registrationCompleted(self):
        self.has_registered = True
        self.setWindowTitle(config.window_title)

    def _createDoThread(self, progress_dialog, process_total, file_full_path, has_registered, **kwargs):
        #output_dir, output_format, password, codec, ):
        output_dir = kwargs.get('output_dir', config.default_output_dir)
        print 'output=', output_dir
        print 'processing=', file_full_path
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        thread = common.DoThread(progress_dialog, process_total, file_full_path, has_registered, **kwargs)
        self.connect(thread, QtCore.SIGNAL("dofinished"), progress_dialog.updateProgress)
        thread.start()
        return thread

    def doIt(self):
        files = self.centralViewer.filesTable.data[:]

        progress_dialog = ProcessingDialog(self)
        #common.show_dialog_on_top(progress_dialog, self)
        dialog_geometry = progress_dialog.geometry()
        width = dialog_geometry.width()
        height = dialog_geometry.height()
        main_geometry = self.geometry()
        dialog_geometry.setY(main_geometry.y())
        dialog_geometry.setX(main_geometry.x()+(main_geometry.width()-dialog_geometry.width())/2)
        dialog_geometry.setWidth(width)
        dialog_geometry.setHeight(height)
        progress_dialog.setGeometry(dialog_geometry)
        ###

        progress_dialog.setMinimumDuration(0)
        progress_dialog.setCancelButtonText('Stop')

        process_total = len(files)
        process_total += 1
        progress_dialog.setRange(0, process_total)
        process_val = 0
        do_thread_list = []

        progress_dialog.show()
        progress_dialog.updateProgress(process_total, '')

        processed_count = 0
        complete_normal = True
        used_times = -1
        auto_open = self.centralViewer.openOutputCheckBox.isChecked()
        output_dir = os.path.normpath(unicode(self.centralViewer.outputComboBox.currentText()))

        progress_dialog.updateProgress(process_total, '')

        while True:
            while files and len(do_thread_list)<config.sync_processes_count:
                f = files.pop(0)
                if self.has_registered:
                    thread = self._createDoThread(progress_dialog, process_total, 
                        f, True, \
                        outputDir = output_dir,\
                        autoOpen = auto_open,\
                        **self.settings)
                    do_thread_list.append(thread)
                else:
                    if (processed_count >= config.trial_version_each_count):
                        # trial version process limitation
                        progress_dialog.updateProgress(process_total, '')
                    else:
                        thread = self._createDoThread(progress_dialog, process_total, 
                            f, True, \
                            outputDir = output_dir,\
                            **self.settings)
                        do_thread_list.append(thread)
                processed_count += 1
            QtGui.qApp.processEvents()
            if progress_dialog.wasCanceled():
                complete_normal = False
                for t in do_thread_list:
                    t.cancel()
                    t.exit()
                return
            if len(do_thread_list)<=0:
                progress_dialog.close()
                break;
            else:
                for t in do_thread_list:
                    if t.isFinished():
                        do_thread_list.remove(t)

        if complete_normal:
            if self.settings.get("playSound", False):
                config.play_sound(config.compete_sound_file)
            if auto_open:
                common.open_folder(output_dir)

        dlg = CompleteDialog(self.has_registered, self)
        common.show_dialog_on_top(dlg, self)

    def doSettings(self):
        dlg = SettingsDialog(self)
        dlg.initForSetting()
        dlg.restore()
        common.show_dialog_on_top(dlg, self)

    def doSettingsAndStart(self):
        dlg = SettingsDialog(self)
        dlg.initForStart()
        dlg.restore()
        common.show_dialog_on_top(dlg, self)

    # save the settings
    def setSettings(self, **kwargs):
        self.settings.update(kwargs)

    def initSettngs(self):
        if os.path.exists(config.recent_settings_holder_file):
            self.settings = pickle.load(open(config.recent_settings_holder_file, 'r'))
        else:
            self.settings = {"checkUpdate": True, "sizeMode": 3, "width": 50, "height": 50, "format": 0, \
                    "keepDateTime": False, "overwriteFiles": False, "playSound": True}

    def createMenus(self):
        self.progMenu = self.menuBar().addMenu(QtGui.QApplication.translate("main", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.helpMenu = self.menuBar().addMenu(QtGui.QApplication.translate("main", "&Help", None, QtGui.QApplication.UnicodeUTF8))

        self.progMenu.addAction(self.licenseAct)
        self.progMenu.addAction(self.settingsAct)
        self.progMenu.addAction(self.quitAct)

        self.helpMenu.addAction(self.helpAct)
        self.helpMenu.addAction(self.aboutAct)

    def createToolbar(self):
        self.menuToolbar = self.addToolBar("menuToolbar")
        self.menuToolbar.setMovable(False)

        self.progMenuToolButton = QtGui.QToolButton(self)
        self.progMenuToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.progMenuToolButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.progMenuToolButton.setText(config.main_menu_string)
        #self.progMenuToolButton.setIcon(QtGui.QIcon(config.main_menu_icon))
        #self.progMenuToolButton.setDefaultAction(self.aboutAct)
        self.connect(self.progMenuToolButton, QtCore.SIGNAL("clicked()"),
                self.progMenuToolButton.showMenu)

        pm = QtGui.QMenu(self)
        pm.addAction(self.licenseAct)
        pm.addAction(self.aboutAct)
        pm.addAction(self.quitAct)

        self.progMenuToolButton.setMenu(pm)
        self.menuToolbar.addWidget(self.progMenuToolButton)

        self.helpToolButton = QtGui.QToolButton(self)
        self.helpToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.helpToolButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.helpToolButton.setText(config.help_menu_string)
        #self.helpToolButton.setIcon(QtGui.QIcon(config.help_menu_icon))
        #self.helpToolButton.setDefaultAction(self.helpAct)
        self.connect(self.helpToolButton, QtCore.SIGNAL("clicked()"),
                self.helpToolButton.showMenu)

        pm = QtGui.QMenu(self)
        pm.addAction(self.helpAct)
        self.helpToolButton.setMenu(pm)
        self.menuToolbar.addWidget(self.helpToolButton)
    def closeEvent(self, e):
        #self.writeSettings()
        QtGui.QMainWindow.closeEvent(self, e)

        
if __name__ == "__main__":
    reload(sys)
    if hasattr(sys, 'setdefaultencoding'):
        sys.setdefaultencoding('utf-8')

    os.chdir(common.module_path())
    app = QtGui.QApplication(sys.argv)
    #app.setStyle("Plastique")

    QtCore.QCoreApplication.addLibraryPath("./")

    # language setup
    if config.enable_multi_lang:
        # language setup
        locale = QtCore.QLocale.system().name()
        appTranslator = QtCore.QTranslator()
        if appTranslator.load("lang_" + locale):
            app.installTranslator(appTranslator)
    

    splash = QtGui.QSplashScreen()
    splash.setPixmap(QtGui.QPixmap(config.splash_icon))
    splash.show()
    # bottomLeft = QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom
    # splash.showMessage(QtCore.QObject().tr("initializing..."), bottomLeft, QtCore.Qt.black)
    # app.processEvents()
    time.sleep(config.splash_delay)

    main = MainWindow()
    main.resize(580, 480)
    main.show()
    
    #check update
    thread = CheckupThread()
    if main.settings.get("checkUpdate", True):
        main.connect(thread, QtCore.SIGNAL("newversion"), main.newVersionAvailable)
    thread.start()

    splash.finish(main)
    sys.exit(app.exec_())
