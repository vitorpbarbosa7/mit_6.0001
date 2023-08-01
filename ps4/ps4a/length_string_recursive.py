


def length(s):

	if s == "":
		return 0

	else:
		return 1 + length(s[1:])


s = 'abcde'

res = length(s)
print(res)

	

