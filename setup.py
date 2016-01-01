import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-anonsurvey3',
    version='0.3.1',
    packages=['anonsurvey3'],
    include_package_data=True,
    license='GPLv3',
    description='A Django app to create Web-based anonymous surveys',
    long_description=README,
    install_requires=["django-tinymce", "Django-tinymce-filebrowser"],
    url='https://github.com/boltomli/django-anonsurvey',
    author='Darko Poljak, Song Li',
    author_email='darko.poljak@gmail.com; songl@outlook.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
