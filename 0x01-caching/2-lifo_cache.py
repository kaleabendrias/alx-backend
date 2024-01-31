#!/usr/bin/python3
"""lifo cache"""
from collections import deque
base_caching = __import__("base_caching").BaseCaching


class LIFOCache(base_caching):
    """class lifo caching"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        if (len(self.cache_data) >= self.MAX_ITEMS):
            removed_key, _ = self.cache_data.popitem()
            print("DISCARD:", removed_key)
        self.cache_data[key] = item

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
