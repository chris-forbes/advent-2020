from advent.days import parse_boarding_pass_string, parse_column_details, determine_seat_number

def challenge_one(data):
    max_seat = -1
    for line in data:
        row = parse_boarding_pass_string(line)
        column = parse_column_details(line)
        seat = determine_seat_number(row, column)
        if seat > max_seat:
            max_seat = seat
    print(f'max seat: {max_seat}')
    return 864

def challenge_two(data):
    seat_ids = []
    max, min = -1, 999
    for line in data:
        row = parse_boarding_pass_string(line)
        column = parse_column_details(line)
        seat = determine_seat_number(row, column)
        if seat > max:
            max = seat
        if seat < min:
            min = seat
        seat_ids.append(seat)
    print(seat_ids)
    print(f'Min: {min} - max {max}')
    print(sorted(seat_ids))
    all_seats = set(range(min, max + 1))
    my_seat = list(all_seats - set(seat_ids))
    print(my_seat)



data = []
with open('files/day_5_full.txt', 'r') as input_file:
    for line in input_file:
        data.append(line.replace('\n', ''))

challenge_one(data)
challenge_two(data)