from itertools import permutations

# Обрабатываем один из маршрутов:
current_path = ('Gusev', 'Meridiani', 'Gale', 'Jezero', 'Elysium')

places = ('Gale', 'Jezero', 'Gusev', 'Meridiani', 'Elysium')
distances = (
    (0, 3570, 2230, 6430, 600),  # Расстояния от Gale.
    (3570, 0, 5280, 4530, 3315),  # Расстояния от Jezero.
    (2230, 5280, 0, 6715, 2540),  # Расстояния от Gusev.
    (6430, 4530, 6715, 0, 6400),  # Расстояния от Meridiani.
    (600, 3315, 2540, 6400, 0),  # Расстояния от Elysium.
)


def route():
    distances_current_path = []
    for i in range(len(current_path) - 1):
        place = places.index(current_path[i])
        next_place = places.index(current_path[i + 1])
        print(f'Мы идём из {place} в {next_place}')
        distances_current_path.append(distances[place][next_place])
    print(distances_current_path)


if __name__ == '__main__':
    print(route())
