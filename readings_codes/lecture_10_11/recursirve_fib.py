



def fib_recur(n):
	print('stack frame created')
	print(f'n : {n}')

	if n == 0:
		return 0

	elif n == 1:
		return 1 

	else:
		res = fib_recur(n-1) + fib_recur(n-2)
		print(f' \n res {res}')
		return res


fib_recur(5)
