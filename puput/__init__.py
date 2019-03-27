"""This module provides some functions to puput command.

These functions are mostly helpers and tools to support its options.
"""

import datetime


def title_filter(entry, prefix):
    """This function return True if the entry's title starts with prefix."""
    return entry['title'].startswith(prefix)


def date_filter(entry):
    """This function returns True if the entry's published date is newer
    than one day."""

    now = datetime.datetime.now()
    interval = datetime.timedelta(days=1)
    entry_published = datetime.datetime.strptime(
        entry['published'][:-4],
        '%a, %d %b %Y %H:%M:%S',
    )
    return now - entry_published <= interval
