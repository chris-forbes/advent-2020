from advent.days import find_matching_sum

__expected = 2020
__data_list = [1721,979,366,299,675,1456]

def test_with_example_data_correct_answer_found():
	a,b = find_matching_sum(__data_list, __expected)
	assert a == 1721
	assert b == 299

def test_with_example_data_final_result_expected():
	a,b = find_matching_sum(__data_list, __expected)
	