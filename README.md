# Flask-Cache-Redis-Cluster
[![PyPI version](https://img.shields.io/pypi/v/Flask-Cache-Redis-Cluster.svg)](https://pypi.python.org/pypi/Flask-Cache-Redis-Cluster)
[![Travis CI](https://travis-ci.org/Richard-Mathie/Flask-Cache-Redis-Cluster.svg?branch=master)](https://travis-ci.org/Richard-Mathie/Flask-Cache-Redis-Cluster)
[![Code Climate](https://codeclimate.com/repos/58ecbc857705a10265000f28/badges/8b2c22252025de68ce4d/gpa.svg)](https://codeclimate.com/repos/58ecbc857705a10265000f28/feed)
[![Test Coverage](https://codeclimate.com/repos/58ecbc857705a10265000f28/badges/8b2c22252025de68ce4d/coverage.svg)](https://codeclimate.com/repos/58ecbc857705a10265000f28/coverage)

Implements a redis cluster backend for [Flask-Cache(ing)](https://pythonhosted.org/Flask-Cacheing/#custom-cache-backends)
as the standard redis cache cannot handle a redis cluster.

## Usage

```python
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
```

## Links
* [Flask-Caching Documentation](https://pythonhosted.org/Flask-Caching/)
* [Original Flask-Cache Extension](https://github.com/thadeusb/flask-cache)
* [Werkzeug Cache](http://werkzeug.pocoo.org/docs/0.11/contrib/cache/)
* [redis-py-cluster](http://redis-py-cluster.readthedocs.io/)

