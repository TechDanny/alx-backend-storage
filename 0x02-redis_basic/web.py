#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""


import redis
import requests
from functools import wraps
from typing import Callable


redisClient = redis.Redis()


def count_and_cache(method):
    """
    counts total time of url accessed
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        cached_key = "cached:" + url
        cached_data = redisClient.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url

        text = method(url)

        redisClient.incr(count_key)
        redisClient.set(cached_key, text)
        redisClient.expire(cached_key, 10)
        return text
    return wrapper


@count_and_cache
def get_page(url: str) -> str:
    """
    track how many times a particular URL was accessed in the key
    """
    rslt = requests.get(url)
    return rslt.text
