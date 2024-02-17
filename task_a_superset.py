def list_superset(list_set_1, list_set_2):
    lenght_set_1 = len(list_set_1)
    lenght_set_2 = len(list_set_2)
    for el in list_set_1:
        if el not in list_set_2 and lenght_set_1 <= lenght_set_2:
            return 'Суперсписок не обнаружен.'
    for el in list_set_2:
        if el not in list_set_1 and lenght_set_2 < lenght_set_1:
            return 'Суперсписок не обнаружен.'
    if lenght_set_2 == lenght_set_1:
        return 'Списки равны.'
    elif lenght_set_1 > lenght_set_2:
        list_set_1 = ' '.join(list_set_1)
        return f'Набор {list_set_1} - суперсписок.'
    list_set_2 = ' '.join(list_set_2)
    return f'Набор {list_set_2} - суперсписок.'


def input_data():
    list_set_1 = input().split()
    list_set_2 = input().split()
    return list_set_1, list_set_2

# list_set_1 = [1, 3, 5, 7]
# list_set_2 = [3, 5]
# list_set_3 = [5, 3, 7, 1]
# list_set_4 = [5, 6]


if __name__ == '__main__':
    print(list_superset(*input_data()))
    # print(list_superset(list_set_2, list_set_3))
    # print(list_superset(list_set_1, list_set_3))
    # print(list_superset(list_set_2, list_set_4))
