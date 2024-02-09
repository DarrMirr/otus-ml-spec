# Вводится целое число (любого размера).
# Написать функцию, которая разобьет это число на разряды символом "пробел",
# Функция возвращает тип данных str
# 1234567 -> 1 234 567, 267 -> 267, 34976 -> 34 976`

def split_digit(number: int) -> str:
    # обработка сценария, если число отрицательное, чтобы знак минус "не отклеился"
    is_positive = True
    if number < 0:
        number = number * (-1)
        is_positive = False

    # блок инициализации переменных для запуска алгоритма
    input_str = str(number)
    output_str = input_str

    # алгоритм разделения числа по разрядам
    for i in range(3, len(input_str), 3):
        index = len(input_str) - i
        output_str = output_str[:index] + ' ' + output_str[index:]

    return output_str if is_positive else '-' + output_str


# ручные проверки корректности работы функции
print(split_digit(1000200300400500))               # ожидаемый результат 1 000 200 300 400 500
print(split_digit(34976))                          # ожидаемый результат 34 976
print(split_digit(1234567))                        # ожидаемый результат 1 234 567
print(split_digit(267))                            # ожидаемый результат 267
print(split_digit(-198267))                        # ожидаемый результат -198 267
print(split_digit(-7))                             # ожидаемый результат -7








###### Для истории ######
# Первый код, написанный на python
