from advent.days import load_customs_files, load_customs_file_corrected

__sample_file_path = '../files/day_6_examples.txt'


def test_load_files():
    questions = load_customs_files(__sample_file_path)
    print(questions)
    assert questions
    assert len(questions) == 5
    assert sum(questions) == 11


def test_corrected_verification():
    questions = load_customs_file_corrected(__sample_file_path)
    assert questions
    assert sum(questions) == 6
