from advent.days import parse_map, traverse_continious, is_tree, next_x
__sample_data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def test_parse_map():
    map_data = parse_map(__sample_data)
    assert len(map_data) == 11


def test_tree_identified():
    assert is_tree('#')
    assert not is_tree('.')


def test_next_x_wraps_correctly():
    map_data = parse_map(__sample_data)
    assert next_x(0, 3, map_data[0]) == 3
    assert next_x(9, 3, map_data[0]) == 1


def test_trees_hit_traverse_continious():
    expected = 7
    map_data = parse_map(__sample_data)
    assert traverse_continious(map_data, (3, 1)) == expected


def test_varying_movement_speeds():
    map_data = parse_map(__sample_data)
    assert traverse_continious(map_data, (1, 1)) == 2
    assert traverse_continious(map_data, (3, 1)) == 7
    assert traverse_continious(map_data, (5, 1)) == 3
    assert traverse_continious(map_data, (7, 1)) == 4
    assert traverse_continious(map_data, (1, 2)) == 2
