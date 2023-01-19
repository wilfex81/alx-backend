#!/usr/bin/env python3
""" Pagination """

import csv
import math
from typing import List, Tuple, Dict, Any


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
        pass

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        pass

    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """ returns tuple of size two containing start index, end index """
        pass
