#!/usr/bin/env python3
"""
Writing strings to Redis
"""


from typing import Union
import uuid
import redis


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
