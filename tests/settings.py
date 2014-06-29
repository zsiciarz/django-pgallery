import os


def project_path(path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), path))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pgallery',
        'USER': os.environ.get('DATABASE_USER', 'pgallery'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', 'pgallery'),
        'HOST': 'localhost',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'markitup',
    'sorl.thumbnail',
    'pgallery',
)

SECRET_KEY = 'notreallyasecret'

MEDIA_ROOT = project_path('media')

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False, 'extensions': ['codehilite']})

MARKITUP_SET = 'markitup/sets/markdown'
