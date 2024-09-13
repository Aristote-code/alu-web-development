#!/usr/bin/python3
""" LFU Caching """

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """ LFU Cache class with LRU tie-breaker """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = defaultdict(int)  # Tracks frequency of each key
        self.usage_order = OrderedDict()   # Tracks the order of usage (LRU)
    
    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            # Update existing item, increment its frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict()
            # Add new item with initial frequency of 1
            self.cache_data[key] = item
            self.frequency[key] = 1
        
        # Update usage order to reflect the recent usage of the key
        if key in self.usage_order:
            del self.usage_order[key]
        self.usage_order[key] = None  # Insert or move key to the end

    def get(self, key):
        """ Retrieve an item by key """
        if key is None or key not in self.cache_data:
            return None
        
        # Increment frequency and update usage order
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

    def _evict(self):
        """ Evict the least frequently used item. If tie, evict LRU """
        # Find the minimum frequency among the items
        min_freq = min(self.frequency.values())
        # Find all keys with this minimum frequency
        min_freq_keys = [k for k in self.usage_order if self.frequency[k] == min_freq]

        # Evict the least recently used among the keys with minimum frequency
        discard_key = min_freq_keys[0]
        del self.cache_data[discard_key]
        del self.frequency[discard_key]
        del self.usage_order[discard_key]
        print(f"DISCARD: {discard_key}")

    def print_cache(self):
        """ Print the current cache """
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")
