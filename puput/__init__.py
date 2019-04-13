"""This module provides some functions to puput command.

These functions are mostly helpers and tools to support its options.
"""

import datetime

from jinja2 import Template


def format_generator(format):
    """This function returns a format function using format."""
    def format_func(e):
        t = Template(format)
        return t.render(e)

    return format_func


def filter_generator(to_date, title_starts):
    """This function returns a filter function combining other
       filters and argument values, if the filters were selected."""
    filters = [
        (
            lambda _: True,
            [],
        ),
    ]

    def filter_func(e):
        for f in filters:
            if not f[0](e, *f[1]):
                return False
        return True

    if to_date:
        filters.append((date_filter, []))
    if title_starts != '':
        filters.append((title_filter, [title_starts]))

    return filter_func


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
