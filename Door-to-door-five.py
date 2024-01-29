from itertools import permutations
from sys import maxsize


def route():
    min_find = maxsize
    min_route = ''
    for all_option in permutations(places):
        total_sum = 0
        for i in range(len(all_option) - 1):
            place = places.index(all_option[i])
            next_place = places.index(all_option[i + 1])
            total_sum += distances[place][next_place]
        if total_sum < min_find:
            min_find = total_sum
            min_route = all_option
    return f'Самый короткий путь: {min_route} протяжённостью {min_find}'


if __name__ == '__main__':
    places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')
    distances = (
        (0, 3570, 2230, 6430, 600),  # Расстояния от Gale.
        (3570, 0, 5280, 4530, 3315),  # Расстояния от Jezero.
        (2230, 5280, 0, 6715, 2540),  # Расстояния от Gusev.
        (6430, 4530, 6715, 0, 6400),  # Расстояния от Meridiani.
        (600, 3315, 2540, 6400, 0),  # Расстояния от Elysium.
    )
    print(route())
