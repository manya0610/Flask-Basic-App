import traceback
from urllib.parse import urlparse

import redis
from env import REDIS_DATABASE_INDEX, REDIS_POOL_MAX_CONNECTIONS, REDIS_URL
from redis import Redis


class RedisClient:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls._create_client()
        return cls._instance

    @classmethod
    def _create_client(cls):
        try:
            url = urlparse(REDIS_URL)
            pool = redis.ConnectionPool(
                host=url.hostname,
                port=url.port,
                username=url.username,
                password=url.password,
                decode_responses=True,
                max_connections=REDIS_POOL_MAX_CONNECTIONS,
                db=REDIS_DATABASE_INDEX,
            )
            return redis.Redis(connection_pool=pool)
        except Exception as e:
            print(e)
            traceback.print_exc()
            raise


redis_client: Redis = RedisClient.get_instance()
