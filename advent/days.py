from typing import List, Union


def find_matching_sum(data_list: List[int], expected: int) -> Union[int, int]:
	"""
	Find which elements when summed together match the expected value
	:param data_list: An array of integers 
	:param expected: The value we're looking to find
	"""
	for i in range(0, len(data_list)):
		current_primary = data_list[i]
		for element in data_list:
			if current_primary == element:
				continue
			else:
				if element + current_primary == expected:
					return current_primary, element
	return 0,0


# def find_product(data_list: List[int], expected: int) -> int:
	