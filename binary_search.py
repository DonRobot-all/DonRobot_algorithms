import time
import os, psutil
process = psutil.Process()

# with open('numbers.txt', 'r') as file:
#     array.append(map(int(file.read())))

# file = open("numbers.txt", "r")
# array = [map(float, line.split("\t")) for line in file]
# print(array)

start_time = time.time()
array = []
with open("numbers.txt") as f:
    for line in f:
        array.append([int(x) for x in line.split()])


def find_element_binary_search(sorted_numbers, element):
    """Находит индекс element в отсортированном списке sorted_numbers."""
    left = 0
    right = len(sorted_numbers)
    while left <= right:
        mid = (left + right) // 2
        if element == sorted_numbers[mid]:
            return mid
        if element > sorted_numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1


def find_element_linear_search(sorted_numbers, element):
    for idx, number in enumerate(sorted_numbers):
        if element == number:
            return idx


t0 = time.time()
# for item in wins:
print(find_element_binary_search(array[0], 10003109))
t1 = time.time()
print("Время выполнения бинарного алгоритма: ", t1 - t0)

end_time = time.time()
print("Время выполнения программы до линейного поиска: ", end_time - start_time)

t0 = time.time()
# for item in wins:
print(find_element_linear_search(array[0], 10002762))
t1 = time.time()
print("Время выполнения линейного алгоритма: ", t1 - t0)

end_time = time.time()
print("Время выполнения всей программы: ", end_time - start_time)
print("Задействовано памяти: ", process.memory_info().rss / 1024 ** 2)