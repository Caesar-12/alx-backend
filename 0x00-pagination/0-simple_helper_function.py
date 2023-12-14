#!/usr/bin/env python3

"""Contains a function that indexes"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    start index and an end index corresponding to the range of
    """

    return ((page-1) * page_size, page_size * page)
