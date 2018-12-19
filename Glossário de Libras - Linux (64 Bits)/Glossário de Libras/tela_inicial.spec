# -*- mode: python -*-

block_cipher = None


a = Analysis(['tela_inicial.py'],
             pathex=['C:\\Users\\Assuncao\\Desktop\\glossario'],
             binaries=[('opencv_ffmpeg344.dll', '.')],
             datas=[
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.py', '.'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.ui', '.'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\Assistant', 'Assistant'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\botoes-barra-lateral', 'botoes-barra-lateral'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.png', '.'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.htm', '.'),
			#('C:\\Users\\Assuncao\\Desktop\\glossario\\*.zip', '.'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.chm', '.'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.hhp', '.'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.hhc', '.'),
			('C:\\Users\\Assuncao\\Desktop\\glossario\\*.ttf', '.'),
		    ],
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
          [],
          name='tela_inicial',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
