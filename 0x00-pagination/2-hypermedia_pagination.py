#!/usr/bin/env python3
"""pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


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
        """get func"""
        assert isinstance(page_size, int) and (page_size > 0)
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data_set = self.dataset
        dataset = self.dataset()
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """hyper func"""
        data_page = self.get_page(page, page_size)
        tot_pages = math.ceil(len(self.dataset()) / page_size)
        hyper_dict = {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if page < tot_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': tot_pages
        }
        return hyper_dict
