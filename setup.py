#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name = 'ascii_py',
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
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords = 'ascii art image fun memes',

    install_requires = [
        'colorama',
        'Pillow',
    ],
    packages = find_packages(exclude=['Media','ascii_py_gui']),

    entry_points = {
        'console_scripts': [
            'ascii_py = ascii_py.main:main'
        ]
    },
)
