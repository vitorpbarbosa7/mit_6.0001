


def inttostr(i):
	
	digits = '0123456789'

	if i == 0:
		return '0'

	result = ''

	# linear complexity on the number of digits
	while i > 0:

		print(i%10)

		# always return the last digit
		result = digits[i%10] + result

		i = i //10

	print(type(result))
	print(result)
	return result


if __name__ == '__main__':

	i = 2345234

	inttostr(i)
