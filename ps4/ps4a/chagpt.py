def permute_string(s):
    if len(s) == 1:
        # Base case: If the string has only one character, return a list containing the character
        return [s]

    left = s[0]
    right = s[1:]

    # Recursive call to permute the right part of the string
    right_permutations = permute_string(right)

    # Process the results from the recursive call and permute the left character with each permutation
    permutations = []
    for permutation in right_permutations:
        for i in range(len(permutation) + 1):
            new_permutation = permutation[:i] + left + permutation[i:]
            permutations.append(new_permutation)

    return permutations

# Test the function with 'abc'
result = permute_string('abc')

# Display the permutations
for i, permutation in enumerate(result):
    print(f"Permutation {i + 1}: {permutation}")
