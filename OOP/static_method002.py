"""
Static methods are used when we don't want subclasses of a class
change/override a specific implementation of a method.

Here, we wouldn't want the subclass DatesWithSlashes to override the
static utility method toDashDate because it only has a single use,
i.e. change date to dash-dates.

We could easily use the static method to our advantage by overriding
getDate() method in the subclass so that it works well with the
DatesWithSlashes class.
"""


class Dates:
    def __init__(self, date_):
        self.date = date_

    def get_date(self):
        return self.date

    @staticmethod
    def to_dashed_date(date_):
        return date_.replace("/", "-")


class DatesWithSlashes(Dates):
    def get_date(self):
        return Dates.to_dashed_date(self.date)


date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if date.get_date() == dateFromDB.get_date():
    print("Equal")
else:
    print("Unequal")
