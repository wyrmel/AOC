valid_increases = [1, 2, 3]
valid_decreases = [-1, -2, -3]
valid_reports = 0

# Read text file levels.txt from DAY 2 folder
file = open("DAY 2/levels.txt", "r").read().split("\n")

for data_set in file:
    ascending = False
    descending = False
    invalid_flag = False

    int_data_set = list(map(int, data_set.split()))
    
    if int_data_set[0] > int_data_set[1]:
        descending = True
    elif int_data_set[0] < int_data_set[1]:
        ascending = True
    else:
        continue

    previous_value = 0
    first_index = True

    for value in int_data_set:
        if first_index:
            previous_value = value
            first_index = False
            continue

        result = value - previous_value
        if (descending and result not in valid_decreases) or (ascending and result not in valid_increases):
            invalid_flag = True
            break
        
        previous_value = value
    
    if invalid_flag == False:
        valid_reports = valid_reports + 1
    
print(valid_reports)