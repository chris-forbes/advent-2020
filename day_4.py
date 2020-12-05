from advent.days import flexible_validation, parse_passport_file, count_valid_passports, strict_validation


def challenge_one(passports) -> int:
    return count_valid_passports(passports, flexible_validation)


def challenge_two(passports) -> int:
    return count_valid_passports(passports, strict_validation)

if __name__ == '__main__':
    passports = parse_passport_file('files/day_4.txt')
    print(f'Challenge one count: [{challenge_one(passports)}]')
    print(f'Challenge two count: [{challenge_two(passports)}]')