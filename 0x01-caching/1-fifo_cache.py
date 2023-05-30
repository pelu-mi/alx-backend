#!/usr/bin/env python3
""" Module for task 1
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Simple caching system
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_log = []

    def put(self, key, item):
        """ Store data in cache but don't exceed max value
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            # Append key to cache_log to track data stored
            if key in self.cache_log:
                self.cache_log.remove(key)
            self.cache_log.append(key)
        # Implement FIFO here
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            # Discard first item in the list
            print("DISCARD: {}".format(self.cache_log[0]))
            del self.cache_data[self.cache_log[0]]
            del self.cache_log[0]

    def get(self, key):
        """ Get data from cache
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        else:
            return None
