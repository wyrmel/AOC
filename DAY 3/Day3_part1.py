import re

file = open("DAY 3/mul.txt", "r").read()

mul_numbers = re.findall(r"mul\((\d+),(\d+)\)", file)

total_sum = 0

for item in mul_numbers:
    total_sum += int(item[0]) * int(item[1])

print(total_sum)
