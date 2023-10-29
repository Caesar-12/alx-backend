#!/usr/bin/env python3
"""Contains the child class LRUCcache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A child class of BaseCaching that uses the LRU algorithm"""

    def __init__(self):
        self.key_order = []
        super().__init__()

    def put(self, key, item):
        """Modified put method"""

        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.key_order.remove(key)
                self.key_order.append(key)
                return
            else:
                self.cache_data.pop(self.key_order[-1])
                print("DISCARD: {}".format(self.key_order[-1]))
                self.key_order.pop(-1)
        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """Simple retrieve cache method"""
        try:
            if key in self.key_order:
                self.key_order.remove(key)
                self.key_order.append(key)
            return self.cache_data[key]
        except KeyError:
            return None
