import functools

file = open("DAY 5/page_numbers.txt", "r").read()
part1, part2 = file.split("\n\n")
rules = [tuple(map(int, item.split("|"))) for item in part1.split()]
data = [list(map(int, item.split(","))) for item in part2.split()]
result = 0

def compare_rules(a, b):
    if (a, b) in rules:
        return -1
    elif (b, a) in rules:
        return 1
    
    return 0

for original_item in data:
    new_item = sorted(original_item, key=functools.cmp_to_key(compare_rules))

    if original_item == new_item:
        result = result + original_item[len(original_item) // 2]

print(result)