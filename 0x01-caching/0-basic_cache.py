#!/usr/bin/env python3

"""Basic caching class methods"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """A child class Basecaching with simple cache methods"""

    def put(self, key, item):
        """Simple cache method to add an item"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Simple retrieve cache method"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
