from advent.days import find_product, find_matching_sum_two, find_matching_sum_three
from typing import List 


def load_file(path: str) -> List[int]:
	data = []
	with open(path, 'r') as input_file:
		for line in input_file:
			data.append(int(line))
	return data


if __name__ == '__main__':
	data = load_file('files/day_1.txt')
	print(find_product(data, 2020, find_matching_sum_two))
	print(find_product(data, 2020, find_matching_sum_three))