# Шифр Цезаря. Написать функцию, которая будет принимать два аргумента: слово (str) и ключ (int).
# Результат выполнения функции - шифрованое слово по методоту Шифр Цезаря.
# Написать вторую функцию, которая будет проводить обратный процесс (или написать одну, выполняющую оба действия)
# 'dog', 3 -> 'grj', 'python', 5 -> 'udymts'

def encode_en(in_text: str, key: int) -> str:
    # Определение границ алфавита
    left_limit = ord("a")
    right_limit = ord("z")

    # Считаем, что регистр не важен при шифровании
    in_text = in_text.lower()

    out_text = ""
    for char in in_text:
        ascii_code = ord(char) + key
        if ascii_code > right_limit:
            # Корректировка по латинскому алфавиту.
            # Вычитание -1 в конце это поправка вызванная суммированием левой границей,
            # т.к. она тоже включена и должна учитываться при шифровании
            ascii_code = ascii_code - right_limit + left_limit - 1
        out_text += chr(ascii_code)
    return out_text


def decode_en(in_text: str, key: int) -> str:
    # Определение границ алфавита
    left_limit = ord("a")
    right_limit = ord("z")

    # Считаем, что регистр не важен при шифровании
    in_text = in_text.lower()

    out_text = ""
    for char in in_text:
        ascii_code = ord(char) - key
        if ascii_code < left_limit:
            # Корректировка по латинскому алфавиту.
            # Вычитание +1 в конце это поправка вызванная суммированием правой границей,
            # т.к. она тоже включена и должна учитываться при шифровании
            ascii_code = right_limit - (left_limit - ascii_code) + 1
        out_text += chr(ascii_code)
    return out_text


# ручные проверки корректности работы функции
print("Кодирование:")
print(encode_en("dog", 3))                  # ожидаемый результат grj
print(encode_en("yellow", 3))               # ожидаемый результат bhoorz
print(encode_en("python", 5))               # ожидаемый результат udymts

print("Декодирование:")
print(decode_en("grj", 3))                  # ожидаемый результат dog
print(decode_en("bhoorz", 3))               # ожидаемый результат yellow
print(decode_en("udymts", 5))               # ожидаемый результат python
