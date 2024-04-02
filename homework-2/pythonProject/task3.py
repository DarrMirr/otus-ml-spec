def amulet_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


assert amulet_area(3, 4, 5) == 6
