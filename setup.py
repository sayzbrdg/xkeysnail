#!/usr/bin/env python

import sys
from setuptools import setup
exec(open("xkeysnail/info.py").read())

_scripts = ["bin/xkeysnail"]
_requires = ["evdev", "python-xlib", "appdirs"]

if sys.platform.startswith('freebsd'):
    _scripts.append("bin/snailnotifier")
else:
    _requires.append("inotify_simple")

setup(name             = "xkeysnail",
      version          = __version__,
      author           = "Masafumi Oyamada",
      url              = "https://github.com/mooz/xkeysnail",
      description      = __description__,
      long_description = __doc__,
      packages         = ["xkeysnail"],
      scripts          = _scripts,
      license          = "GPL",
      install_requires = _requires
      )
