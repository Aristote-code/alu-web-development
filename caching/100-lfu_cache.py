#!/usr/bin/python3
""" LFU Caching """

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFU Cache class with LRU tie-breaker """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = {}
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the item and increase frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()
            # Add the new item with initial frequency 1
            self.cache_data[key] = item
            self.frequency[key] = 1
        # Update usage order
        self.usage_order[key] = None
        self.usage_order.move_to_end(key)

    def get(self, key):
        """ Retrieve an item by key """
        if key is None or key not in self.cache_data:
            return None
        # Increment frequency and update usage order
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

    def _evict(self):
        """
        Evict the least frequently used item.
        If there's a tie, evict the least recently used item among them.
        """
        # Find the minimum frequency among all keys
        min_freq = min(self.frequency.values())
        # Identify keys with the minimum frequency
        min_freq_keys = [
            k for k in self.usage_order if self.frequency[k] == min_freq
        ]
        # The first key in usage_order among min_freq_keys is the LRU
        discard_key = min_freq_keys[0]
        # Remove the item from all tracking structures
        del self.cache_data[discard_key]
        del self.frequency[discard_key]
        del self.usage_order[discard_key]
        print(f"DISCARD: {discard_key}")

    def print_cache(self):
        """ Print the current cache """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
