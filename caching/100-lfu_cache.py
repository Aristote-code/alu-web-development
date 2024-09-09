#!/usr/bin/python3
"""LFU cache"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """LFU (Least Frequently Used) cache implementation"""

    def __init__(self):
        """
        Initialize the LFU cache
        Calls the parent class constructor and sets up frequency and usage tracking
        """
        super().__init__()
        self.frequency = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache
        If the cache is full, remove the least frequently used item
        Args:
            key: The key to store the item under
            item: The item to store in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self._evict()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None
            self._update_frequency(key)

    def get(self, key):
        """
        Retrieve an item from the cache
        Args:
            key: The key of the item to retrieve
        Returns:
            The item if it exists in the cache, None otherwise
        """
        if key is None or key not in self.cache_data:
            return None
        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """
        Update the frequency and usage order of an item
        Args:
            key: The key of the item to update
        """
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)

    def _evict(self):
        """
        Evict the least frequently used item from the cache
        If there's a tie, remove the least recently used among the least frequent
        """
        min_freq = min(self.frequency.values())
        least_frequent = [k for k, v in self.frequency.items() if v == min_freq]

        if len(least_frequent) == 1:
            discard_key = least_frequent[0]
        else:
            discard_key = next(k for k in self.usage_order if k in least_frequent)

        del self.cache_data[discard_key]
        del self.frequency[discard_key]
        del self.usage_order[discard_key]
        print(f"DISCARD: {discard_key}")

    def print_cache(self):
        """Print the current state of the cache"""
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")