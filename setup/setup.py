# -*- coding: utf-8 -*-
# filename:setup.py

from distutils.core import setup
import py2exe
import sys
import os

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

excludes = []
class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "3.2"
        self.company_name = "Hibosoft Software"
        self.copyright = "Copyright (C) 2009-2014 Hibosoft Software"
        self.name = "Hibosoft Batch Image Resizer"
        #self.comments = "A Batch Image Resizer App",
        #self.file_description = 'Hibosoft Batch Image Resizer',
        #self.internal_name = 'BatchImageResizer.exe',
        #self.legal_copyright = 'Copyright (C) 2012 Hibosoft Software',
        # self.legal_trademarks = None,
        #self.original_filename = 'BatchImageResizer.exe',
        #self.product_name = 'Hibosoft Batch Image Resizer',
        #self.product_version = '3.1.4.r20',
        # self.special_build = None,

################################################################
def pack_data_files(src, dest):
    data_dir = []
    for f in os.listdir(src):
        f1 = os.path.join(src, f)
        if os.path.isfile(f1):
            data_dir.append((dest, [f1]))
        elif os.path.isdir(f1):
            new_desc = os.path.join(dest, f)
            data_dir += pack_data_files(f1, new_desc)
    return data_dir

PROGRAM_DIR = os.path.dirname(__file__)

data_files = []
# add folder
# for folder_name in ("key-gen-confs", "keys",):
#    folder_path = os.path.join(PROGRAM_DIR, folder_name)
#    data_files += pack_data_files(folder_path, folder_name)

# add file
for file_name in ("msvcp90.dll", "lang_zh_CN.qm", "click.wav"):
    data_files.append(('.', [os.path.join(PROGRAM_DIR, file_name),]))

BatchImageResizer = Target(
    decription = 'Hibosoft Batch Image Resizer',

    # what to build
    script = "main.py",
    icon_resources = [(1, "icon.ico")],
    dest_base = "BatchImageResizer")

setup(
        name = 'BatchImageResizer',
        version = "3.2",
        description = "A Batch Image Resizer App",
        author = "Hibosoft Software",
        data_files = data_files,
        options = {"py2exe": {"compressed": 1,
                              "optimize": 2,
                              "ascii": 0,
                              #"bundle_files": 1, #create a single exe file
                              "bundle_files": 3,
                              "excludes": excludes,
                              "includes":["sip"]}},
        zipfile = None, #don't create library.zip
        # console = [{"script": 'main.py', 'icon_resources': [(0, 'ICON.ico')]} ],
        windows = [BatchImageResizer],
    )
