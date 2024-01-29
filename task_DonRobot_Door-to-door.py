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
    result = ' '.join(min_route)
    return f'{min_find}\n{result}'


def input_data():
    places = input().split()
    distances = [[int(i) for i in input().split()] for _ in range(5)]
    return places, distances


if __name__ == '__main__':
    places, distances = input_data()
    print(route())
