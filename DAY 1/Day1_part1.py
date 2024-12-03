file = list(map(int, open("DAY 1/data.txt", "r").read().split()))

data_a = []
data_b = []

for index, item in enumerate(file):
    data_a.append(item) if index % 2 != 1 else data_b.append(item)

total_distance = 0

for item_a, item_b in zip(sorted(data_a), sorted(data_b)):
    total_distance = total_distance + abs(item_a - item_b)

print(total_distance)
