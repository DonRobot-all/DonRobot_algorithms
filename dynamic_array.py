# Импорт библиотеки для работы с временем.
import time

# Количество элементов в массивах.
data2 = []
print(id(data2))
elements_count = int(input())
for data_index in range(elements_count):
    # Добавляем новые элементы в конец списка.
    data2.append(f'some new value {data_index}')
print(id(data2))
