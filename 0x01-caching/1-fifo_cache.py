#!/usr/bin/env python3

"""Child class of BaseCaching class"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Contains modified methods put and get"""

    def __init__(self):
        """Concstructor"""
        super().__init__()

    def put(self, key, item):
        """Modified put method"""

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.cache_data.popitem(last=False)
            print("DICARD: {}".format(discarded[0]))
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Simple retrieve cache method"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None