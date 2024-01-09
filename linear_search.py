all_tickets = [2345325, 5325235, 525235234, 5453535,
               636262564, 7856852, 43574947]
# find_my_ticket = 6246458
find_my_ticket = 2345325


def check_element(tickets, find_ticket):
    for ticket in tickets:
        if find_ticket == ticket:
            return True
    return False


if check_element(all_tickets, find_my_ticket):
    print(f"Билет {find_my_ticket} найден")
else:
    print(f"Билет {find_my_ticket} не найден")


def check_index_element(tickets, find_ticket):
    for idx, ticket in enumerate(tickets):
        if find_ticket == ticket:
            return str(idx)
    return False


idx = check_index_element(all_tickets, find_my_ticket)
if idx:
    print(f"Билет {find_my_ticket} найден под индексом {idx}")
else:
    print(f"Билет {find_my_ticket} не найден")


# Необходимо настроить эту функцию для работы с отсортированными массивами.
# Дополните код функции проверками:
# Если проверяемый элемент массива меньше искомого, то функция должна перейти
# к проверке следующего элемента.
# Если текущий элемент больше искомого, нужно остановить проверку и вернуть
# сообщение
# Элемент [искомое_значение] не найден в массиве..
