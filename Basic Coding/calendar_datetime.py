import calendar as cal
from datetime import date

year = int(input("Enter a year : "))
if cal.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

year = 2024
month = 11
print(cal.month(year,month))
print(cal.calendar(year))
print(cal.monthrange(year,month)[1])
