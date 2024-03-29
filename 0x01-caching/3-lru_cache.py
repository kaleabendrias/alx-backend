#!/usr/bin/env python3
"""LRUCache that inherits from BaseCaching and is a caching system"""
base_caching = __import__("base_caching").BaseCaching


class LRUCache(base_caching):
    """class LRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """put method"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            discarded_key = self.lru_list.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))
        self.cache_data[key] = item
        if key in self.lru_list:
            self.lru_list.remove(key)
        self.lru_list.append(key)

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.lru_list:
            self.lru_list.remove(key)
        self.lru_list.append(key)
        return self.cache_data[key]
