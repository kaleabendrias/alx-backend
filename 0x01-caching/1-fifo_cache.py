#!/usr/bin/env python3
"""base_cache calss"""
base_caching = __import__("base_caching").BaseCaching


from collections import deque

class FIFOCache(base_caching):
    """Fifo cache"""
    def __init__(self):
        """init func"""
        super().__init__()
        self.key_queue = deque()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            removed_key = self.key_queue.popleft()
            del self.cache_data[removed_key]
            print("DISCARD:", removed_key)
        self.cache_data[key] = item
        self.key_queue.append(key)

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

