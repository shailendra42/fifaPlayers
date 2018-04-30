import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'Name': os.path.join(BASSE_DIR, 'db.sqlite3'),
        
    }

}

DEBUG = True