# -*- coding: utf-8 -*-
import os
import sys
import common
import playsound
from modulepath import module_path

from PyQt4 import QtGui

# only darwin & windows supported
if sys.platform == 'darwin':
    is_darwin = True
    is_windows = False
else:
    is_darwin = False
    is_windows = True

# international
enable_multi_lang = True

store = "fastspring"
# store = "regnow"

version = "3.2"
revision = 32
program_full_name = "Hibosoft Batch Image Resizer"
# main window title
# window_title = "Hibosoft Batch Image Resizer"
program_simple_name = "Batch Image Resizer"
version_text = "v" + version
# copyright_text = "© 2009-2014, Hibosoft Software"


#splash page graphics path
splash_icon = ':/images/splash.png'
#splash page delay time(seconds)
splash_delay = 1

# the first `program name' top menu
#main_menu_string = "&File"
main_menu_icon = ':/images/logo.png'

# the second `help' top menu
#help_menu_string = "&Help"
help_menu_icon = ':/images/help.png'

# supported file formats
supported_formats = {
                # gif, insp, pcx, ppm, spider, xbm, xv thumbnails
    'image': ['.jpg', '.jpeg', '.jpe', '.png', '.tiff', '.bmp', '.gif']
}

file_types = {
    'image': 'JPEG, PNG, TIFF, BMP, GIF'
}

# the files table alternative row background color
#An ARGB quadruplet on the format #AARRGGBB
#Note that it also holds a value for the alpha-channel. The default alpha channel is ff, i.e opaque.
file_table_alternative_row_color = 0xFF887FFB

# the complete info
# complete_dialog_info_prompt = QtGui.QApplication.translate("dialogs", """
#<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
#<html><head><meta name="qrichtext" content="1" /><style type="text/css">
#p, li { white-space: pre-wrap; }
#</style></head><body style=" font-family:'Arial'; font-size:9pt; font-weight:400; font-style:normal;">
#<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Arial'; font-size:14pt;"><span style=" font-size:18pt; font-weight:600;">Your resizing is complete!</span></p></body></html>
#""", None, QtGui.QApplication.UnicodeUTF8))

# change your purchase product http link here
if store == "fastspring":
    help_website = "http://www.hibosoft.com/help/hibosoft-batch-image-resizer/?a=f"
    def get_order_url():
        return "http://www.hibosoft.com/buy/hibosoft-batch-image-resizer/?a=f"
elif store == "regnow":
    help_website = "http://www.hibosoft.com/help/hibosoft-batch-image-resizer/?a=r"
    def get_order_url(regnow_order_regpath=''):
        default_order_url = "http://www.hibosoft.com/buy/hibosoft-batch-image-resizer/?a=r" 
        regnow_order_regpath = r"SOFTWARE\Digital River\SoftwarePassport\hibosoft software\Hibosoft Batch Image Resizer\0"
        if is_windows:
            import _winreg as winreg
            try:
                aReg = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
                aKey = winreg.OpenKey(aReg, regnow_order_regpath) 
                v, t = winreg.QueryValueEx(aKey,"BuyURL")
                winreg.CloseKey(aKey)
                return v
            except:
                try:
                    winreg.CloseKey(aKey)
                except:
                    pass
                return default_order_url
        return default_order_url

# check for update and download invalid sn
check_update_url = "http://www.hibosoft.com/checkup/hibosoft-batch-image-resizer/"
check_update_file = ".cu"

# Synchronous processes count
sync_processes_count = 2

# trial version can only process this number of files in each process session
trial_version_each_count = 3

# trial version can only use  this number of times
trial_version_use_times = 3

# the  trial version complete and registration reminder
#complete_dialog_registration_reminder_prompt = unicode(QtGui.QApplication.translate("config", """
#<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
#<html><head><meta name="qrichtext" content="1" /><style type="text/css">
#p, li { white-space: pre-wrap; }
#</style></head><body style=" font-family:'Arial'; font-size:9pt; font-weight:400; font-style:normal;">
#<hr />
#<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">The evaluation version of Hibosoft Batch Image Resizer only can resize max 3 files. </p>
#<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">To run unlimited resizing, enter a valid license key, which you may order</p>
#<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"> from our web store by clicking the order button below.</p></body></html>
#""", None, QtGui.QApplication.UnicodeUTF8))

# function to verify a license key
#   if it is a valid license key , return True, otherwise return False
#   def verify_license_key(name, license_key):
#        return True/False
verify_license_key_fun = common.verify_license_key

# function to check if this copy is registered
#   if it is a registered copy, return True, otherwise return False
#   def isRegistered():
#       return True/False
is_registered_fun = common.is_registered

# prompt for selecting files when click 'Click here to choose files' button & add files button
#select_files_prompt = QtGui.QApplication.translate("config", "Select files to resize", None, QtGui.QApplication.UnicodeUTF8)

#select_folder_prompt = QtGui.QApplication.translate("config", "Select folder to resize", None, QtGui.QApplication.UnicodeUTF8)
#selected_folded_is_empty_prompt = QtGui.QApplication.translate("config", "Selected folder does not have any image files.", None, QtGui.QApplication.UnicodeUTF8)

# the default output directory for output
default_output_dir = os.path.join(os.path.expanduser("~"), "Batch Image Resizer Out")

# we put the recent used output directories in this file
recent_output_dir_list_holder_file = os.path.join(os.path.expanduser("~"), "." + program_full_name, "outputs.txt")
# we put the recent used settings in this file
recent_settings_holder_file = os.path.join(os.path.expanduser("~"), "." + program_full_name, "settings.txt")
if not os.path.exists(os.path.join(os.path.expanduser("~"), "." + program_full_name)):
    os.makedirs(os.path.join(os.path.expanduser("~"), "." + program_full_name))


#call this function to play sound when procession complete
play_sound = playsound.play_sound_fun

#the wav sound file full path
compete_sound_file = os.path.join(module_path(), 'click.wav')
