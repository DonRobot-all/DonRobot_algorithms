def list_superset(list_set_1, list_set_2):
    lenght_set_1 = len(list_set_1)
    lenght_set_2 = len(list_set_2)
    for el in list_set_1:
        if el not in list_set_2 and lenght_set_1 <= lenght_set_2:
            return 'Супермножество не обнаружено.'
    for el in list_set_2:
        if el not in list_set_1 and lenght_set_2 < lenght_set_1:
            return 'Супермножество не обнаружено.'
    if lenght_set_2 == lenght_set_1:
        return 'Наборы равны.'
    elif lenght_set_1 > lenght_set_2:
        return f'Набор {list_set_1} - супермножество.'
    return f'Набор {list_set_2} - супермножество.'


list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
