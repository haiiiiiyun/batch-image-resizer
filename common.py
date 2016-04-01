# -*- coding: utf-8 -*-
import os
import sys
import datetime
import time
import shutil
import tempfile

from process import process
from modulepath import module_path
from PyQt4 import QtCore
import checkkey

HOME = os.path.expanduser("~")
__ = 0
for _ in  "Hibo soft Batch Image Resizer":
    __ += ord(_)
REGISTER_FILE_PATH = os.path.normpath(os.path.join(HOME, ".hbbir-" + str(__)))
USE_TIME_LIMIT_FILE_BASE_NAME = os.path.normpath(os.path.join(HOME, ".hbbir2-" + str(__)))

def show_dialog_on_top(dialog, mainwindow, width_inc=0, height_inc=0):
    dialog_geometry = dialog.geometry()
    width = dialog_geometry.width()
    height = dialog_geometry.height()
    main_geometry = mainwindow.geometry()
    dialog_geometry.setY(main_geometry.y())
    dialog_geometry.setX(main_geometry.x()+(main_geometry.width()-dialog_geometry.width())/2)
    dialog_geometry.setWidth(width + width_inc)
    dialog_geometry.setHeight(height + height_inc)
    dialog.setGeometry(dialog_geometry)
    return dialog.exec_()

def jiaMi(s , key):
    b = bytearray( str(s).encode("utf-8"))
    n = len(b) # 求出 b 的字节数
    c = bytearray( n*2 )
    j = 0
    for i in range( 0, n ):
        b1 = b[i]
        b2 = b1 ^ key     # b1 = b2^ key
        c1 = b2 % 16
        c2 = b2 // 16     # b2= c2*16 + c1
        c1 = c1 + 65
        c2 = c2 + 65      # 由于c1,c2都是 0~15之间的数,
                          # 加上65就变成了A-P 的字符的编码
        c[j]    = c1
        c[j+1] = c2
        j = j+2
    return c.decode("utf-8")

def jieMi( s, key):
    c = bytearray( str(s).encode("utf-8") )
    n = len(c) # 求出 b 的字节数
    if n % 2 != 0 :
        return ""
    n = n // 2
    b = bytearray( n )
    j = 0
    for i in range( 0, n ):
        c1 = c[j] 
        c2 = c[j+1] 
        j   = j+2
        c1 = c1 - 65
        c2 = c2 - 65
        b2 = c2*16 + c1
        b1 = b2^ key
        b[i]= b1
    try:   
      return b.decode("utf-8")
    except:
      return ""

def verify_license_key(license_key):
    license_key = str(license_key)
    if checkkey.pkv_check_key(license_key) == 0: # valid
        today = datetime.date.today()

        if not os.path.exists(REGISTER_FILE_PATH):
            key = license_key + "-%0.4d-%0.2d%0.2d"%(today.year, today.month, today.day)
            try:
                f = open(REGISTER_FILE_PATH, 'w')
                f.write(jiaMi(key, 0x84))
                f.close()
            except IOError:
                return False
        # set file attr to hidden on windows
        set_file_hidden(unicode(REGISTER_FILE_PATH))
        return True
    return False

# function to check if this copy is registered
#   if it is a registered copy, return True, otherwise return False

def is_registered():
    try:
        f = open(REGISTER_FILE_PATH, 'r')
        ln = f.read()
        f.close()
    except IOError:
        return False
    key = jieMi(ln, 0x84)
    license_key = key[:29]
    try:
        regYear = key[-9:-5]
        regMonth = key[-4:-2]
        regDay = key[-2:]
        regDate = datetime.date(int(regYear), int(regMonth), int(regDay))
    except:
        return False

    # if this key is black listed
    if checkkey.pkv_check_key(license_key) != 0: # invalid
        os.remove(REGISTER_FILE_PATH)
        return False

    today = datetime.date.today()

    #After 30 days, there needs to be a remote server call to see if the key is present, 
    #and if it is present, delete the hidden file because this user was given a refund 
    #and is no longer registered. If the no key was found, do nothing to the hidden file.
    if today + datetime.timedelta(days=-30) > regDate:
        if remote_check_license_key_refund(license_key):
            os.remove(REGISTER_FILE_PATH)
            return False
        else: # We change registeration date to a big one so we don't need to remote check again
            try:
                # reset file hidden attr windows, python will raise `IOError 13' when opening a hidden file for modification
                reset_file_hidden(unicode(REGISTER_FILE_PATH))
                f = open(REGISTER_FILE_PATH, 'w')
                key = license_key + "-3011-0101"
                f.write(jiaMi(key, 0x84))
                f.close()
                # set file attr to hidden on windows
                set_file_hidden(unicode(REGISTER_FILE_PATH))
                return True
            except IOError:
                return False
    return True

#if refund, return True, otherwise return False

def remote_check_license_key_refund(license_key):
    return False

def build_output_filename(src_file_fullpath, output_dir_fullpath, target_ext, overwrite_files):
    filename = os.path.splitext(os.path.basename(src_file_fullpath))[0]
    path = unicode(os.path.join(output_dir_fullpath, filename + target_ext))
    if overwrite_files:
        return path

    if not os.path.exists(path):
        return path
    index = 1
    while True:
        path = unicode(os.path.join(output_dir_fullpath, filename + '_' + str(index)+target_ext))
        if not os.path.exists(path):
            return path
        index += 1
    return u''

class DoThread(QtCore.QThread):
    def __init__(self, progress_dialog, process_total, src_file_fullpath, is_registered, **kwargs):
        QtCore.QThread.__init__(self)
        self.progress_dialog = progress_dialog
        self.process_total = process_total
        self.src_file_fullpath = src_file_fullpath
        self.is_registered = is_registered
        self.output_dir = kwargs.get("outputDir")
        self.mode = kwargs.get("mode")
        self.width = kwargs.get("width")
        self.height = kwargs.get("height")
        self.keep_datetime = kwargs.get("keepDateTime")
        self.overwrite_files = kwargs.get("overwriteFiles")
        self.output_format = kwargs.get("outputFormat")

        self.hasCanceled = False
        self.hasFinished = False

    def finished(self):
        return self.hasFinished

    def cancel(self):
        self.hasCanceled = True

    def run(self):
        target_ext = os.path.splitext(os.path.basename(self.src_file_fullpath))[1]
        if self.output_format in ("JPEG", "PNG", "TIFF", "BMP",):
            target_ext = "." + str(self.output_format).lower()
        output_file = build_output_filename(self.src_file_fullpath, self.output_dir, target_ext, self.overwrite_files)

        if self.hasCanceled:
            self.hasFinished = True
            self.emit(QtCore.SIGNAL("dofinished"), self.process_total, self.src_file_fullpath)
            return
        ret = process(src_file = self.src_file_fullpath, dest_file = output_file,\
                width = self.width, height = self.height,\
                mode = self.mode, keep_datetime = self.keep_datetime)
        self.hasFinished = True
        self.emit(QtCore.SIGNAL("dofinished"), self.process_total, self.src_file_fullpath)

# ----------------------------------------------------------------------------
# subprocess.terminate is not implemented on some Windows python versions.
# This workaround works on both POSIX and Windows.

def subprocess_terminate( proc ) :
    try:
        proc.terminate()
    except AttributeError:
        print " no terminate method to Popen.."
        try:
            import signal
            os.kill( proc.pid , signal.SIGTERM)
        except AttributeError:
            print "  no os.kill, using ctypes..."
            try:
                import ctypes
                PROCESS_TERMINATE = 1
                handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, proc.pid)
                ctypes.windll.kernel32.TerminateProcess(handle, -1)
                ctypes.windll.kernel32.CloseHandle(handle)
            except ImportError:
                print "  ERROR: could not terminate process."


# We cannot rely on __file__, because __file__ is not there in the py2exed main-script.

# get jpg file demension width/height
# reference: http://www.64lines.com/jpeg-width-height

def jpeg_width_height(jpeg_file_path):
    try:
        f = open(jpeg_file_path, "rb")
    except IOError:
        return (0, 0,)
    data = f.read()
    data_size = len(data)
    i=0
    # data[0~3]: 0xFFD8FFE0
    i += 4
    # data[6~9]: 'JFIF' or 'EXIF'
    block_length = ord(data[i])*256 + ord(data[i+1])

    while i<data_size:
        i+=block_length
        if i>=data_size:
            return (0, 0,)
        if ord(data[i]) != 0xFF:
            return (0, 0,)
        if ord(data[i+1]) == 0xC0:
            return (ord(data[i+7])*256 + ord(data[i+8]), ord(data[i+5])*256 + ord(data[i+6]),) # (widht, height,)
        else:
            i+=2
            block_length = ord(data[i])*256+ord(data[i+1])
    return (0, 0,)

# open folder using the default folder explorer

if sys.platform == 'darwin':
    import subprocess
    def open_folder(path):
        subprocess.check_call(['open', '--', path])
else: #window
    import webbrowser
    def open_folder(path):
        webbrowser.open_new_tab(path)

# get number of used times, trial version has use times limitation
def used_times():
    idx = 0
    while True:
        filepath = USE_TIME_LIMIT_FILE_BASE_NAME + str(idx+1)
        if not os.path.exists(filepath):
            return idx
        idx += 1

def increment_used_times():
    ut = used_times()
    filepath = USE_TIME_LIMIT_FILE_BASE_NAME + str(ut+1)
    if not os.path.exists(filepath):
        try:
            f = open(filepath, 'w')
            f.close()
        except IOError:
            return False
        # set file attr to hidden on windows
        if not set_file_hidden(filepath):
            return False
    return True

def set_file_hidden(filepath):
    # change file attr to hidden on windows
    try:
        import ctypes
        # FILE_ATTRIBUTE_HIDDEN: 0x02
        ctypes.windll.kernel32.SetFileAttributesW(filepath, 0x02)
    except:
        return False

def reset_file_hidden(filepath):
    # reset file hidden attr on windows
    try:
        import ctypes
        ctypes.windll.kernel32.SetFileAttributesW(unicode(REGISTER_FILE_PATH), 0x0)
    except:
        pass

if __name__ == "__main__":
    print is_registered()

