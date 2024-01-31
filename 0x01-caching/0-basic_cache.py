#!/usr/bin/env python3
"""base_cache calss"""
base_caching = __import__("base_caching").BaseCaching


class BasicCache(base_caching):
    """class basic caching"""
    def __init__(self):
        """init method"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """method get"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key, None)

