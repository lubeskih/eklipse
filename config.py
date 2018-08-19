DEBUG = False
SQLALCHEMY_ECHO = False

import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URL = 'sqlite:///' + \
os.path.join(basedir, 'eklipse/database/database.sqlite')
