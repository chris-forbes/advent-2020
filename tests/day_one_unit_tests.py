from advent.days import find_matching_sum_two, find_product, find_matching_sum_three

__expected = 2020
__data_list = [1721,979,366,299,675,1456]

def test_with_example_data_correct_answer_found():
	a,b = find_matching_sum_two(__data_list, __expected)
	assert a == 1721
	assert b == 299

def test_with_example_data_final_result_expected():
	b = find_product(__data_list, __expected, find_matching_sum_two)
	assert b == 514579

def test_with_example_data_correct_answer_found_three_numbers():
	a,b,c = find_matching_sum_three(__data_list, __expected)
	assert a == 979
	assert b == 366
	assert c == 675

def test_with_example_data_final_result_expected_three():
	b = find_product(__data_list, __expected, find_matching_sum_three)
	assert b == 241861950