#include <stdio.h>
#include <stdlib.h>

// Function to count occurrences of 'value' in 'arr'
int count_occurences(int arr[], int size, int value) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == value) {
            count++;
        }
    }
    return count;
}

int main(void) {
    // Load data from file
    FILE *file = fopen("data.txt", "r");
    if (file == NULL) {
        printf("Error: Could not open data file.\n");
        return 1; // Didn't exit successfully
    }

    int data[2000]; // amount of numbers
    int size = 0;

    // Read numbers from file
    while (fscanf(file, "%d", &data[size]) == 1) {
        size++;
    }
    fclose(file);

    // Separate into data_a and data_b
    int data_a[1000], data_b[1000];
    int index_a = 0, index_b = 0;

    for (int i = 0; i < size; i++) {
        if (i % 2 != 1) {
            data_a[index_a++] = data[i];
        } else {
            data_b[index_b++] = data[i];
        }
        
    }

    // Calculate similarity_score
    int similarity_score = 0;

    for (int i = 0; i < index_a; i++) {
        similarity_score += data_a[i] * count_occurences(data_b, index_b, data_a[i]);
    }

    printf("Similarity score: %d\n", similarity_score);
    
    return 0;
    
}