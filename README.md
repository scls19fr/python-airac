# python-airac

Regular, planned Aeronautical Information Publications (AIP) as defined by the International Civil Aviation Organization (ICAO) are published and become effective at fixed dates.

AIRAC cycle definition as published in the [ICAO Aeronautical Information Services Manual (DOC 8126; AN/872; 6th Edition; 2003)](https://www.icao.int/NACC/Documents/Meetings/2014/ECARAIM/REF09-Doc8126.pdf). Test cases validate documented dates from 2003 until 2022. They also assert that the rare cases of a 14th cycle, e. g. in the years 2020 and 2043 are correctly handled.

https://en.wikipedia.org/wiki/Aeronautical_Information_Publication

This project provides a Python library to deal with AIRAC cycle dates.

This project is not maintained by ICAO. Please use this project at your own risk.

## Installation

[python-airac](https://github.com/scls19fr/python-airac) is not currently a [Python registered package](https://juliapackages.com/).

Currently only developer version is available. It can be installed by running commandline:

```bash
$ pip install git+https://github.com/scls19fr/python-airac
```

## Usage

### Airac object

#### Get current AIRAC cycle
```python
In [1]: from airac import Airac

In [2]: airac = Airac()

In [3]: airac
Out[3]: <Airac 2101 2021-01-28>
```

#### Get first AIRAC cycle of a given year

```python
In [4]: Airac.from_year(2021)
Out[4]: <Airac 2101 2021-01-28>
```

#### Get properties of an AIRAC cycle

```python
In [5]: airac.date
Out[5]: datetime.date(2021, 1, 28)

In [6]: airac.ident
Out[6]: 2101

In [7]: airac.year
Out[7]: 2021
```

### Iterating over AIRAC cycle
```python
In [8]: airac = Airac.from_year(2021)

In [9]: airac.next()
Out[9]: <Airac 2102 2021-02-25>

In [10]: airac.move(12)
Out[10]: <Airac 2113 2021-12-30>

In [11]: airac.previous()
Out[11]: <Airac 2014 2020-12-31>
```

### Showing all cycle dates for a given year
```python
In [12]: g = (Airac(d) for d in airac_cycle_dates(2021))

In [13]: list(g)
Out[13]:
[<Airac 2101 2021-01-28>,
 <Airac 2102 2021-02-25>,
 <Airac 2103 2021-03-25>,
 <Airac 2104 2021-04-22>,
 <Airac 2105 2021-05-20>,
 <Airac 2106 2021-06-17>,
 <Airac 2107 2021-07-15>,
 <Airac 2108 2021-08-12>,
 <Airac 2109 2021-09-09>,
 <Airac 2110 2021-10-07>,
 <Airac 2111 2021-11-04>,
 <Airac 2112 2021-12-02>,
 <Airac 2113 2021-12-30>]
```

### Showing all cycle dates between 2 dates
```python
In [14]: 
```

### Parsing an AIRAC ident string
```python
In [15]: Airac.from_ident("1913")
Out[15]: <Airac 1913 2019-12-05>
```

### More informations

More informations can be found by watching at code:

- [code](airac/__init__.py)
- [tests](tests/test_airac.py)
