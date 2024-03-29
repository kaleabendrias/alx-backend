#!/usr/bin/env python3
"""pagination"""


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
