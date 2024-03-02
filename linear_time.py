def calculate_average(data):
    data_sum = 0
    for item in data:
        # Перебираем и суммируем все элементы массива:
        data_sum += item
    # Получившуюся сумму делим на количество элементов.
    average = data_sum / len(data)
    return average


print(calculate_average([1, 2, 3, 4, 5]))

# Оценим временную сложность этого алгоритма: подсчитаем, как от длины n 
# входного массива зависит число выполняемых операций.

#     Перед началом цикла присваиваем ноль переменной data_sum — одна операция.
#     Внутри цикла n раз выполняется суммирование — n операций.
#     Подсчёт длины массива выполняется за одно действие: скорость выполнения
# тех или иных операций можно найти в справочниках.
#     Итак, это ещё одна операция.
#     Деление общей суммы на длину массива — одна операция.

# Алгоритм состоит из двух частей — цикла со сложностью O(n) и трёх
# математических операций, которые выполняются за константное время O(1).
# Итого: временная сложность алгоритма равна O(n + 3). То есть в целом время
# выполнения растёт как O(n), но на 3 операции больше.
