# Написать функцию, которая принимает на вход квадратное уравнение (одной строкой)
# и возвращает его корни, либо сообщает, что их нет
# "x**2 - 11*x + 28 = 0" -> x_1 = 4, x_2 = 7

def evaluate(quad_equation: str) -> list:
    # Объявление вспомогательных переменных
    quad_x = ""
    x = ""
    value_before_equal = ""
    value_after_equal = ""

    # Парсинг выражения
    equation = quad_equation.replace(" ", "")

    equation_split = equation.split("x**2")
    quad_x = equation_split[0].replace("*", "")
    quad_x = quad_x if len(quad_x) > 0 else "1"

    equation_split = equation_split[1].split("x")
    x = equation_split[0].replace("*", "")
    x = x if len(x) > 0 else "1"

    equation_split = equation_split[1].split("=")
    value_before_equal = equation_split[0]
    value_after_equal = equation_split[1]
    value_before_equal = value_before_equal if len(value_before_equal) > 0 else "0"
    value_after_equal = value_after_equal if len(value_after_equal) > 0 else "0"

    # Решение уравнения
    a = int(quad_x)
    b = int(x)
    c = int(value_before_equal) + int(value_after_equal)

    d = b * b - 4 * a * c

    if d < 0:
        return [None]
    elif d == 0:
        return [ b / 2 * a ]
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return [x1, x2]


# ручные проверки корректности работы функции
print(evaluate("x**2 - 11*x + 28 = 0"))                  # ожидаемый результат [7.0, 4.0]
print(evaluate("5*x**2 + 3*x + 7 = 0"))                  # ожидаемый результат [None]
print(evaluate("x**2 - 6*x + 9 = 0"))                    # ожидаемый результат [-3.0]