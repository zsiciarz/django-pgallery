from django.conf import settings

if not settings.configured:
    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django_nose',
        'markitup',
        'sorl.thumbnail',
        'pgallery',
    )
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'pgallery',
                'USER': 'pgallery',
                'PASSWORD': 'pgallery',
                'HOST': 'localhost',
            }
        },
        INSTALLED_APPS=INSTALLED_APPS,
        MARKITUP_FILTER=('markdown.markdown', {'safe_mode': False, 'extensions': ['codehilite']}),
        MARKITUP_SET='markitup/sets/markdown',
    )


from django_nose import NoseTestSuiteRunner

test_runner = NoseTestSuiteRunner()
test_runner.run_tests(['pgallery'])
