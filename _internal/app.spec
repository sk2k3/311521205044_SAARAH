# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\app.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\app.spec', '.'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\facial_recognition.py', '.'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\upload_status.json', '.'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\attendance_records', 'attendance_records/'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\encodings', 'encodings/'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\models', 'models/'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\static', 'static/'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\templates', 'templates/'), ('C:\\Users\\user\\PycharmProjects\\attendance_system - Copy\\uploads', 'uploads/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)
