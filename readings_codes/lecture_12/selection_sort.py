''' 
given prefis in list L[0:i]
and suffix with L[i+1:len(L)], then we guarantee that 
no element in prefix is larget than any element in suffix, since all elements 
in prefix were put there by comparing it to the all other elements, which makes this an invariant
'''

'''

# Base case: prefix empty, and suffix is the whole list - invariant is true 

# Inductive step: move minimum element from suffix to the end of the prefix. Since invariant is true before move, the prefix is sorted after this appending. 

# when exist, prefix will be entire list, and will be sorted

'''

# O(n*n)
def selectionsort(L):

	suffixSt = 0
	
	# while the suffix lenght is not the full initial lenght list 
	while suffixSt != len(L): # this crazy while gives us already an O(n) in the face
		print(f'\nPrefix list: {L[0:suffixSt]}')
		print(f'Suffix list: {L[suffixSt:]}\n')

		for i in range(suffixSt, len(L)): # walk down the remaining of the list, even if gets shorter, it is still O(n) 
			
			# if the element is smaller than the element at suffixSt, then swap them
			# since the smaller should go to the suffixSt position
			if L[i] < L[suffixSt]:
				print(f'new smallest element {L[i]}')
				
				L[suffixSt], L[i] = L[i], L[suffixSt]

		# after a whole iteration, finding a element which is the smaller comparing to the suffix, update the suffixSt which now will be larger

		suffixSt += 1		


if __name__ == '__main__':

	L = [4,3,2,6,1]

	selectionsort(L)
