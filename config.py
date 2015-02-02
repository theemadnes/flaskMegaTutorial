import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_user = os.environ['DBUSER']
db_password = os.environ['DBPASS']
db_path = os.environ['DBPATH']
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + db_user + ':' + db_password + '@' + db_path
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']

WTF_CSRF_ENABLED = True
SECRET_KEY = 'this is my secret key'
POSTS_PER_PAGE = 3

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]