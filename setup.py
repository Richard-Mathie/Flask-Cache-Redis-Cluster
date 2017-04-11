#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open('Version', 'rb') as f:
    version = next(f).strip().decode('utf-8')

with open('README.rst') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = [r for r in f]

__doc__ = readme

setup(
    name='Flask-Cache-Redis-Cluster',
    version=version,
    url='https://github.com/Richard-Mathie/Flask-Cache-Redis-Cluster',
    license='BSD',
    author='Richard Mathie',
    author_email='richard.mathie@cantab.net',
    description='Adds redis cluster caching support to the Flask Cache(ing) extension',
    long_description=__doc__,
    packages=['flask_cache_redis_cluster'],
    platforms='any',
    install_requires=requirements,
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)
