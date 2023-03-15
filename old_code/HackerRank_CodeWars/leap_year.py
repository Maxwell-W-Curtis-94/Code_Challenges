def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


years = [
    1800,
    1900,
    1992,
    2000,
    2100,
    2200,
    2300,
    2400
]

for y in years:
    print(leap_year(year=y))
