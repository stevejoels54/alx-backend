#!/usr/bin/env python3
"""index_range function"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): Page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        tuple: Start index and end index for the specified pagination.
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
