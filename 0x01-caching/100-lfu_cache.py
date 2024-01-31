#!/usr/bin/python3
"""lifo cache"""
import base_caching  # Explicit import for clarity


class LFUCache(base_caching.BaseCaching):
    """A Least Frequently Used (LFU) caching system."""

    def __init__(self):
        super().__init__()
        self.keys_to_frequencies = {}  # Map keys to their access frequencies

    def put(self, key, item):
        """
        Adds an item to the cache.
        """
        if key and item:
            current_value = self.get(key)
            if current_value != item:  # Only update if value has changed
                self.cache_data[key] = item
                self.keys_to_frequencies[key] = 1

                # Evict if cache is full
                if self.is_full():
                    self.evict_lru()
            else:
                # Update frequency even if value is the same
                self.update_frequency(key)

    def get(self, key):
        """Retrieves an item from the cache and updates its frequency."""
        value = self.cache_data.get(key, None)
        if value:
            self.update_frequency(key)
        return value

    def update_frequency(self, key):
        """Increments the access frequency of a key."""
        self.keys_to_frequencies[key] += 1

    def evict_lru(self):
        """Evicts the least frequently used item from the cache."""
        least_frequent_key = min(self.keys_to_frequencies,
                                 key=self.keys_to_frequencies.get)
        print(f"DISCARD: {least_frequent_key}")
        self.cache_data.pop(least_frequent_key)
        self.keys_to_frequencies.pop(least_frequent_key)

    def is_full(self):
        """Returns True if the cache is full, False otherwise."""
        return len(self.cache_data) >= self.MAX_ITEMS
