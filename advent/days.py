from typing import List, Union, Tuple
from advent.model.password_policy import PasswordPolicy


def find_matching_sum_two(data_list: List[int], expected: int) -> Union[int, int]:
	"""
	Find which elements when summed together match the expected value
	:param data_list: An array of integers
	:param expected: The value we're looking to find
	"""
	working_set = [x for x in data_list if x < expected]
	for elemen in working_set:
		for i in range(0, len(working_set)):
			current_primary = working_set[i]
			for element in working_set:
				if current_primary == element or current_primary == elemen or element == elemen:
					continue
				else:
					if element + current_primary == expected:
						return current_primary, element
	return 0, 0


def find_matching_sum_three(data_list: List[int], expected: int) -> Union[int, int]:
	"""
	Find which elements when summed together match the expected value
	:param data_list: An array of integers
	:param expected: The value we're looking to find
	"""
	working_set = [x for x in data_list if x < expected]
	for x in working_set:
		for y in working_set:
			for z in working_set:
				if x == y or x == z or y == z:
					continue
				else:
					if x + y + z == expected:
						return x, y, z
	return 0, 0, 0


def multiply(*args):
	"""
	Multiplies an arbitary number of packed arguments together
	:param args: packed args from multiple return tuple
	"""
	data = 1
	for x in args:
		for y in x:
			if y > 0:
				data *= y
	return data


def find_product(data_list: List[int], expected: int, sum_method: (List[int], int)) -> int:
	"""
	Finds the product of two numbers in a given list which sum to the expected value
	:param data_list: An array of integers
	:param expected: The value we're looking to find
	"""
	return multiply(sum_method(data_list, expected))


def extract_policy(password_line: str) -> PasswordPolicy:
	"""
	Extracts the password policy from the given password_line
	:param password_line: Full line from the test files
	"""
	ranges, mandatory_char, password = password_line.split(' ')
	minimum, maximum = ranges.split('-')
	return PasswordPolicy(int(minimum), int(maximum), mandatory_char.replace(':', ''))


def count_based_policy(policy: PasswordPolicy, password_line: str):
	"""
	Validates a given password policy against a password line
	:param policy: password policy object
	:param password_line: the password line string
	"""
	_, _, password_str = password_line.split(' ')
	counted_characters = str(password_str).count(policy.character)
	return counted_characters >= policy.minimum and counted_characters <= policy.maximum


def positional_based_policy(policy: PasswordPolicy, password_line: str):
	"""
	Validates a given password policy against a password line
	:param policy: password policy object
	:param password_line: the password line string
	"""
	_, _, password_str = password_line.split(' ')
	position_one = password_str[policy.minimum - 1]
	position_two = password_str[policy.maximum - 1]
	return (position_one == policy.character) ^ (position_two == policy.character)


def validate_policy(policy: PasswordPolicy, password_line: str, password_validation_policy=count_based_policy) -> bool:
	"""
	Validates thepassword based on the password_validation_policy
	:param policy: password policy object
	:param password_line: the password line string
	:param password_validation_policy: The policy to use for validation
	"""
	return password_validation_policy(policy, password_line)


def parse_map(map_data: str) -> List[str]:
	"""
	Parses the given map string into a grid
	:param map_data: the map data string
	:return: map data grid
	"""
	map_data_grid = []
	for line in map_data.split('\n'):
		map_data_grid.append(line)
	return map_data_grid


def next_x(current_x: int, x_movement: int, current_x_line: str) -> int:
	"""
	Determines the next x position and wraps if appropriate
	:param current_x: the starting position
	:param x_movement: how many steps must be made at each x
	:param current_x_line: the current line we're working on
	:return: next x index
	"""
	next_x_pos = current_x + x_movement
	if next_x_pos > len(current_x_line) - 1:  # wrap to 0 and add
		difference = len(current_x_line) - current_x
		new_x_move = x_movement - difference
		return 0 + new_x_move
	return next_x_pos


def is_tree(positional_character: str) -> bool:
	return positional_character == '#'


def traverse_continious(map_data: List[str], movement: Tuple[int, int]) -> int:
	"""
	Traverses the given map data counting how many trees you would hit
	:param map_data: x,y grid of map data
	:param movement:  x,y movement tuple
	:return: number of trees in the given map data that would be hit by moving in the movement manner
	"""
	trees_encountered = 0
	x_traversal, y_traversal = movement
	current_x, current_y = 0, 0

	while current_y < len(map_data):
		current_position = map_data[current_y][current_x]
		if is_tree(current_position):
			trees_encountered += 1
		current_x = next_x(current_x, x_traversal, map_data[current_y])
		current_y += y_traversal
		if current_y >= len(map_data):
			return trees_encountered
	return trees_encountered
