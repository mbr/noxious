#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='noxious',
    version='0.1.dev1',
    description='An XML parser for people that hate XML.',
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='https://github.com/mbr/noxious',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ])
