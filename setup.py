#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='britney-cookies',
    version='0.1',
    author='Arnaud Grausem',
    author_email='arnaud.grausem@gmail.com',
    maintainer='Arnaud Grausem',
    maintainer_email='arnaud.grausem@gmail.com',
    url='https://github.com/agrausem/britney-cookies',
    license='PSF',
    description='Session-based cookie middleware for britney',
    long_description=long_description,
    py_modules=['britney_cookies'],
    download_url='http://pypi.python.org/pypi/britney-cookies',
    install_requires=['britney'],
    keywords=['SPORE', 'REST Api', 'authentication', 'britney', 'cookie'],
    entry_points={
        'britney.plugins.middleware': [
            'Cookie = britney_cookies:Cookie'
        ]
    },
    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    )
)
