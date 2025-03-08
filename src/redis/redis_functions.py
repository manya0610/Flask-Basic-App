from functools import wraps
from typing import Any

import redis
from src.redis import redis_client


def redis_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except redis.RedisError as e:
            print(f"Redis error in {func.__name__}: {e}")
            raise e

    return wrapper


class RedisFunctions:
    @staticmethod
    @redis_error_handler
    def get_message_key(key: str) -> str:
        return f"message:#{key}"

    @staticmethod
    @redis_error_handler
    def hsetex(key: str, payload: dict, ttl: int = 1800):
        pipeline = redis_client.pipeline()
        key = RedisFunctions.get_message_key(key)
        pipeline.hset(name=key, mapping=payload)
        pipeline.expire(key, time=ttl)
        return pipeline.execute()

    @staticmethod
    @redis_error_handler
    def hgetall(key: str) -> dict:
        message: dict = redis_client.hgetall(name=RedisFunctions.get_message_key(key))
        return message

    @staticmethod
    @redis_error_handler
    def exists(key: str) -> bool:
        key_in_redis: bool = bool(
            redis_client.exists(RedisFunctions.get_message_key(key))
        )
        return key_in_redis

    @staticmethod
    @redis_error_handler
    def get(key: str) -> str:
        return redis_client.get(RedisFunctions.get_message_key(key))

    @staticmethod
    @redis_error_handler
    def set(key: str, value: Any) -> str:
        return redis_client.set(RedisFunctions.get_message_key(key), value)

    @staticmethod
    @redis_error_handler
    def incr(key: str, amount: int = 1):
        return redis_client.incr(RedisFunctions.get_message_key(key), amount)

    @staticmethod
    @redis_error_handler
    def expire(key: str, seconds: int):
        return redis_client.expire(RedisFunctions.get_message_key(key), seconds)

    @staticmethod
    @redis_error_handler
    def delete(key: str):
        return redis_client.delete(RedisFunctions.get_message_key(key))
