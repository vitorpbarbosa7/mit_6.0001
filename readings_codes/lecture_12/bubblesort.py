def bubblesort(L):

	swap = False
	
	# it will continue until no more out of order values are encountered
	# if it enters the loop, it means some of the values are out of order in that iteration yet

	while not swap: # O(n) can pass here n times, if it needs to swap in all iterations
		print(f'\n Current L: {L}\n')

		swap = True
		for j in range(1, len(L)): # O(n) goes through the list n times
			print(f'Intermediary L: {L}')
			print(f"Comparing '{L[j-1]}' and '{L[j]}' ")
			# if previous is bigger than the next, swap
			if L[j-1] > L[j]:
				swap = False
				temp = L[j]
				# bigger which was before, go to next position
				L[j] = L[j-1]
				#smaller which was after, to bo previous position
				L[j-1] = temp
			

if __name__ == '__main__':

	L = [4,3,2,6,1]

	print(bubblesort(L))
