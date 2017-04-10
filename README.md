# Flask-Cache-Redis-Cluster
This implements a redis cluster backend for [Flask-Cache(ing)](https://pythonhosted.org/Flask-Cache/#custom-cache-backends)
as the standard redis cache cannot handle a redis cluster.

## Usage

```
class Config(object):

    CACHE_TYPE = 'flask_cache_redis_cluster.rediscluster'
    CACHE_REDIS_HOST = 'redis'
    CACHE_REDIS_PORT = 6379
    CACHE_KEY_PREFIX = '<your prefix>'
    # ... other options
```
