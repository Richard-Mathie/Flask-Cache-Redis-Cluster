from flask import Flask
from flask_caching import Cache

class Config(object):
    CACHE_TYPE = 'flask_cache_redis_cluster.rediscluster'
    CACHE_REDIS_HOST = 'redis'
    CACHE_REDIS_PORT = 6379
    CACHE_KEY_PREFIX = 'flask_cache_redis_cluster_test'

app = Flask(__name__)
cache = Cache()


def test_load():
    app.config.from_object(Config)
    cache.init_app(app)

