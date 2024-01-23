#!/usr/bin/env python3
"""
List all documents in Python
"""


def list_all(mongo_collection):
    """
    lists all documents in a collectio
    """
    data = mongo_collection.find()
    if data.count() == 0:
        return []
    return data
