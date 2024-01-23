#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    topics = mongo_collection.find({"topic": topic})
    documents = [x for x in topics]
    return documents