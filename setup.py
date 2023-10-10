from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["pytube", "PySide6", "os"], 'excludes': [""], 'include_files': ['logo-transparent.ico']}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'YTDownloader', icon="logo-transparent.ico",)
]

setup(name='YT Downloader',
      version = '1.4.0',
      description = 'Convert & download Youtubevideo URLs to MP3.',
      copyright='Copyright (C) 2023 S3R43o3',
      options = {'build_exe': build_options},
      executables = executables)
