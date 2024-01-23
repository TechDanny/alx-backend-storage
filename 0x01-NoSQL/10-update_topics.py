#!/usr/bin/env python3
"""
Change School topic
"""


def update_topics(mongo_collection, name, topics):
    """
    This function changes all topics of a school document based on the name
    """
    change_topic = mongo_collection.update_many({"name": name},
                                                {"$set": {"topics": topics}})
    return change_topic