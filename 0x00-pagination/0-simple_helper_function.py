#!/usr/bin/env python3
""" Module for task 0
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> tuple:
    """ Return a tuple of size two containing a start index and
        an end index corresponding to the range of indexes
    """
    start = page_size * (page - 1)
    end = page_size * page
    return (start, end)
