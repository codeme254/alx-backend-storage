#!/usr/bin/env python3
"""
List all documents in a collection in mongodb using py
"""


def list_all(mongo_collection):
    """
    List all documents in a collection in mongodb with py
    """
    return [document for document in mongo_collection.find()]
