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
    'django_hstore',
    'markitup',
    'sorl.thumbnail',
    'pgallery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = 'notreallyasecret'

MEDIA_ROOT = project_path('media')

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False, 'extensions': ['codehilite']})

MARKITUP_SET = 'markitup/sets/markdown'
