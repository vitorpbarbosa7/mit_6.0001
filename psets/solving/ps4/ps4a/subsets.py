

def generate_subsets(nums):
    if not nums:
        return [[]]  # Base case: an empty list has one subset - the empty subset
    
    # Recursive call to get subsets excluding the last element

    last_element = nums[-1]
    
    print(f'last element {last_element}')

    subsets_without_last = generate_subsets(nums[:-1])
    print(f'subsets without last: {subsets_without_last}')

    # Append the last element to each subset obtained from the recursive call
    subsets_with_last = []
    
    for subset in subsets_without_last:
        print(f'for subset_without_last: {subset} adding the last_element: {last_element}')
        subsets_with_last.append(subset + [last_element])

    print(subsets_with_last)
    breakpoint()
    
    # Combine the subsets obtained with and without the last element
    return subsets_without_last + subsets_with_last

# Test the function
original_list = [1, 2, 3]
result = generate_subsets(original_list)
print(result)