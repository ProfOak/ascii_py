#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name = 'ascii_py_gui',
    version = '1.2',
    description = 'Make ascii art',

    author = 'ProfOak',
    author_email = 'OpenProfOak@gmail.com',
    url = 'https://www.github.com/ProfOak/Ascii_py/',
    license = 'MIT',

    classifiers = [
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',
        'Topic :: Games/Entertainment',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Editors',

        # This is because shutil.get_terminal_size() was added in 3.3
        # the pypi version of  PySide is not compatible with Python 3.5
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords = 'ascii art image fun memes',

    install_requires = [
        'colorama',
        'Pillow',
        'PySide',
    ],
    packages = find_packages(exclude=['Media','ascii_py']),

    entry_points = {
        'console_scripts': [
            'ascii_py_gui = ascii_py_gui.main:main'
        ]
    },
)
