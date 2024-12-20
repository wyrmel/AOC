valid_increases = [1, 2, 3]
valid_decreases = [-1, -2, -3]
valid_reports = 0

# Read text file levels.txt from DAY 2 folder
file = open("DAY 2/levels.txt", "r").read().split("\n")

def is_valid_report(int_data_set):
    """This function checks if a given report is valid by determining if it is strictly ascending or descending with valid increments or decrements."""
    ascending = False
    descending = False

    if int_data_set[0] > int_data_set[1]:
        descending = True
    elif int_data_set[0] < int_data_set[1]:
        ascending = True
    else:
        return False
    
    previous_value = int_data_set[0]

    for value in int_data_set[1:]:
        result = value - previous_value

        if(descending and result not in valid_decreases) or (ascending and result not in valid_increases):
            return False
        
        previous_value = value
    
    return True

for data_set in file:
    int_data_set = list(map(int, data_set.split()))

    # Checks if the report is valid as is
    if is_valid_report(int_data_set):
        valid_reports += 1
    else:
        # Sliding window to check for valid sequences by removing one level at a time
        for i in range(len(int_data_set)):
            modified_data_set = int_data_set[:i] + int_data_set[i+1:]

            if is_valid_report(modified_data_set):
                valid_reports += 1
                break

print(valid_reports)