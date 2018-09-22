#
# Copyright (c) 2006 Alexey Borzenkov (snaury@gmail.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
"""This module is created as a workaround for bugs in Python 2.4/2.5"""

import os

__all__ = ['nativenseconds', 'getnativefiletime', 'getfiletime', 'setnativefiletime', 'setfiletime']

class filetime_result(tuple):

    @property
    def ctime(self):
        return self[0]

    @property
    def atime(self):
        return self[1]

    @property
    def mtime(self):
        return self[2]

__secs_between_epochs = 11644473600
def __time_to_FILETIME(time):
    return long((time + __secs_between_epochs) * 10000000)
def __FILETIME_to_time(time):
    return (time - __secs_between_epochs * 10000000) / 10000000.0
def nativenseconds(secs):
    return long(secs * 10000000)

if os.name == 'nt':

    try:
        import ctypes
        __have_ctypes = True
    except:
        __have_ctypes = False

if os.name == 'nt' and __have_ctypes:

    try:
        __CreateFile = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)
        __CreateFile = __CreateFile(('CreateFileW', ctypes.windll.kernel32), (
            (1, 'lpFileName'),
            (1, 'dwDesiredAccess'),
            (1, 'dwShareMode'),
            (1, 'lpSecurityAttributes'),
            (1, 'dwCreationDisposition'),
            (1, 'dwFlagsAndAttributes'),
            (1, 'hTemplateFile'),))
    except AttributeError:
        __CreateFile = ctypes.WINFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_void_p)
        __CreateFile = __CreateFile(('CreateFileA', ctypes.windll.kernel32), (
            (1, 'lpFileName'),
            (1, 'dwDesiredAccess'),
            (1, 'dwShareMode'),
            (1, 'lpSecurityAttributes'),
            (1, 'dwCreationDisposition'),
            (1, 'dwFlagsAndAttributes'),
            (1, 'hTemplateFile'),))

    __GetFileTime = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
    __SetFileTime = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64))
    __CloseHandle = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_void_p)

    __GetFileTime = __GetFileTime(('GetFileTime', ctypes.windll.kernel32), (
        (1, 'hFile'),
        (2, 'lpCreationTime'),
        (2, 'lpLastAccessTime'),
        (2, 'lpLastWriteTime'),))
    __SetFileTime = __SetFileTime(('SetFileTime', ctypes.windll.kernel32), (
        (1, 'hFile'),
        (1, 'lpCreationTime'),
        (1, 'lpLastAccessTime'),
        (1, 'lpLastWriteTime'),))
    __CloseHandle = __CloseHandle(('CloseHandle', ctypes.windll.kernel32), (
        (1, 'hObject'),))

    __OPEN_EXISTING = 3
    __FILE_WRITE_ATTRIBUTES = 0x40000000 # GENERIC_READ (0x80000000L)
    __FILE_READ_ATTRIBUTES = 0x80000000 # GENERIC_WRITE (0x40000000L)
    __FILE_FLAG_BACKUP_SEMANTICS = 0x02000000

    def __check_CreateFile(result, func, args):
        if result == -1 or result == 0xFFFFFFFF:
            raise ctypes.WinError()
        return result
    __CreateFile.errcheck = __check_CreateFile

    def __check_FileTime(result, func, args):
        if not result:
            raise ctypes.WinError()
        return args[1], args[2], args[3]
    __GetFileTime.errcheck = __check_FileTime
    __SetFileTime.errcheck = __check_FileTime

    def getnativefiletime(filename):
        """gets file's ctime, atime and mtime in native units (uses Windows native API)"""
        hFile = __CreateFile(filename, __FILE_READ_ATTRIBUTES, 0, None, __OPEN_EXISTING, __FILE_FLAG_BACKUP_SEMANTICS, None)
        try:
            ctime, atime, mtime = __GetFileTime(hFile)
            return filetime_result((ctime.value, atime.value, mtime.value))
        finally:
            __CloseHandle(hFile)

    def getfiletime(filename):
        """gets file's ctime, atime and mtime (uses Windows native API)"""
        ctime, atime, mtime = getnativefiletime(filename)
        ctime = __FILETIME_to_time(ctime)
        atime = __FILETIME_to_time(atime)
        mtime = __FILETIME_to_time(mtime)
        return filetime_result((ctime, atime, mtime))

    def setnativefiletime(filename, ctime=None, atime=None, mtime=None):
        """sets file's ctime, atime and mtime in native units (uses Windows native API)"""
        hFile = __CreateFile(filename, __FILE_WRITE_ATTRIBUTES, 0, None, __OPEN_EXISTING, __FILE_FLAG_BACKUP_SEMANTICS, None)
        try:
            if ctime is not None:
                ctime = ctypes.c_uint64(ctime)
            if atime is not None:
                atime = ctypes.c_uint64(atime)
            if mtime is not None:
                mtime = ctypes.c_uint64(mtime)
            __SetFileTime(hFile, ctime, atime, mtime)
        finally:
            __CloseHandle(hFile)

    def setfiletime(filename, ctime=None, atime=None, mtime=None):
        """sets file's ctime, atime and mtime (uses Windows native API)"""
        if ctime is not None:
            ctime = __time_to_FILETIME(ctime)
        if atime is not None:
            atime = __time_to_FILETIME(atime)
        if mtime is not None:
            mtime = __time_to_FILETIME(mtime)
        setnativefiletime(filename, ctime, atime, mtime)

else:

    def getfiletime(filename):
        """gets file's ctime, atime and mtime (uses Python os API)"""
        st = os.stat(filename)
        return filetime_result((st.st_ctime, st.st_atime, st.st_mtime))

    def getnativefiletime(filename):
        ctime, atime, mtime = getfiletime(filename)
        ctime = __time_to_FILETIME(ctime)
        atime = __time_to_FILETIME(atime)
        mtime = __time_to_FILETIME(mtime)
        return filetime_result((ctime, atime, mtime))

    def setfiletime(filename, ctime=None, atime=None, mtime=None):
        """sets file's atime and mtime (uses Python os API)"""
        if atime is None or mtime is None:
            st = os.stat(filename)
            if atime is None:
                atime = st.st_atime
            if mtime is None:
                mtime = st.st_mtime
        os.utime(filename, (atime, mtime))

    def setnativefiletime(filename, ctime=None, atime=None, mtime=None):
        if ctime is not None:
            ctime = __FILETIME_to_time(ctime)
        if atime is not None:
            atime = __FILETIME_to_time(atime)
        if mtime is not None:
            mtime = __FILETIME_to_time(mtime)
        setfiletime(filename, ctime, atime, mtime)
