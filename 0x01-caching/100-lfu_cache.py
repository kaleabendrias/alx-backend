#!/usr/bin/python3
"""LFUCache that inherits from BaseCaching and is a caching system"""
base_caching = __import__("base_caching").BaseCaching


class LFUCache(base_caching):
    """LFUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.frequency = {}
        self.access_time = 0

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            if key not in self.cache_data:
                min_frequency = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_frequency]

                lru_key = min(lfu_keys, key=lambda k: self.frequency.get(k, 0))
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD: {}".format(lru_key))
        self.cache_data[key] = item
        if key not in self.frequency:
            self.frequency[key] = 0

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        return self.cache_data[key]
