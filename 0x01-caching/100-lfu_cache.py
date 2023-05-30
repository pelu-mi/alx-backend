#!/usr/bin/env python3
""" Module for task 5
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Simple caching system
    """
    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.cache_log = []
        self.cache_usage = {}

    def put(self, key, item):
        """ Store data in cache but don't exceed max value
        """
        if key is None or item is None:
            return
        # ------------------------
        # Implement LFU & LRU here
        # ------------------------
        max_items = BaseCaching.MAX_ITEMS
        size = len(self.cache_data.keys())
        if key not in self.cache_data.keys() and size == max_items:
            # Find least frequently used items in the list
            # -based on storage and access
            del_list = []
            min_val = min(self.cache_usage.values())
            for k, v in self.cache_usage.items():
                if v == min_val:
                    del_list.append(k)
            # Check if list of LFU keys is more than one and implement LRU
            if len(del_list) > 1:
                del_key = ""
                for i in range(0, len(self.cache_log)):
                    for k in del_list:
                        if k == self.cache_log[i]:
                            del_key = k
                            break
                    if del_key != "":
                        break
            else:
                del_key = del_list[0]
            # Delete item
            print("DISCARD: {}".format(del_key))
            del self.cache_data[del_key]
            self.cache_log.remove(del_key)
            del self.cache_usage[del_key]
        # ----------------------------
        # Add key to data storage here
        # ----------------------------
        self.cache_data[key] = item
        # Append key to cache_log and track usage in cache_usage
        # -to track data stored
        if key in self.cache_log:
            self.cache_log.remove(key)
        self.cache_log.append(key)
        if key in self.cache_usage.keys():
            self.cache_usage[key] += 1
        else:
            self.cache_usage[key] = 1

    def get(self, key):
        """ Get data from cache
        """
        if key is not None and key in self.cache_data.keys():
            # Append key to cache_log and update cache_usage if data is gotten
            if key in self.cache_log:
                self.cache_log.remove(key)
            self.cache_log.append(key)
            if key in self.cache_usage.keys():
                self.cache_usage[key] += 1
            else:
                self.cache_usage[key] = 1
            return self.cache_data[key]
        else:
            return None
