from typing import List, Union
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
	return 0,0


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
						return x,y,z
	return 0,0,0


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
	return PasswordPolicy(int(minimum), int(maximum), mandatory_char.replace(':',''))


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
	position_one = password_str[policy.minimum -1 ]
	position_two = password_str[policy.maximum -1 ]
	return (position_one == policy.character) ^ (position_two == policy.character)


def validate_policy(policy: PasswordPolicy, password_line: str, password_validation_policy = count_based_policy) -> bool:
	"""
	Validates thepassword based on the password_validation_policy
	:param policy: password policy object
	:param password_line: the password line string
	:param password_validation_policy: The policy to use for validation
	"""
	return password_validation_policy(policy, password_line)

