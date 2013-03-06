#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='treelogger4mongo',
    version='0.0.1',
    description='A logger that logs in a tree structure and saves in mongo',
    author='Jonatan Nilsson',
    author_email='jonatan@nilsson.is',
    url='https://github.com/TheThing/treelogger4mongo',
    long_description=open('readme.md', 'r').read(),
    packages=[
        'treelogger4mongo',
    ],
    requires=[
        'pymongo',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: WTFPL',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: System :: Logging',
    ],
)