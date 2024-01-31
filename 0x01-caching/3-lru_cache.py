#!/usr/bin/python3
"""LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize LRUCache"""
        super().__init__()
        self.lru_order = []

    def update_lru_order(self, key):
        """Update the LRU order with the most recent access"""
        if key in self.lru_order:
            self.lru_order.remove(key)
        self.lru_order.insert(0, key)

    def put(self, key, item):
        """Add an item in the cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.lru_order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            self.cache_data[key] = item
            self.update_lru_order(key)

    def get(self, key):
        """Get an item by key"""
        if key is not None and key in self.cache_data:
            self.update_lru_order(key)
            return self.cache_data[key]
        else:
            return None
