file = open("DAY 4/xmas.txt", "r").read()

# find two MAS in the shape of an X
# M.S
# .A.
# M.S

coordinate_dict = {}
valid_positions = [((-1, -1), (1, 1)), ((1, -1), (-1, 1))]
found_matches = 0

# Receives starting point and coordinate change as arguments
def find_match(coordinates):
    mas_count = 0
    for position in valid_positions:
        letter_lookups = ["M", "S"]
        new_coordinate = (coordinates[0] + position[0][0], coordinates[1] + position[0][1])
        lookup = coordinate_dict.get(new_coordinate)

        if not lookup or lookup not in letter_lookups:
            return False
        
        letter_lookups.remove(lookup)
        new_coordinate = (coordinates[0] + position[1][0], coordinates[1] + position[1][1])
        lookup = coordinate_dict.get(new_coordinate)

        if not lookup or lookup not in letter_lookups:
            return False
        
        mas_count += 1

    return mas_count == 2

# Iterate over all rows of text
for i, row in enumerate(file.split()):
    # Iterate over all letters in row
    for j, letter in enumerate(row):
        # Save coordinate and letter
        coordinate_dict[(i, j)] = letter

# Loop through all coordinates and letters in dict
for coordinates, letter in coordinate_dict.items():
    # If the letter is not A, continue since there's nothing to check
    if letter != "A":
        continue
    
    if find_match(coordinates):
        found_matches += 1

print(found_matches)