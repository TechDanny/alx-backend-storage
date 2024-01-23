#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    get_topics = mongo_collection.find({"topics": topic})
    documents = [x for x in get_topics]
    return documents