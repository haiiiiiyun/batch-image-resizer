# -*- mode: python -*-
base_folder = os.path.normpath("E:/workspace/batch-image-resizer")
program_name = "BatchImageResizer"
a = Analysis([os.path.join(base_folder, 'main.py')],
             pathex=[base_folder],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
version_file = os.path.join(base_folder, "setup", "version.txt")
icon_file = os.path.join(base_folder, "setup", "icon.ico")
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.win32/main', program_name + '.exe'),
          debug=True,
          strip=None,
          upx=False,
          console=True , version=version_file, icon=icon_file)

# add folder
# for folder_name in ("key-gen-confs", 
#   "keys",):
#   a.datas += Tree(os.path.join(base_folder, folder_name), folder_name)

# add file
for file_name in ("click.wav", "lang_zh_CN.qm", ):
    a.datas += [(file_name, os.path.join(base_folder, file_name), "DATA"),]

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=False,
               name=os.path.join('dist', 'main'))
app = BUNDLE(coll,
             name=os.path.join('dist', program_name + '.app'))
