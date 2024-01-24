#!/usr/bin/env python3
"""
Writing strings to Redis
"""


from typing import Union, Callable
import uuid
import redis
from functools import wraps


class Cache:
    '''
    creating a class cache
    '''
    def __init__(self):
        """
        stores an instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Returns a callable
        """
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            Output for each function
            """
            self._redis.incr(key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates random keys
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) -> Union[str, bytes,
                                                          int, float, None]:
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> Union[str, None]:
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        return self.get(key, fn=int)
