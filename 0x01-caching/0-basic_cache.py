#!/usr/bin/env python3

"""Basic caching class methods"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """A child class Basecaching with simple cache methods"""

    def __init__(self):
        super().__init__(self, self.cache_data)

    def put(self, key, item):
        """Simple cache method to add an item"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Simple retrieve cache method"""
        if not key or not self.cache_data[key]:
            return None
        else:
            return self.cache_data[key]
