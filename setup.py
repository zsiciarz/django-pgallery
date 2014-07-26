import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-pgallery',
    version=__import__('pgallery').__version__,
    description='Photo gallery app for PostgreSQL and Django.',
    long_description=read('README.rst'),
    author='Zbigniew Siciarz',
    author_email='zbigniew@siciarz.net',
    url='http://github.com/zsiciarz/django-pgallery',
    download_url='http://pypi.python.org/pypi/django-pgallery',
    license='MIT',
    install_requires=[
        'Django>=1.4',
        'Pillow',
        'psycopg2>=2.4',
        'django-markitup>=1.0',
        'django-model-utils>=1.1',
        'djorm-ext-core>=0.4.2',
        'djorm-ext-expressions>=0.4.4',
        'djorm-ext-hstore>=0.4.2',
        'djorm-ext-pgarray',
        'sorl-thumbnail>=11',
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
)
