from advent.days import get_f_from_list, get_b_from_list, parse_boarding_pass_string, parse_column_details, determine_seat_number


__sample_data = "FBFBBFFRLR"

def test_f_string():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual_list = get_f_from_list(test_list)
    expected = [1, 2, 3, 4, 5]
    assert sorted(actual_list) == sorted(expected)


def test_b_string():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    actual_list = get_b_from_list(test_list)
    expected = [5, 6, 7, 8, 9]
    assert sorted(actual_list) == sorted(expected)


def test_split_partitioning():
    expected = 44
    actual = parse_boarding_pass_string(__sample_data)
    assert expected == actual


def test_column_partitions_correctly():
    expected = 5
    test_string = "FBFBBFFRLR"
    actual = parse_column_details(test_string, plane_range=range(0, 8))
    assert expected == actual


def test_known_string():
    known_string = "BFFFBBFRRR"
    row = parse_boarding_pass_string(known_string)
    column = parse_column_details(known_string)
    seat_no = determine_seat_number(row, column)
    assert row == 70
    assert column == 7
    assert seat_no == 567


def test_known_string_two():
    known_string = "FFFBBBFRRR"
    row = parse_boarding_pass_string(known_string)
    column = parse_column_details(known_string)
    seat_no = determine_seat_number(row, column)
    assert row == 14
    assert column == 7
    assert seat_no == 119


def test_known_string_three():
    known_string = "BBFFBBFRLL"
    row = parse_boarding_pass_string(known_string)
    column = parse_column_details(known_string)
    seat_no = determine_seat_number(row, column)
    assert row == 102
    assert column == 4
    assert seat_no == 820