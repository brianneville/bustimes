# -*- mode: python -*-
import pygame
from kivy.deps import sdl2
from kivy import kivy_data_dir
from kivy.tools.packaging import pyinstaller_hooks as hooks

# kivy_deps_all = hooks.get_deps_all()
# kivy_factory_modules = hooks.get_factory_modules()

block_cipher = None

bin = [Tree(p) for p in sdl2.dep_bins]

a = Analysis(['UI.py'],
             pathex=['C:\\Users\\Brian\\PycharmProjects\\bustimes'],
             binaries=None,
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          *bin,
          name='UI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
