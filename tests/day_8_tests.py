from advent.days import load_instructions_file, run_instructions


__sample_file = '../files/day_8_test_file.txt'


def test_load_test_file():
    instructions = []
    with open(__sample_file, 'r') as input_file:
        for line in input_file:
            instructions.append(line.strip())
    loaded_instructions = load_instructions_file(__sample_file)
    for i in range(0, len(instructions)):
        assert instructions[i] == loaded_instructions[i]


def test_accumulator_before_duplicate_command():
    expected = 5
    instructions = load_instructions_file(__sample_file)
    actual = run_instructions(instructions)
    assert expected == actual