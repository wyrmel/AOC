file = list(map(int, open("DAY 1/data.txt", "r").read().split()))

data_a = []
data_b = []

for index, item in enumerate(file):
    data_a.append(item) if index % 2 != 1 else data_b.append(item)

similarity_score = 0

for item in data_a:
    similarity_score = similarity_score + (item * data_b.count(item))

print(similarity_score)