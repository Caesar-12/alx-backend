#!/usr/bin/env python3
"""Contains the child class LFUCcache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A child class of BaseCaching that uses the LFU algorithm"""

    def __init__(self):
        self.key_order = []
        self.key_freq = {}
        super().__init__()

    def put(self, key, item):
        """Modified put method"""

        if not key or not item:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.key_order.remove(key)
                self.key_order.insert(0, key)
                self.key_freq[key] += 1
                return
            else:
                sorted_keys = []
                least_count = 0
                for k, v in self.key_freq.items():
                    sorted_keys.append((k,v))
                sorted_keys.sort()
                for freq in sorted_keys:
                    if freq[1] == sorted_keys[0][1]:
                        least_count += 1
                if least_count == 1:
                    self.cache_data.pop(sorted_keys[0][0])
                    print("DISCARD: {}".format(sorted_keys[0][0]))
                    self.key_order.pop(-1)
                else:
                    l_index = []
                    for j in range(least_count):
                        for i in range(-1, -(len(self.cache_data)), -1):
                            if sorted_keys[j][0] == self.key_order[i]:
                                l_index.append(i)
                                continue
                    l_index.sort()
                    self.cache_data.pop(self.key_order[l_index[0]])
                    print("DISCARD: {}".format(self.key_order[l_index[0]]))
                    self.key_order.pop(l_index[0])
        self.cache_data[key] = item
        self.key_freq[key] = 1
        self.key_order.insert(0, key)

    def get(self, key):
        """Simple retrieve cache method"""
        try:
            if key in self.key_order:
                self.key_order.remove(key)
                self.key_order.insert(0, key)
                self.key_freq[key] += 1
            return self.cache_data[key]
        except KeyError:
            return None
