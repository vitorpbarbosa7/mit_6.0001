


def bisect_search2(L, e):
	
	def bisect_search_helper(L, e, low, high):
		print('stack frame created')

		if high == low:
			return L[low] == e

		mid = (low + high)//2

		print(f'low: {low}, mid: {mid}, high: {high}')

		if L[mid] == e:
			return True
		
		
		elif L[mid] > e:
			if low == mid:
				return False
			else:
				# search in left partition
				# mid - 1 becomes the high
				return bisect_search_helper(L, e, low, mid - 1)

		else:
			# search in right partition, mid + 1 becomes the low value
			return bisect_search_helper(L, e, mid + 1, high)

	if len(L) == 0:
		return False

	else:
		return bisect_search_helper(L, e, 0, len(L) - 1)


if __name__ == '__main__':

	L = [12,29,56,45,65,34,20,82,81,53,44,24,25,13,22,11,27,31,26,19]
	L = sorted(L)

	e = 42

	bisect_search2(L,e)
