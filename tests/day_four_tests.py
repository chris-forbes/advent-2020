from advent.model.passport import Passport
from advent.days import parse_passport_file, extract_passport_from_string, count_valid_passports, flexible_validation, strict_validation


__example_file = '../files/day_4_example_data.txt'
__invalid_strict_examples = '../files/day_4_example_2.txt'
__valid_strict_examples = '../files/day_4_valid_examples.txt'


def test_can_extract_passport_data_from_clean_line():
    clean_line = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm"
    passport = extract_passport_from_string(clean_line)
    assert passport.byr == 1937
    assert passport.hcl == '#fffffd'


def test_file_parses_correctly():
    passports = parse_passport_file(__example_file)
    assert len(passports) == 4


def test_flexible_validation():
    clean_line = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 hgt:183cm"
    passport = extract_passport_from_string(clean_line)
    assert flexible_validation(passport)


def test_invalid_line_flexible_validation():
    invalid_line = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017"
    passport = extract_passport_from_string(invalid_line)
    assert not flexible_validation(passport)


def test_expected_validation():
    passports = parse_passport_file(__example_file)
    valid = count_valid_passports(passports, flexible_validation)
    assert valid == 2


def test_invalid_counts():
    passports = parse_passport_file(__invalid_strict_examples)
    valid = count_valid_passports(passports, strict_validation)
    assert valid == 0


def test_valid_strict_examples():
    passports = parse_passport_file(__valid_strict_examples)
    valid = count_valid_passports(passports, strict_validation)
    assert valid == 4