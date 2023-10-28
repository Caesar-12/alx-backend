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

        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                return
            else:
                for keys in self.cache_data.keys():
                    rem_key = keys
                    del self.cache_data[keys]
                    break
                print("DICARD: {}".format(rem_key))
        self.cache_data[key] = item

    def get(self, key):
        """Simple retrieve cache method"""
        try:
            return self.cache_data[key]
        except KeyError:
            return None
