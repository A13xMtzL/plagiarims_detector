from collections import Counter

def word_occurrences_in_vectors(vector1, vector2):
    # Create Counters for each vector
    counter1 = Counter(vector1)
    counter2 = Counter(vector2)
    
    # Initialize lists to store counts for each vector
    counts_vector1 = []
    counts_vector2 = []
    
    # Iterate over unique words in both vectors
    unique_words = set(vector1 + vector2)
    for word in unique_words:
        # Get the count of the word in each vector
        count_vector1 = counter1[word]
        count_vector2 = counter2[word]
        
        # Append the counts to the respective lists
        counts_vector1.append(count_vector1)
        counts_vector2.append(count_vector2)
    
    return counts_vector1, counts_vector2

# Example usage
vector1 = ["apple", "banana", "apple", "orange"]
vector2 = ["banana", "grape", "apple", "banana"]

counts_vector1, counts_vector2 = word_occurrences_in_vectors(vector1, vector2)

print("Counts in vector1:", counts_vector1)
print("Counts in vector2:", counts_vector2)
