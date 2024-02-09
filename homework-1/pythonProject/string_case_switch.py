# Написать функцию, которая заменяет принимает строку текста и изменяет снейк_кейс на КамелКейс и наоборот
# my_first_func -> MyFirstFunc, AnotherFunction -> nother_function

# Перевод snake case строки в camel case
def snake_to_camel_case(snake: str) -> str:
    word_parts = snake.split("_")

    camel_str = ""
    for characters in word_parts:
        camel_str += characters.capitalize()

    return camel_str


# Перевод camel case строки в snake case
def camel_to_snake_case(camel: str) -> str:
    snake_str = ""
    for char in camel:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    return snake_str[1:2].lower() + snake_str[2:]


# ручные проверки корректности работы функции
print(snake_to_camel_case("my_first_func"))                             # ожидаемый результат MyFirstFunc
print(snake_to_camel_case("snake_case_to_camel_case"))                  # ожидаемый результат SnakeCaseToCamelCase

print(camel_to_snake_case("MyFirstFunc"))                               # ожидаемый результат my_first_func
print(camel_to_snake_case("SnakeCaseToCamelCase"))                      # ожидаемый результат snake_case_to_camel_case