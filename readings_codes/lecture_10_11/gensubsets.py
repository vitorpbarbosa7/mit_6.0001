



def gensubsets(L):
	print('stack frame created')
	print(L)

	res = []
	
	if len(L) == 0:
		return [[]]
	
	# generate subsets for a list without containing the last element
	smaller = gensubsets(L[:-1])
	print(f'smaller: {smaller}')

	extra = L[-1:] # just last element
	print(f'extra: {extra}')
	new = []
	
	# for all subsets, add the last element
	for small in smaller:
		new.append(small+extra)
	
	print(f'created: {smaller+new}')
	return smaller+new

if __name__ == '__main__':

	L = [1,2,3,4]

	print(gensubsets(L))
