#!/usr/bin/env python3
"""MRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize MRUCache"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = next(iter(self.cache_data))
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)

            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
