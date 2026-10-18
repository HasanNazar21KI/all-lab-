from datetime import date
from dateutil.relativedelta import relativedelta


def age_in_years(birth):
    """python-dateutil: рахує вік у роках."""
    return relativedelta(date.today(), birth).years
