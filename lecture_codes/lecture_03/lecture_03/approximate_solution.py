import matplotlib.pyplot as plt
import numpy as np

cube = 10000
eps = 0.1
guess = 0
# seems like we'll see a lot of this in the future (gradient descent, any algorithm that tries to find an approximate solution and accepts it within a error bound, lb and ub)
increment = 0.01
num_guesses = 0

# possible to create an algorithm which has a better strategy to initialize the search
# and also possible to have a better guess to where to go from, based on the difference of our guess and the cube, if we're getting closer of far from it
# gradient?
hist_values = []
while abs(guess**3 - cube) >= eps:
	diff = abs(guess**3 - cube)
	guess += increment
	num_guesses += 1

	hist_values.append(guess)

	# debug with previous knowledge
	if guess > np.cbrt(cube) + 100:
		print('already reached a value greater than the expected correct one')	
		break

	if guess > cube:
		print('guess reached a value greater than cube')
		break

	if num_guesses % 1000 == 0:
		print(guess, 'and', diff)

print('num_guesses = ', num_guesses)

if abs(guess**3 - cube) >= eps:
	print('Failed on finding the cube root of ', cube)
else:
	print(guess, ' is close to the cube root of ', cube)

#plt.plot(hist_values)
#plt.show()


# Visualize why it does not work
#>>> np.abs((0.01*2153)**3 - 10000)
#19.964422999997623
#>>> np.abs((0.01*2154)**3 - 10000)
#6.051736000001256
#>>> np.abs((0.01*2155)**3 - 10000)
#7.873875000001135
