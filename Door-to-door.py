from itertools import permutations

def route():
    places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')
    # Получим все возможные комбинации элементов кортежа places...
    combinations = permutations(places)
    # ...и проитерируемся по объекту с этими комбинациями:
    for path_index, travel_path in enumerate(combinations):
        print(path_index, travel_path)


if __name__ == '__main__':
    route()
