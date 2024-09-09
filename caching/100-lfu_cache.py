#!/usr/bin/python3
"""LFU cache"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """LFU cache"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = []

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            self._discard_least_frequent()

        self.cache_data[key] = item
        self.frequency[key] += 1
        self._update_usage_order(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self._update_usage_order(key)
        return self.cache_data[key]

    def _discard_least_frequent(self):
        """Discard the least frequently used item"""
        min_freq = min(self.frequency.values())
        least_frequent = [k for k in self.usage_order if self.frequency[k] == min_freq]

        discard_key = least_frequent[0]
        del self.cache_data[discard_key]
        del self.frequency[discard_key]
        self.usage_order.remove(discard_key)
        print("DISCARD:", discard_key)

    def _update_usage_order(self, key):
        """Update the usage order of items"""
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)