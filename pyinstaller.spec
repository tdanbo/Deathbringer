# -*- mode: python ; coding: utf-8 -*-
import os
import sys

site_packages = next(p for p in sys.path if "site-packages" in p)
print(site_packages)
block_cipher = None

# SCRIPTNAME
scriptname = os.path.basename(os.getcwd())

data_list = []

# IF YOU RUN PYSBS ENABLE THIS SECTION
# site_packages = next(p for p in sys.path if 'site-packages' in p)
# data_list.append((os.path.join(site_packages,"pysbs"),"pysbs"))

# WILL ORGANISE ICONS TO DIST FOLDER
icon_root = "src\\.icons"
json_root = "src\\.json"
file_root = "src\\.files"
items_root = "src\\.items"
feats_root = "src\\.feats"

for data_root in [icon_root, json_root, file_root,items_root,feats_root]:
    for root, dirs, files in os.walk(data_root, topdown=False):
        for name in files:
            icon_path = os.path.join(root, name)
            data_list.append((icon_path, os.path.basename(data_root)))

a = Analysis(
    ["src\\run.pyw"],
    pathex=[],
    binaries=[],
    datas=data_list,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=True,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=scriptname,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    icon="src\\.icons\\app_icon.ico",
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
