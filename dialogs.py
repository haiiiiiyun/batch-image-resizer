# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import config
import common
import os
import pickle
import webbrowser

from ui_aboutwidget import Ui_aboutDialog
from ui_registerwidget import Ui_registerDialog
from ui_wronglicensewidget import Ui_wrongLicenseDialog
from ui_completewidget import Ui_completeDialog
from ui_messagewidget import Ui_messageDialog
from ui_settingswidget import Ui_settingsDialog
from ui_processingwidget import Ui_processingDialog
from ui_updatewidget import Ui_updateDialog

def handleDarwinDialog(dlg):
    dlg.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.FramelessWindowHint)
    dlg.mainFrame.setFrameStyle(self.mainFrame.frameStyle()|QtGui.QFrame.Sunken)

class AboutDialog(QtGui.QDialog, Ui_aboutDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "About Batch Image Resizer", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("dialogs", "V3.2", None, QtGui.QApplication.UnicodeUTF8))
        # the copyright char can not be set
        # self.copyrightLabel.setText(config.copyright_text)
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)

class RegisterDialog(QtGui.QDialog, Ui_registerDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "Registration", None, QtGui.QApplication.UnicodeUTF8))
        self.keyLineEdit.setText('')
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)
        
        self.registerButton.setDefault(True)
        self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"),
                self.close)
        self.connect(self.registerButton, QtCore.SIGNAL("clicked()"),
                self.doRegister)
        self.connect(self.buyButton, QtCore.SIGNAL("clicked()"),
                self.doBuy)

    def doRegister(self):
        key = self.keyLineEdit.text()
        parent = self.parentWidget()
        if not key:
            dlg = MessageDialog(self.parentWidget())
            message = unicode(QtGui.QApplication.translate("dialogs", "Please enter a license key.", None, QtGui.QApplication.UnicodeUTF8))
            dlg.setText(message)
            common.show_dialog_on_top(dlg, self.parentWidget())
        else:
            if common.verify_license_key(key):
                self.close()
                dlg = MessageDialog(self.parentWidget())
                message = unicode(QtGui.QApplication.translate("dialogs", "Registration is complete, Thank you.", None, QtGui.QApplication.UnicodeUTF8))
                dlg.setText(message)
                common.show_dialog_on_top(dlg, self.parentWidget())
                self.parentWidget().registrationCompleted()
            else:
                dlg = WrongLicenseDialog(parent)
                r = common.show_dialog_on_top(dlg, self.parentWidget())
                if r==QtGui.QDialog.Accepted:
                    pass
                else:
                    self.close()

    def doBuy(self):
        order_url = config.get_order_url()
        webbrowser.open_new_tab(order_url)

class WrongLicenseDialog(QtGui.QDialog, Ui_wrongLicenseDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "License is invalid", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)

class CompleteDialog(QtGui.QDialog, Ui_completeDialog):
    def __init__(self, registered=False, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.completeLabel.setText(QtGui.QApplication.translate("dialogs", """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Arial'; font-size:9pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; font-size:14pt;"><span style=" font-size:18pt; font-weight:600;">Your resizing is complete!</span></p></body></html>
""", None, QtGui.QApplication.UnicodeUTF8))
        self.demoAlertLabel.setText(QtGui.QApplication.translate("dialogs", """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Arial'; font-size:9pt; font-weight:400; font-style:normal;">
<hr />
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">The evaluation version of Hibosoft Batch Image Resizer only can resize max 3 files. </p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">To run unlimited resizing, enter a valid license key, which you may order.</p>
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> from our web store by clicking the order button below.</p></body></html>
""", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "Processing is complete", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)

        self.okButton.setDefault(True)
        self.connect(self.licenseButton, QtCore.SIGNAL("clicked()"),
                self.doRegister)
        self.connect(self.buyButton, QtCore.SIGNAL("clicked()"),
                self.doPurchase)

        if registered:
            self.demoAlertLabel.setVisible(False)
            self.licenseButton.setVisible(False)
            self.buyButton.setVisible(False)
        self.status = registered

    def setStatus(self, registered):
        if self.status == registered:
            return

        if registered:
            self.demoAlertLabel.setVisible(False)
            self.licenseButton.setVisible(False)
            self.buyButton.setVisible(False)
        else:
            self.demoAlertLabel.setVisible(True)
            self.licenseButton.setVisible(True)
            self.buyButton.setVisible(True)
        self.status = registered

    def doRegister(self):
        p = self.parentWidget()
        self.close()
        p.doRegister()

    def doPurchase(self):
        webbrowser.open_new_tab(config.purchase_website)

class MessageDialog(QtGui.QDialog, Ui_messageDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "Infomation", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)

    def setText(self, text):
        self.messageLabel.setText(text)

class SettingsDialog(QtGui.QDialog, Ui_settingsDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)

        self.sizeModeComboBox.setEditable(False)
        self.sizeModeComboBox.clear()
        for (mode,txt) in ( 
            ("Set Width & Height in Pixels",
                unicode(QtGui.QApplication.translate("dialogs", "Set Width & Height in Pixels", None, QtGui.QApplication.UnicodeUTF8)),),
            ("Set Width in Pixels, Height Keep Ratio",
                unicode(QtGui.QApplication.translate("dialogs", "Set Width in Pixels, Height Keep Ratio", None, QtGui.QApplication.UnicodeUTF8)),),
            ("Set Height in Pixels, Width Keep Ratio",
                unicode(QtGui.QApplication.translate("dialogs", "Set Height in Pixels, Width Keep Ratio", None, QtGui.QApplication.UnicodeUTF8)),),
            ("Set Width & Height in Percentage",
                unicode(QtGui.QApplication.translate("dialogs", "Set Width & Height in Percentage", None, QtGui.QApplication.UnicodeUTF8)),),
            ("Set Width in Percentage, Height Keep Ratio",
                unicode(QtGui.QApplication.translate("dialogs", "Set Width in Percentage, Height Keep Ratio", None, QtGui.QApplication.UnicodeUTF8)),),
            ("Set Height in Percentage, Width Keep Ratio",
                unicode(QtGui.QApplication.translate("dialogs", "Set Height in Percentage, Width Keep Ratio", None, QtGui.QApplication.UnicodeUTF8)),),
        ):

            self.sizeModeComboBox.addItem(txt, QtCore.QVariant(mode))

        self.widthSpinBox.setRange(0, 65535)
        self.heightSpinBox.setRange(0, 65535)

        self.outputFormatComboBox.setEditable(False)
        self.outputFormatComboBox.clear()
        outputFormats = config.file_types["image"].split(", ")

        _text = unicode(QtGui.QApplication.translate("dialogs", "As Original", None, QtGui.QApplication.UnicodeUTF8))
        outputFormats.insert(0, _text)
        for fmt in outputFormats:
            self.outputFormatComboBox.addItem(fmt, QtCore.QVariant(fmt))

        self.connect(self.sizeModeComboBox, QtCore.SIGNAL("currentIndexChanged(int)"),
                self.sizeModeComboBoxChanged)
        self.connect(self.startButton, QtCore.SIGNAL("clicked()"),
                self.doStart)
        self.connect(self.okButton, QtCore.SIGNAL("clicked()"),
                self.doSettings)

    def sizeModeComboBoxChanged(self, i):
        idx = self.sizeModeComboBox.currentIndex()
        px = unicode(QtGui.QApplication.translate("dialogs", "px", None, QtGui.QApplication.UnicodeUTF8))
        if idx == 0: # Width & Height (Pixels)
            self.widthModeLabel.setText(px)
            self.widthSpinBox.setEnabled(True)
            self.heightModeLabel.setText(px)
            self.heightSpinBox.setEnabled(True)
            self.ratioLabel.setVisible(False)
        elif idx == 1: # Width Pixels (Keep Proportions)
            self.widthModeLabel.setText(px)
            self.widthSpinBox.setEnabled(True)
            self.heightModeLabel.setText(px)
            self.heightSpinBox.setEnabled(False)
            self.ratioLabel.setVisible(True)
        elif idx == 2: # Height Pixels (Keep Proportions)
            self.widthModeLabel.setText(px)
            self.widthSpinBox.setEnabled(False)
            self.heightModeLabel.setText(px)
            self.heightSpinBox.setEnabled(True)
            self.ratioLabel.setVisible(True)
        elif idx == 3: # Width & Height (Percentage)
            self.widthModeLabel.setText("%")
            self.widthSpinBox.setEnabled(True)
            self.heightModeLabel.setText("%")
            self.heightSpinBox.setEnabled(True)
            self.ratioLabel.setVisible(False)
        elif idx == 4: # Width Percentage (Keep Proportions)
            self.widthModeLabel.setText("%")
            self.widthSpinBox.setEnabled(True)
            self.heightModeLabel.setText("%")
            self.heightSpinBox.setEnabled(False)
            self.ratioLabel.setVisible(True)
        elif idx == 5: # Height Percentage (Keep Proportions)
            self.widthModeLabel.setText("%")
            self.widthSpinBox.setEnabled(False)
            self.heightModeLabel.setText("%")
            self.heightSpinBox.setEnabled(True)
            self.ratioLabel.setVisible(True)

    # restore settings
    def restore(self):
        if os.path.exists(config.recent_settings_holder_file):
            values = pickle.load(open(config.recent_settings_holder_file, 'r'))
        else:
            values = {"sizeMode": 3, "width": 50, "height": 50, "format": 0, \
                    "keepDateTime": False, "overwriteFiles": False, "playSound": True}

        self.sizeModeComboBox.setCurrentIndex(values["sizeMode"])
        self.widthSpinBox.setValue(values["width"])
        self.heightSpinBox.setValue(values["height"])
        self.outputFormatComboBox.setCurrentIndex(values["format"])
        self.keepDateTimeCheckBox.setChecked(values["keepDateTime"])
        self.overwriteFilesCheckBox.setChecked(values["overwriteFiles"])
        self.playSoundCheckBox.setChecked(values["playSound"])

    # save settings
    def save(self):
        values = {"sizeMode": self.sizeModeComboBox.currentIndex(),\
                "width": self.widthSpinBox.value(),\
                "height": self.heightSpinBox.value(),\
                "format": self.outputFormatComboBox.currentIndex(), \
                "keepDateTime": self.keepDateTimeCheckBox.isChecked(),\
                "overwriteFiles": self.overwriteFilesCheckBox.isChecked(),\
                "playSound": self.playSoundCheckBox.isChecked()}
        pickle.dump(values, open(config.recent_settings_holder_file, 'w'))
        return values


    def initForSetting(self):
        self.startButton.setVisible(False)
        self.okButton.setVisible(True)

    def initForStart(self):
        self.startButton.setVisible(True)
        self.okButton.setVisible(False)

    def doStart(self):
        self.doSettings()
        self.parentWidget().doIt()

    def doSettings(self):
        values = self.save()
        mode = unicode(self.sizeModeComboBox.itemData(self.sizeModeComboBox.currentIndex()).toString())
        outputFormat = unicode(self.outputFormatComboBox.itemData(self.outputFormatComboBox.currentIndex()).toString())
        self.parentWidget().setSettings(mode = mode, width = values["width"], height = values["height"], \
                keepDateTime = values["keepDateTime"], overwriteFiles = values["overwriteFiles"], \
                outputFormat = outputFormat, playSound = values["playSound"])
        self.close()

class ProcessingDialog(QtGui.QDialog, Ui_processingDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)

        self.canceled = False

        self.connect(self.cancelButton, QtCore.SIGNAL("clicked()"),
                self.doCancel)

    def setMinimumDuration(self, v):
        pass


    def doCancel(self):
        self.canceled = True

    def setRange(self, start, end):
        self.progressBar.setRange(start, end)

    def setValue(self, v):
        self.progressBar.setValue(v)

    def wasCanceled(self):
        return self.canceled

    def setCancelButtonText(self, text):
        self.cancelButton.setText(text)

    def setFormat(self, fmt):
        self.progressBar.setFormat(fmt)

    def updateProgress(self, processTotal, currentFileFullPath=''):
        processValue = self.progressBar.value() + 1
        self.progressBar.setValue(processValue)
        filename = ""
        if currentFileFullPath:
            filename = os.path.basename(currentFileFullPath)
        _text = unicode(QtGui.QApplication.translate("dialogs", "Processing ", None, QtGui.QApplication.UnicodeUTF8))
        self.messageLabel.setText(_text + filename + " ...")

class UpdateDialog(QtGui.QDialog, Ui_updateDialog):
    def __init__(self, parent=None, program_name="Hibosoft Batch Image Resizer", version="3.1.4.330", download_url="http://www.hibosoft.com/download/"):
        QtGui.QDialog.__init__(self, parent)
        self.download_url = download_url
        self.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("dialogs", "New Version Available", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowFlags(self.windowFlags()^QtCore.Qt.WindowContextHelpButtonHint)
        if config.is_darwin:
            handleDarwinDialog(self)

        self.messageLabel.setText(QtGui.QApplication.translate("dialogs", "New version of is available.\nWould you like to upgrade to the newest version now?", None, QtGui.QApplication.UnicodeUTF8))

        # self.connect(self.askLaterButton, QtCore.SIGNAL("clicked()"),
        #        self.close)
        self.connect(self.noButton, QtCore.SIGNAL("clicked()"),
                self.do_not_remind)
        self.connect(self.downloadButton, QtCore.SIGNAL("clicked()"),
                self.go_download)

    def do_not_remind(self):
        self.close()
        if os.path.exists(config.recent_settings_holder_file):
            values = pickle.load(open(config.recent_settings_holder_file, 'r'))
        else:
            values = {"checkUpdate": False, "sizeMode": 3, "width": 50, "height": 50, "format": 0, \
                    "keepDateTime": False, "overwriteFiles": False, "playSound": True}
        values["checkUpdate"] = False

        pickle.dump(values, open(config.recent_settings_holder_file, 'w'))

    def go_download(self):
        self.close()
        webbrowser.open_new_tab(self.download_url)
        

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    # dlg = BrowserDialog()
    # dlg.show()
    sys.exit(app.exec_())
                
