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
                lfu_keys = [k for k, v in self.cache_data.items()
                            if self.frequency.get(k, 0) == min_frequency]

                if lfu_keys:
                    lru_key = min(lfu_keys, key=lambda k: self.access_time - self.frequency.get(k, 0))
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD: {}".format(lru_key))
                else:
                    pass
        self.cache_data[key] = item
        self.access_time += 1
        self.frequency[key] = self.access_time

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        self.access_time += 1
        self.frequency[key] = self.access_time
        return self.cache_data[key]
