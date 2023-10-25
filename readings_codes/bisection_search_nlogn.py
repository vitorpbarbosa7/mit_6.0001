


def bisect_search(L, e):
	print('stack frame created')
	print(f'current list: {L}')

	if L == []:
		# O(1)
		print(False)
		return False
	elif len(L) == 1:
		# O(1)
		print(L[0] == e)
		return L[0] == e

	else:
		half = len(L)//2
		if L[half] > e:
			# copying a list in python is O(n), because it iterates over every item in the list to copy it
			return bisect_search(L[:half], e)
		else:
			return bisect_search(L[half:], e)


if __name__ == '__main__':

	L = [12,29,56,45,65,34,20,82,81,53,44,24,25,13,22,11,27,31,26,19]
	L = sorted(L)

	e = 42

	bisect_search(L,e)
	
