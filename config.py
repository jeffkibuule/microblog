import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
	ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
	GOOGLE_TRANSLATOR_KEY = os.environ.get('GOOGLE_TRANSLATOR_KEY')

	ADMINS = os.environ.get('ADMINS').split(',')
	LANGUAGES=['en', 'es']

	POSTS_PER_PAGE = 25