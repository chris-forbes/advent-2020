from advent.days import extract_policy, validate_policy, positional_based_policy


def count_based_policy_counter(data):
	"""
	Uses the count based policy to find the number of invalid passwords
	:param data: cleansed data strings
	"""
	print('Using count based password policy')
	valid = 0
	invalid = 0
	for password in data:
		policy = extract_policy(password)
		if validate_policy(policy, password):
			valid += 1
		else:
			invalid += 1

	print(f'[+]\tValid: {valid}')
	print(f'[+]\tInvalid: {invalid}')


def positional_based_policy_counter(data):
	"""
	Uses the count based policy to find the number of invalid passwords
	:param data: cleansed data strings
	"""
	print('Using positional_based_policy')
	valid = 0
	invalid = 0
	for password in data:
		policy = extract_policy(password)
		if validate_policy(policy, password, positional_based_policy):
			valid += 1
		else:
			invalid += 1

	print(f'[+]\tValid: {valid}')
	print(f'[+]\tInvalid: {invalid}')


if __name__ == '__main__':
	data = []
	[data.append(str(line).replace('\n','')) for line in open('files/day_2.txt', 'r') ]
	count_based_policy_counter(data)
	positional_based_policy_counter(data)