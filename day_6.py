from advent.days import load_customs_files, load_customs_file_corrected

file_path = 'files/day_6.txt'
questions = load_customs_files(file_path)
print(sum(questions))
questions = []
questions = load_customs_file_corrected(file_path)
print(sum(questions))