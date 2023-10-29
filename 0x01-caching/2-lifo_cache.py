#!/usr/bin/env python3

"""Child class of BaseCaching class"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Contains modified methods put and get"""

    def __init__(self):
        """Concstructor"""
        self.last_in = None
        super().__init__()

    def put(self, key, item):
        """Modified put method"""

        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.last_in = key
                return
            else:
                self.cache_data.pop(self.last_in)
                print("DISCARD: {}".format(self.last_in))
        self.cache_data[key] = item
        self.last_in = key

    def get(self, key):
        """Simple retrieve cache method"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
