#!/usr/bin/python3
"""MRUCache that inherits from BaseCaching and is a caching system"""
base_caching = __import__("base_caching").BaseCaching


class MRUCache(base_caching):
    """MRUCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """init method"""
        super().__init__()
        self.mru_list = []

    def put(self, key, item):
        """Put method"""
        if key is None or item is None:
            return
        if (len(self.cache_data) >= self.MAX_ITEMS):
            removed_key = self.mru_list.pop()
            del self.cache_data[removed_key]
            print("DISCARD: {}".format(removed_key))
        self.cache_data[key] = item
        if key in self.mru_list:
            self.mru_list.remove(key)
        self.mru_list.append(key)

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.mru_list:
            self.mru_list.remove(key)
        self.mru_list.append(key)
        return self.cache_data[key]