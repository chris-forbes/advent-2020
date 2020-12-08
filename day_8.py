from advent.days import load_instructions_file, run_instructions
from typing import List


def challenge_one(instructions: List[str]) -> int:
    accumulator, _ = run_instructions(instructions)
    return accumulator


def challenge_two(instructions: List[str]) -> None:
    possible_problems = [1, 101, 105, 117, 122, 130, 144, 151, 177, 217, 230, 235, 237, 241, 251, 262, 268, 269, 270,
                         286, 292, 303, 316, 339, 343, 349, 354, 358, 362, 364, 376, 386, 387, 397, 404, 411, 428, 43,
                         451, 462, 467, 478, 484, 5, 51, 525, 539, 544, 546, 578, 586, 594, 601, 615, 618, 629, 68, 73,
                         78] # I got these from the "stacktrace" mechanism

    for problem in possible_problems:
        index = problem - 1
        instructions_patched = instructions.copy()
        instructions_patched[index] = instructions_patched[index].replace('jmp', 'nop')
        print(f'auto patched {instructions[index]} with {instructions_patched[index]}')
        accumulator, status = run_instructions(instructions_patched)
        if status:
           print(f'Successful patch has been found {instructions[index]} with {instructions_patched[index]}')
           print(f'Accumulator: {accumulator}')
           break


if __name__ == '__main__':
    instructions = load_instructions_file('files/day_8_final.txt')
    print(f'Challenge one: {challenge_one(instructions)}')
    print(challenge_two(instructions))