# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui

from ui_promptwidget import Ui_promptWidget
import config

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class PromptWidget(QtGui.QLabel, Ui_promptWidget):
    def __init__(self, parent=None):
        QtGui.QLabel.__init__(self, parent)
        self.setupUi(self)
        #self.setFlat(True)
        #self.setWindowFlags(QtCore.Qt.Dialog|QtCore.Qt.FramelessWindowHint)

        if config.enable_multi_lang:
            locale = QtCore.QLocale.system().name()
            if str(locale).lower() == "zh_cn":
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/prompt_button_cn.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
                self.toolButton.setIcon(icon)

                self.label.setStyleSheet(_fromUtf8("background-image: url(:/images/prompt_text_cn.png); background-repeat: no-repeat;\n"))

        self.connect(self.toolButton, QtCore.SIGNAL("clicked()"),
                self._emitClicked)

    def _emitClicked(self):
        self.emit(QtCore.SIGNAL("clicked()"))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    w = PromptWidget()
    w.show()
    sys.exit(app.exec_())
