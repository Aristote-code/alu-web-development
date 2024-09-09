#!/usr/bin/python3
"""LFU cache"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0
        self.frequency_list = {}

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            self._evict()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1
            if 1 not in self.frequency_list:
                self.frequency_list[1] = []
            self.frequency_list[1].append(key)
        else:
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1
            if 1 not in self.frequency_list:
                self.frequency_list[1] = []
            self.frequency_list[1].append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Update frequency of an item"""
        freq = self.frequency[key]
        self.frequency[key] += 1
        self.frequency_list[freq].remove(key)
        if not self.frequency_list[freq]:
            del self.frequency_list[freq]
            if freq == self.min_frequency:
                self.min_frequency += 1
        if freq + 1 not in self.frequency_list:
            self.frequency_list[freq + 1] = []
        self.frequency_list[freq + 1].append(key)

    def _evict(self):
        """Evict the least frequently used item"""
        lfu_key = self.frequency_list[self.min_frequency].pop(0)
        if not self.frequency_list[self.min_frequency]:
            del self.frequency_list[self.min_frequency]
        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        print(f"DISCARD: {lfu_key}")