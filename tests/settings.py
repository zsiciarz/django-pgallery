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
    'django.contrib.postgres',
    'django.contrib.sessions',
    'django.contrib.messages',
    'markitup',
    'pgallery',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

SECRET_KEY = 'notreallyasecret'

ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
        },
    },
]

MEDIA_ROOT = project_path('media')

STATIC_URL = '/static/'

MARKITUP_FILTER = ('markdown.markdown', {'extensions': ['markdown.extensions.codehilite']})

MARKITUP_SET = 'markitup/sets/markdown'
