#!/usr/bin/env python3
"""Pagination function for help.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function index_range takes two integer arguments page and page_size.
    """

    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)
