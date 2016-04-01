# -*- coding: utf-8 -*-
import os, sys

# We cannot rely on __file__, because __file__ is not there in the py2exed/PyInstaller main-script.

def we_are_frozen():
    """Returns whether we are frozen via py2exe/PyInstaller.
    This will affect how we find out where we are located."""
    return hasattr(sys, "frozen")

def module_path():
    """ This will get us the program's directory,
    even if we are frozen using py2exe/PyInstaller"""

    if we_are_frozen():
        if "_MEIPASS2" in os.environ: #PyInstaller one-file package
            return os.path.dirname(unicode(os.environ["_MEIPASS2"], sys.getfilesystemencoding( )))
        return os.path.dirname(unicode(sys.executable, sys.getfilesystemencoding( )))

    return os.path.dirname(unicode(__file__, sys.getfilesystemencoding( )))


