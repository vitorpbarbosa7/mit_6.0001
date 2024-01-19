cube = 27
eps = 0.01
num_guesses = 0
low = 0
high = cube

guess = (low + high)/2

num_guesses = 0
while abs(guess**3 - cube) > eps:
	# same thing, change the way we increment, we change value of guess, to go to another iteration

	if guess**3 > cube:
		high = guess
	else:
		low = guess
	
	# new guess
	guess = (low + high)/2

	num_guesses += 1

print('it took ', num_guesses, 'reach final result')	
print('guess is ', guess, 'and cube is ', cube)

