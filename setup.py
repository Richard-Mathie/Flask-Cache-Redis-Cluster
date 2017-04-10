#!/usr/bin/env python
"""
Flask-Cache-Redis-Cluster
=============
Implements a redis cluster backend for Flask-Cache(ing)
as the standard redis cache cannot handle a redis cluster.

Usage
-----
The redis cluster backend can be imported vire the Cache Extension by:
.. code:: python
    from flask import Flask
    from flask_caching import Cache
    app = Flask(__name__)
    # For more configuration options, check out the documentation
    cache = Cache(app, config={'CACHE_TYPE': 'flask_cache_redis_cluster.rediscluster'})
Links
=====
* `Documentation <https://pythonhosted.org/Flask-Caching/>`_
* `Original Flask-Cache Extension <https://github.com/thadeusb/flask-cache>`_
* `Werkzeug Cache <http://werkzeug.pocoo.org/docs/0.11/contrib/cache/>`_
"""
from setuptools import setup, find_packages

with open('Version', 'rb') as f:
    version = f.read().strip().decode('utf-8')


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
    install_requires=[
        'werkzeug',
        'redis-py-cluster'
    ],
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
