from typing import List, Union, Tuple
from advent.model.password_policy import PasswordPolicy
from advent.model.passport import Passport
from math import ceil
import re


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


def extract_passport_from_string(data_line: str) -> Passport:
	"""
	Takes a password string with all data and parses it into a passport object
	:param data_line: the full data line
	:return: @Passport object
	"""
	passport = Passport()
	data_dict = {}
	for data_element in data_line.split(' '):
		if data_element == '':
			continue
		key, value = data_element.split(':')
		data_dict[key] = value
	passport.byr = int(data_dict['byr']) if 'byr' in data_dict.keys() else None
	passport.pid = data_dict['pid'] if 'pid' in data_dict.keys() else None
	passport.eyr = int(data_dict['eyr']) if 'eyr' in data_dict.keys() else None
	passport.hcl = data_dict['hcl'] if 'hcl' in data_dict.keys() else None
	passport.ecl = data_dict['ecl'] if 'ecl' in data_dict.keys() else None
	passport.cid = data_dict['cid'] if 'cid' in data_dict.keys() else None
	passport.iyr = int(data_dict['iyr']) if 'iyr' in data_dict.keys() else None
	passport.hgt = data_dict['hgt'] if 'hgt' in data_dict.keys() else None
	return passport


def parse_passport_file(file_path: str) -> List[Passport]:
	"""
	Parses the give file and returns a list of @Passport objects
	:param file_path: the path to the data file
	:returns: List of passport objects
	"""
	passports = []
	with open(file_path, 'r') as input_file:
		full_string = ""
		for line in input_file:
			if line == '\n':
				passports.append(extract_passport_from_string(full_string))
				full_string = ""
				continue
			full_string += str(line).replace('\n', ' ')
		passports.append(extract_passport_from_string(full_string))
	return passports


def flexible_validation(passport: Passport) -> bool:
	"""
	Determisn if a passport is flexible
	:param passport: the passport to check
	:return: valid or not
	"""
	if passport.ecl and passport.pid and passport.eyr and passport.hcl and passport.byr and passport.iyr and passport.hgt:
		return True
	return False


def strict_validation(passport: Passport) -> bool:
	if not passport.byr:
		return False
	else:
		if passport.byr < 1920 or passport.byr > 2002:
			return False

	if not passport.iyr:
		return False
	else:
		if passport.iyr < 2010 or passport.iyr > 2020:
			return False
	if not passport.eyr:
		return False
	else:
		if passport.eyr < 2010 or passport.eyr > 2030:
			return False

	if not passport.hgt:
		return False
	elif "cm" in passport.hgt or "in" in passport.hgt:
		numbers = re.findall('[0-9]+', passport.hgt)
		numbers = int(numbers[0])
		if "cm" in passport.hgt:
			if numbers < 150 or numbers > 193:
				return False
		elif "in" in passport.hgt:
			if numbers < 59 or numbers > 76:
				return False
		else:
			return False
	else:
		return False

	if not passport.hcl:
		return False
	else:
		pattern = re.compile("#[a-f 0-9]{6}")
		if not pattern.match(passport.hcl):
			return False

	if not passport.ecl:
		return False
	else:
		valid = ['amb','blu','brn','gry','grn','hzl','oth']
		if passport.ecl not in valid:
			return False

	if not passport.pid:
		return False
	else:
		if len(passport.pid) != 9:
			return False
	return True


def count_valid_passports(passport_list: List[Passport], validation_method: ()) -> int:
	"""
	Uses the validation method to count how many valid passports have been parsed
	:param passport_list: list of passport objects
	:param validation_method: the method to use for determining if a passport object is valid
	:return: number of valid passports
	"""
	count = 0
	for passport in passport_list:
		if validation_method(passport):
			count += 1
	return count


def get_f_from_list(plane_range: List[int]) -> List[int]:
	"""
	returns the front half of the list
	:param plane_range: the range to work with
	:return: the front half of the list
	"""
	current_length = len(plane_range) - 1
	middle_sector = ceil(current_length / 2)
	return plane_range[:-middle_sector]


def get_b_from_list(plane_range: List[int]) -> List[int]:
	"""
	returns the front half of the list
	:param plane_range: the range to work with
	:return: the front half of the list
	"""
	current_length = len(plane_range) - 1
	middle_sector = ceil(current_length / 2)
	return plane_range[middle_sector:]


def parse_boarding_pass_string(boarding_pass: str, plane_range: range = range(0, 128), f_function: () = get_f_from_list, b_function: () = get_b_from_list) -> List[int]:
	"""
	Parses a given boarding pass string
	:param plane_range: Optional range, default 0,128
	:param f_function: function for forward slicing
	:param b_function: function for backward slicing
	:param boarding_pass: the boarding pass string
	:return: the row number
	"""

	for char in boarding_pass:
		if char.lower() == 'f':
			plane_range = f_function(plane_range)
		elif char.lower() == 'b':
			plane_range = b_function(plane_range)
	if boarding_pass[:len(boarding_pass) - 3][-1].lower() == 'f':
		x = min(plane_range)
		return x
	elif boarding_pass[:len(boarding_pass) - 3][-1].lower() == 'b':
		y = max(plane_range)
		return y
	return plane_range


def parse_column_details(boarding_pass: str, plane_range: range = range(0, 8), f_function: () = get_f_from_list, b_function: () = get_b_from_list) -> List[int]:
	"""
	determines the column number from the string
	Parses a given boarding pass string
	:param plane_range: Optional range, default 0,128
	:param f_function: function for forward slicing
	:param b_function: function for backward slicing
	:param boarding_pass: the boarding pass string
	:return: the row number
	:return: the column number
	"""
	last_three = boarding_pass[-3:]
	for char in last_three:
		if char.lower() == 'l':
			plane_range = f_function(plane_range)
		elif char.lower() == 'r':
			plane_range = b_function(plane_range)
	if boarding_pass[-1].lower() == 'l':
		x = min(plane_range)
		return x
	elif boarding_pass[-1].lower() == 'r':
		x = max(plane_range)
		return x


def determine_seat_number (row: int, column: int) -> int:
	"""
	Determines the seat number from the row and column
	:param row: the row number you worked out
	:param column:  the column number you worked out
	:return: the seat number
	"""
	seat = row * 8
	seat += column
	return seat


def load_customs_files(file_path: str) -> List[int]:
	"""
	detemines which questions where answered yes
	:param file_path: fulle path to the file
	:return: list of each groups answers
	"""
	az_pattern = re.compile('[a-z]+')
	questions_answered_per_group = []
	with open(file_path, 'r') as input_file:
		questions = set()
		for line in input_file:
			if az_pattern.match(line):
				for char in line.replace('\n', ''):
					questions.add(char)
			else:
				sum_of_questions_answered = len(questions)
				questions_answered_per_group.append(sum_of_questions_answered)
				questions = set()
				continue
		questions_answered_per_group.append(len(questions))
	return questions_answered_per_group


def load_customs_file_corrected(file_path: str) -> List[int]:
	"""
		determines which questions where all group members answered yes
		:param file_path: fulle path to the file
		:return: list of each groups answers
	"""
	az_pattern = re.compile('[a-z]+')
	questions_answered_per_group = []
	with open(file_path, 'r') as input_file:
		questions = {}
		members_per_party = 0
		for line in input_file:
			if az_pattern.match(line):
				members_per_party += 1
				for char in line.replace('\n', ''):
					if char in questions.keys():
						questions[char] += 1
					else:
						questions[char] = 1
			else:
				answered_by_all = 0
				for k,v in questions.items():
					if v == members_per_party:
						answered_by_all += 1
				questions_answered_per_group.append(answered_by_all)
				questions = {}
				members_per_party = 0

		answered_by_all = 0
		for k, v in questions.items():
			if v == members_per_party:
				answered_by_all += 1
		questions_answered_per_group.append(answered_by_all)
	return questions_answered_per_group


def load_instructions_file(file_path: str) -> List[str]:
	"""
	Parses the instruciton file into a list
	:param file_path: the full path to the instructions file
	:return: the instructions in an OrderedList
	"""
	instructions = []
	with open(file_path, 'r') as input_file:
		for line in input_file:
			instructions.append(line.strip())
	return instructions


def run_instructions(instructions: List[str]) -> int:
	"""
	Runs the given instruction set until it is about to run a command for the second time
	:param instructions: instruction set
	:return: accumulator -> int
	"""
	accumulator = 0
	inst_ptr = 0
	instruction_history = []
	all_jump_instructions = []
	all_nop_instructions = []
	while inst_ptr != len(instructions):
		instruction, value = instructions[inst_ptr].split(' ')
		# have we run an instruction at this point previously?
		if inst_ptr in instruction_history:

			if len(all_jump_instructions) == 0:
				for executed_instr in instruction_history:
					if 'jmp' in instructions[executed_instr]:
						all_jump_instructions.append(f'instruction: [{instructions[executed_instr]}] -> line number [{executed_instr + 1}], ')
					elif 'nop' in instructions[executed_instr]  :
						all_nop_instructions.append(f'instruction: [{instructions[executed_instr]}] -> line number [{executed_instr + 1}], ')

			print('Duplicate detected exiting early')
			print(f""" 
Stack trace: 
	Instruction ptr [{inst_ptr}]
	Instruction ran: [{instruction_history}]
	jump_instructions : [{all_jump_instructions}]
	nop_instructions []: [{all_nop_instructions}]
			""")
			return accumulator, False
		else:
			instruction_history.append(inst_ptr)

		if instruction == 'jmp':
			inst_ptr += int(value)
			continue

		elif instruction == 'acc':
			accumulator += int(value)
			inst_ptr += 1
			continue

		elif instruction == 'nop':
			inst_ptr += 1
			continue
	print('run complete...')
	return accumulator, True