
def _print(left, right):

    print(f''' Left {left} and right {right}''')

def exec(left, right):

    permutations = []

    n = len(right) + 1
    for i in range(len(right)+1):

        if i == 0:
            word = left + right

        elif i > 0 and i < n:
            word = right[:i] + left + right[i:]

        else:
            word = right + left
        
        permutations.append(word)

    print(permutations)

    return permutations

sequence = 'abcd'

# left = sequence[0]
# right = sequence[1:]

# # para ter o outro lado, eu preciso aplicar a logica left, right em right

# previous_left  = left
# left = right[0]
# right = right[1:]
# res = exec(left, right)
# print(res)

# for output_right in res:
#     print(f'output right: {output_right}')
#     print(exec(previous_left, output_right))



def permutation(sequence):

    if len(sequence) == 1:
        return sequence

    else:
        left = sequence[0]
        right = sequence[1:]

        _print(left, right)

        permutation(right)

# res = permutation(sequence)
# print(res)
