


'''
Divide an conquer strategy, that is, splitting the list into two peaces (famous probably log2 complexity)

Steps:

1 - If list is of length 0 or 1, list is already sorted
2 - If list has more than one element, split into two lists, and sort each

The list is split in half until have sublists of only 1 element

 
3 - Merge sorted lists

3.1 - Look at first element of each, move smaller to first positions?
3.2 - When one list is empty, add all remaining element of the other list to the merged list
'''

'''
Complexity analysis of merge

go through two lists, only one pass

compare only the smallest elements in each sublist

O(len(left) + len(right)) copied elements
O(len(longer list)) comparisons
linear in lenght of the lists
'''

def merge(left, right, superior_side):

	'''
	Merging two lists in a sorted manner, considering that each list is already sorted
	'''
	print(f'\n superior side: {superior_side}')
	print(f'merging {left} and {right}')
	
	result = []
	i,j = 0,0

	# appending to the result the ones with smallest value at each step
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	# add remaining elements if not yet added to the result, since it's only added when i and j reach the lenght of the lists 

	while (i < len(left)):
		result.append(left[i])
		i += 1

	while (j < len(right)):
		result.append(right[j])
		j += 1

	print(f'Result of merging: {result}\n')
	
	return result
		

# How to break the problem into two?

def mergesort(L, side:str):

	'''
	L : list of elements
	side: keep track of what side is it in 
	'''
	
	print(f'\nside: {side}')
	print(f'List: {L}')

	# Base Case
	if len(L) < 2:

		return L[:]
	
	# Divide
	else:

		mid = len(L)//2
		left = L[:mid]
		right = L[mid:]

		print(f'left: {left}')
		print(f'right: {right}')

		left = mergesort(left, 'left')
		right = mergesort(right, 'right')
	
	# Conquer
		return merge(left, right, superior_side=side)
		
if __name__ == '__main__':

	L = [3,2,1,4,6,5]

	mergesort(L, 'start')

