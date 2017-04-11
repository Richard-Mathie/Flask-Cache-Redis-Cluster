Flask-Cache-Redis-Cluster
=========================

|PyPI version| |Travis CI| |Code Climate| |Test Coverage|

Implements a redis cluster backend for
`Flask-Cache(ing) <https://pythonhosted.org/Flask-Cacheing/#custom-cache-backends>`__
as the standard redis cache cannot handle a redis cluster.

Usage
-----

.. code:: python

    from flask import Flask
    from flask_caching import Cache
    app = Flask(__name__)


    class Config(object):

        CACHE_TYPE = 'flask_cache_redis_cluster.rediscluster'
        CACHE_REDIS_HOST = 'redis'
        CACHE_REDIS_PORT = 6379
        CACHE_KEY_PREFIX = '<your prefix>'
        # ... other options


    app.config.from_object(Config)
    cache = Cache(app)

Links
-----

-  `Flask-Caching
   Documentation <https://pythonhosted.org/Flask-Caching/>`__
-  `Original Flask-Cache
   Extension <https://github.com/thadeusb/flask-cache>`__
-  `Werkzeug
   Cache <http://werkzeug.pocoo.org/docs/0.11/contrib/cache/>`__
-  `redis-py-cluster <http://redis-py-cluster.readthedocs.io/>`__

.. |PyPI version| image:: https://img.shields.io/pypi/v/Flask-Cache-Redis-Cluster.svg
   :target: https://pypi.python.org/pypi/Flask-Cache-Redis-Cluster
.. |Travis CI| image:: https://travis-ci.org/Richard-Mathie/Flask-Cache-Redis-Cluster.svg?branch=master
   :target: https://travis-ci.org/Richard-Mathie/Flask-Cache-Redis-Cluster
.. |Code Climate| image:: https://codeclimate.com/repos/58ecbc857705a10265000f28/badges/8b2c22252025de68ce4d/gpa.svg
   :target: https://codeclimate.com/repos/58ecbc857705a10265000f28/feed
.. |Test Coverage| image:: https://codeclimate.com/repos/58ecbc857705a10265000f28/badges/8b2c22252025de68ce4d/coverage.svg
   :target: https://codeclimate.com/repos/58ecbc857705a10265000f28/coverage
