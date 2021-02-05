import datetime


AIRAC_DELAY = {
    "publication_date_major_changes": datetime.timedelta(days=56),
    "publication_date_normal": datetime.timedelta(days=42),
    "latest_delivery_date": datetime.timedelta(days=28),
    "cut_off_date": datetime.timedelta(days=20),
    "fms_data_production": datetime.timedelta(days=15),
    "delivery_to_operator": datetime.timedelta(days=7),
}

AIRAC_INTERVAL = datetime.timedelta(days=28)
AIRAC_INITIAL_DATE = datetime.date(2015, 1, 8)


date = datetime.date.today()


def airac_date(date=datetime.date.today()):
    if date >= AIRAC_INITIAL_DATE:
        diff_cycle = (date - AIRAC_INITIAL_DATE).days // AIRAC_INTERVAL.days
    else:
        diff_cycle = -((AIRAC_INITIAL_DATE - date).days // AIRAC_INTERVAL.days + 1)
    return AIRAC_INITIAL_DATE + diff_cycle * AIRAC_INTERVAL


def airac_first_cycle_date(year):
    return airac_date(datetime.date(year - 1, 12, 31)) + AIRAC_INTERVAL


def airac_last_cycle_date(year):
    return airac_date(datetime.date(year, 12, 31))


def airac_cycle_dates(year):
    start = airac_first_cycle_date(year)
    stop = airac_last_cycle_date(year)
    while start <= stop:
        yield start
        start += AIRAC_INTERVAL


def number_airac_cycles(year):
    return len(list(airac_cycle_dates(year)))


def airac_cycle_tuple(date=datetime.date.today()):
    date = airac_date(date)
    airac_year = date.year
    cycle = (date - airac_first_cycle_date(airac_year)).days // AIRAC_INTERVAL.days + 1
    return (airac_year, cycle)


def airac_cycle(year, cycle):
    return (year - 2000) * 100 + cycle


def airac_cycle_ident(date=datetime.date.today()):
    t = airac_cycle_tuple(date)
    return airac_cycle(t[0], t[1])


class Airac:
    def __init__(self, date=datetime.date.today()):
        self.date = airac_date(date)
        airac_year, cycle = airac_cycle_tuple(date)
        ident = airac_cycle(airac_year, cycle)
        self.year = airac_year
        self.cycle = cycle
        self.ident = ident

    def __repr__(self) -> str:
        return "<Airac %s %s>" % (self.ident, self.date)

    def __hash__(self) -> int:
        return hash(self.date)

    def __eq__(self, o: object) -> bool:
        return hash(self) == hash(o)

    def __lt__(self, o: object) -> bool:
        return self.date < o.date

    def __le__(self, o: object) -> bool:
        return self.date <= o.date

    def __gt__(self, o: object) -> bool:
        return self.date > o.date

    def __ge__(self, o: object) -> bool:
        return self.date >= o.date

    @staticmethod
    def from_year(year):
        return Airac(airac_first_cycle_date(year))

    def move(self, cycles_number):
        return Airac(self.date + cycles_number * AIRAC_INTERVAL)

    def next(self):
        return self.move(1)

    def previous(self):
        return self.move(-1)

    @staticmethod
    def from_ident(ident):
        ident = int(ident)
        cycle = ident % 100
        airac_year = 2000 + ident // 100
        date = airac_first_cycle_date(airac_year) + (cycle - 1) * AIRAC_INTERVAL
        if date.year != airac_year:
            raise ValueError("can't parse Airac ident %s" % ident)
        return Airac(date)
