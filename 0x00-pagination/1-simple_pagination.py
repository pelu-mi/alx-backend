#!/usr/bin/env python3
""" Module for task 1
"""


from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> tuple:
    """ Return a tuple of size two containing a start index and
        an end index corresponding to the range of indexes
    """
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Return the list of pages for the dataset
        """
        # Assert and verify both args are integers and > 0
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        # Get the page indexes using index_range
        start, end = index_range(page, page_size)
        # Return the pages required
        try:
            page_data = self.dataset()[start: end]
        except IndexError:
            page_data = []
        return page_data
