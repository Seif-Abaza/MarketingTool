# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('./marketing.py', 'MarketTools'), ('./requirements.txt', 'MarketTools'), ('./Classes', 'MarketTools/Classes'), ('./Facebook', 'MarketTools/Facebook'), ('./Interface', 'MarketTools/Interface'), ('./locat', 'MarketTools/locat'), ('./Telegram', 'MarketTools/Telegram'), ('./utils', 'MarketTools/utils'), ('./WhatsApp', 'MarketTools/WhatsApp'), ('./Sessions', 'MarketTools/Sessions'), ('./Log', 'MarketTools/Log')]
binaries = []
hiddenimports = []
tmp_ret = collect_all('PySide6')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)
splash = Splash(
    './images/8596d749-a292-4389-9bd9-bc6795a4c7de.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    splash,
    splash.binaries,
    [],
    name='MarketMiner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=True,
    argv_emulation=False,
    target_arch='x86_64',
    codesign_identity=None,
    entitlements_file=None,
    icon=['images/MM_Logo.ico'],
    hide_console='hide-early',
)
