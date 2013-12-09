# -*- mode: python -*-
a = Analysis(['BorderlessStone.py'],
             pathex=['C:\\Users\\Miguel\\Documents\\BorderlessStone\\BorderlessStone'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='BorderlessStone.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
