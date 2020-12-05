from advent.days import traverse_continious
from math import prod

def challenge_one(map_data):
    print(f'Challenge one: {traverse_continious(map_data, (3, 1))}')


def challenge_two(map_data):
    trees_encountered_results = []
    movements = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for movement in movements:
        trees_encountered = traverse_continious(map_data, movement)
        print(f'Challenge two: Current movement [{movement}], trees_encountered: {trees_encountered}')
        trees_encountered_results.append(trees_encountered)
    print(f'All trees encountered: [{trees_encountered_results}]')
    print(prod(trees_encountered_results))


if __name__ == '__main__':
    map_data = []
    with open('files/day_3.txt', 'r') as input_file:
        for line in input_file:
            map_data.append(str(line).replace('\n', ''))
    challenge_one(map_data)
    challenge_two(map_data)
