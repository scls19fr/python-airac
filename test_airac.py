import pytest

import airac
from airac import airac_date
from airac import airac_first_cycle_date, airac_last_cycle_date
from airac import airac_cycle_dates, number_airac_cycles
from airac import Airac
from airac import airac_cycle_tuple, airac_cycle, airac_cycle_ident

import datetime


def test_airac_date():
    assert airac_date(datetime.date(2020, 1, 15)) == datetime.date(2020, 1, 2)
    assert airac_date(datetime.date(2021, 2, 5)) == datetime.date(2021, 1, 28)


def test_airac_first_cycle_date():
    first_day = [
        (2003, 23),
        (2004, 22),
        (2005, 20),
        (2006, 19),
        (2007, 18),
        (2008, 17),
        (2009, 15),
        (2010, 14),
        (2011, 13),
        (2012, 12),
        (2013, 10),
        (2014, 9),
        (2015, 8),
        (2016, 7),
        (2017, 5),
        (2018, 4),
        (2019, 3),
        (2020, 2),
        (2021, 28),
        (2022, 27),
    ]
    for (year, day) in first_day:
        assert airac_first_cycle_date(year) == datetime.date(year, 1, day)


def test_airac_last_cycle_date():
    last_day = [
        (2003, 25),
        (2004, 23),
        (2005, 22),
        (2019, 5),
        (2020, 31),
        (2021, 30),
        (2022, 29),
    ]
    for (year, day) in last_day:
        assert airac_last_cycle_date(year) == datetime.date(year, 12, day)


def airac_number_of_cycles():
    assert list(airac_cycle_dates(2020)) == [
        datetime.date(2020, 1, 2),
        datetime.date(2020, 1, 30),
        datetime.date(2020, 2, 27),
        datetime.date(2020, 3, 26),
        datetime.date(2020, 4, 23),
        datetime.date(2020, 5, 21),
        datetime.date(2020, 6, 18),
        datetime.date(2020, 7, 16),
        datetime.date(2020, 8, 13),
        datetime.date(2020, 9, 10),
        datetime.date(2020, 10, 8),
        datetime.date(2020, 11, 5),
        datetime.date(2020, 12, 3),
        datetime.date(2020, 12, 31),
    ]

def airac_number_of_cycles():
    exceptions = [2020, 2043]
    for year in range(2003, 2050 + 1):
        n = number_airac_cycles(year)
        if year not in exceptions:
            assert n == 13
        else:
            assert n == 14

def test_airac_cycle():
    assert airac_cycle_tuple(datetime.date(2020, 1, 30)) == (2020, 2)
    assert airac_cycle(2020, 2) == 2002
    assert airac_cycle_ident(datetime.date(2020, 1, 30)) == 2002

def test_airac_object():
    year = 2020
    airac = Airac.from_year(year)
    assert airac.date == datetime.date(2020, 1, 2)
    assert airac.year == 2020
    assert airac.cycle == 1
    assert airac.ident == 2001

    airac = airac.next()
    assert airac.date == datetime.date(2020, 1, 30)
    assert airac.year == 2020
    assert airac.cycle == 2
    assert airac.ident == 2002

    airac = airac.previous()
    airac = airac.previous()
    assert airac.date == datetime.date(2019, 12, 5)
    assert airac.year == 2019
    assert airac.cycle == 13
    assert airac.ident == 1913

def test_parse_airac_ident():
    assert Airac.from_ident("1913").date == datetime.date(2019, 12, 5)

    assert Airac.from_ident("2001").date == datetime.date(2020, 1, 2)
    assert Airac.from_ident("2002").date == datetime.date(2020, 1, 30)
    assert Airac.from_ident("2014").date == datetime.date(2020, 12, 31)

    with pytest.raises(ValueError):
        Airac.from_ident("2115")
