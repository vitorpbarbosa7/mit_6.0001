class Example:
    def __init__(self):
        self.valid_words = ["apple", "banana", "cherry"]

    def get_valid_words(self):
        return self.valid_words  # Returning the original list

# Create an instance of the class
ex = Example()

# Get the list using the method
words = ex.get_valid_words()
print('Original Words: ', ex.valid_words) 
# Modify the returned list
words.append("date")

# Check the original list inside the object
print(ex.valid_words)  # Output: ['apple', 'banana', 'cherry', 'date']

