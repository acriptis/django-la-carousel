#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

try:
    README = open('README.md').read()
except:
    README = None

try:
    REQUIREMENTS = open('requirements.txt').read()
except:
    REQUIREMENTS = None

setup(
    name='django-la-carousel',
    version="v0.1.0",
    description=(
        'Django app for a simple carousel management'
    ),
    long_description=README,
    install_requires=REQUIREMENTS,
    author='Fábio Piovam Elias',
    author_email='fabio@laborautonomo.org',
    url='https://github.com/laborautonomo/django-la-carousel/',
    packages=find_packages(),
    include_package_data=True,
)