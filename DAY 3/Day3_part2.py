import re

file = open("DAY 3/mul.txt", "r").read()

mul_numbers = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", file)

total_sum = 0
enabled_flag = True

for value_a, value_b, enabled, disabled in mul_numbers:
    if disabled:
        enabled_flag = False
    if enabled:
        enabled_flag = True
        continue
    if enabled_flag:
        total_sum += int(value_a) * int(value_b)

print(total_sum)
