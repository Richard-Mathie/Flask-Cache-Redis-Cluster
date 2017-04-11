# Flask-Cache-Redis-Cluster

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

