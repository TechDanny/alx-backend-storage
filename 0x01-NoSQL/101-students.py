#!/usr/bin/env python3
"""
Top student
"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student