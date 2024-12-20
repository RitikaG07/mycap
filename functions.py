def most_frequent(string):
    # Convert the string to lowercase for case-insensitivity
    string = string.lower()
    
    # Create a dictionary to count the frequency of each letter
    frequency = {}
    for letter in string:
        if letter.isalpha():  # Consider only alphabetic characters
            frequency[letter] = frequency.get(letter, 0) + 1
    
    # Sort the dictionary by frequency in descending order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # Print the letters with their frequencies
    for letter, count in sorted_frequency:
        print(f"{letter} = {count:02}")

# Accept input from the user
input_string = input("Please enter a string: ")
most_frequent(input_string)
