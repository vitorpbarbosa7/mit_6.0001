
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

def permutation(sequence):

    if len(sequence) == 1:
        return [sequence]
    
    left = sequence[0]

    print(f'left is {left}')

    right = permutation(sequence[1:])

    add_left = []
    for without_left in right:
        res = exec(without_left, left)
        print(f'res intemerd: {res}\n')
        for _res in res:
            add_left.append(_res)

    return right + add_left

sequence = 'abc'
permutation(sequence)