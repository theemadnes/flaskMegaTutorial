# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_user = os.environ['DBUSER']
db_password = os.environ['DBPASS']
db_path = os.environ['DBPATH']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + db_user + ':' + db_password + '@' + db_path
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
'''MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None'''
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

# administrator list
ADMINS = ['alex.mattson@gmail.com']

WTF_CSRF_ENABLED = True
SECRET_KEY = 'this is my secret key'
POSTS_PER_PAGE = 3
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]