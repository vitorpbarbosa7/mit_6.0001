class RecursiveStringSplitter:
    def __init__(self):
        self.result_lists = []

    def split_string(self, s, left=None):
        if len(s) == 1:
            # If we reach the last level with only one element, put it inside a list
            self.result_lists.append([s])
            return

        left = s[0] if left is None else left
        right = s[1:]

        # Recursive call to go to the last level
        self.split_string(right, left)

        # Process the results from the last level and combine the lists
        for lst in self.result_lists:
            lst[-1] = left + lst[-1]
            lst.append(lst[-1] + left)

# Test the class
string_to_split = 'abc'
splitter = RecursiveStringSplitter()
splitter.split_string(string_to_split)

# Display the results
for i, lst in enumerate(splitter.result_lists):
    print(f"List {i + 1}: {lst}")
