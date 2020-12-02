
from advent.model.password_policy import PasswordPolicy
from advent.days import extract_policy, validate_policy, positional_based_policy


__valid_example = '1-3 a: abcde'
__invalid_example = '1-6 z: abcde'


def test_valid_input_policy_extracted():
	policy = extract_policy(__valid_example)
	print(policy)
	assert policy is not None
	assert policy.minimum == 1
	assert policy.maximum == 3
	assert policy.character == 'a'

def test_valid_input_correct_passwords_detected():
	policy = extract_policy(__valid_example)
	policy_valid:bool  = validate_policy(policy, __valid_example)
	assert policy_valid


def test_max_char_password_valid():
	password_string = '1-5 b: bbbbb'
	policy = extract_policy(password_string)
	assert validate_policy(policy, password_string)


def test_min_char_password_valid():
	password_string = '1-3 c: caerwxf'
	policy = extract_policy(password_string)
	assert validate_policy(policy, password_string)


def test_invalid_password_string():
	policy = extract_policy(__invalid_example)
	assert not validate_policy(policy, __invalid_example)


def test_valid_positional_policy():
	policy = extract_policy(__valid_example)
	assert validate_policy(policy, __valid_example, positional_based_policy)


def test_invalid_positional_policy_no_match():
	password_string = '1-4 a: cdefsg'
	policy = extract_policy(password_string)
	assert not validate_policy(policy, password_string, positional_based_policy)


def test_invalid_positional_policy_duplicate_char():
	password_string = '1-3 b: babdd'
	policy = extract_policy(password_string)
	assert not validate_policy(policy, password_string, positional_based_policy)