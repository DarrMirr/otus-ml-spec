def leap_year(year):
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
        return 'YOU SHALL PASS'
    else:
        return 'YOU SHALL NOT PASS'


assert leap_year(5) == 'YOU SHALL NOT PASS'
assert leap_year(4) == 'YOU SHALL PASS'
assert leap_year(400) == 'YOU SHALL PASS'
assert leap_year(100) == 'YOU SHALL NOT PASS'
assert leap_year(4000) == 'YOU SHALL PASS'
