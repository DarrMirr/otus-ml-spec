import numpy as np

print('----------')
print('Создайте случайный array (np.random.rand()) длинной 100. Преобразуйте его так, чтобы Максимальный элемент(ы) был равен 1, Минимальный элемент(ы) был равен 0, Остальные элементы в итнтервале от 0 до 1 остаются прежними:')
my_array = np.random.rand(100)

max_arg = np.argmax(my_array)
min_arg = np.argmin(my_array)
my_array[max_arg] = 1
my_array[min_arg] = 0

print(np.max(my_array), np.min(my_array))
print(my_array)

print('----------')
print('Создайте array размером 5×6 с целыми числами в интервале [0,50]. Напечатайте колонку, которая содержит максимальный элемент полученной матрицы:')\

my_array = np.random.randint(0, 50, size=(5, 6))
max_element = np.max(my_array)
max_element_coord = np.where(my_array == max_element)
selected_column = max_element_coord[1]

print('Shape: ', my_array.shape)
print('Array')
print(my_array)
print(f'max element {max_element}')
print(f'max element column number {selected_column}')

print('----------')
print('Напишите функцию, которая принимает на вход матрицу (array) X и возвращает все её уникальные строки в виде новой матрицы.')


def get_unique_rows(X):
    return np.unique(X, axis=0)


# X = np.random.randint(4, 6, size=(10, 3))
X = np.array([[1, 2, 3], [3, 2, 1], [1, 2, 3], [1, 3, 2]])
print(X)

X_unique = get_unique_rows(X)
print(X_unique)
