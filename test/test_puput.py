import datetime

import pytest

import puput


normal_entry = {
    'title': 'Some simple title',
}
job_offer_entry = {
    'title': 'Job offer: Company is looking for employee',
}


@pytest.mark.parametrize(
    'entry,prefix,expected_output',
    [
        (
            normal_entry,
            'Job offer',
            False,
        ),
        (
            job_offer_entry,
            'Job offer',
            True,
        )
    ],
    ids=[
        'Normal entry - Job offer',
        'Job offer entry - Job offer',
    ],
)
def test_title_filter(
        entry,
        prefix,
        expected_output,
):
    assert(puput.title_filter(entry, prefix) == expected_output)


today = datetime.datetime(2019, 3, 1, 9, 10, 11, 1234)
yesterday = 'Thu, 28 Feb 2019 19:10:11 UTC'
a_week_ago = 'Fri, 22 Feb 2019 19:10:11 UTC'
yesterday_entry = {
    'title': 'Some entry',
    'link': 'https://some.site/entry',
    'published': yesterday,
}
a_week_ago_entry = {
    'title': 'Some entry',
    'link': 'https://some.site/entry',
    'published': a_week_ago,
}
original_strptime = datetime.datetime.strptime


@pytest.fixture
def patch_datetime_now(monkeypatch):
    class mockDatetime(object):
        @classmethod
        def now(cls):
            return today

        @classmethod
        def strptime(cls, date, format):
            if date[-4:] == ' UTC':
                raise ValueError(
                    "time data '{}' does not match format '{}'".format(
                        date,
                        format,
                    ),
                )
            return original_strptime(date, format)

    monkeypatch.setattr(datetime, 'datetime', mockDatetime)


@pytest.mark.parametrize(
    'entry,expected_output',
    [
        (
            yesterday_entry,
            True,
        ),
        (
            a_week_ago_entry,
            False,
        ),
    ],
    ids=[
        'Yesterday entry',
        'A week ago entry',
    ],
)
def test_date_filter(
        entry,
        expected_output,
        patch_datetime_now,
):
    assert(puput.date_filter(entry) == expected_output)
