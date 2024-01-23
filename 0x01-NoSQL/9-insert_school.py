#!/usr/bin/env python3
"""
Insert document in python
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    data_id = mongo_collection.insert(kwargs)
    return data_id
