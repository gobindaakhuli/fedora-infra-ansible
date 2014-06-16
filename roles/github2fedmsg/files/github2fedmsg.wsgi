import sys
sys.stdout = sys.stderr

import __main__
__main__.__requires__ = __requires__ = ["github2fedmsg", "sqlalchemy>=0.8"];
import pkg_resources
pkg_resources.require(__requires__)

import os
os.environ['PYTHON_EGG_CACHE'] = '/var/www/.python-eggs'

from pyramid.paster import get_app, setup_logging
ini_path = '/etc/github2fedmsg/github2fedmsg.ini'
setup_logging(ini_path)

application = get_app(ini_path, 'main')
