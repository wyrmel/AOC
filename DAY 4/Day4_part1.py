file = open("DAY 4/xmas.txt", "r").read()

# Words can be horizontal, vertical, diagonal, written backwards, or even overlapping other words

coordinate_dict = {}
valid_positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
letter_lookups = ["M", "A", "S"]
found_matches = 0

# Receives starting point and coordinate change as arguments
def find_match(coordinates, coordinate_change):
    # Go through the letter lookups
    for letter in letter_lookups:
        # Get new coordinate
        new_coordinate = (coordinates[0] + coordinate_change[0], coordinates[1] + coordinate_change[1])
        lookup = coordinate_dict.get(new_coordinate)

        # If the lookup doesn't exists or the letter is wrong, return False
        if not lookup or lookup != letter:
            return False
        # Set new coordinates as coordinates to change
        coordinates = new_coordinate

    return True

# Iterate over all rows of text
for i, row in enumerate(file.split()):
    # Iterate over all letters in row
    for j, letter in enumerate(row):
        # Save coordinate and letter
        coordinate_dict[(i, j)] = letter

# Loop through all coordinates and letters in dict
for coordinates, letter in coordinate_dict.items():
    # If the letter is not X, continue since there's nothing to check
    if letter != "X":
        continue
    # Loop through all the valid position changes to look for matching words
    for position in valid_positions:
        # Check if the match is found
        if find_match(coordinates, position):
            found_matches += 1

print(found_matches)
