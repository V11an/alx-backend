#!/usr/bin/env python3
"""
definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes 2 int args and returns a tuple of size two
    containing start & end index corresponding to range of
    indexes to return in a list for those pagination parameters
    Args:
        page(int): page no. to return (pages are 1-indexed)
        page_size(int): no. of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
