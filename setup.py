#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name = "ascii_py",
    version = "2.0",
    description = "Make ascii art",
    # This is because shutil.get_terminal_size() was added in 3.3
    python_requires=">=3.5",
    author = "ProfOak",
    author_email = "OpenProfOak@gmail.com",
    url = "https://www.github.com/ProfOak/Ascii_py/",
    license = "MIT",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Programming Language :: Python :: 3",
    ],
    keywords = "ascii art image fun memes",
    install_requires = [
        "colorama==0.4.4",
        "Pillow==8.0.1",
    ],
    packages = find_packages(exclude=["Media"]),
    scripts=["bin/ascii_py"],
)
