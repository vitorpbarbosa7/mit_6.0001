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

    return permutations

def get_permutations(sequence):

    if len(sequence) == 1:

        print(sequence)
    else:
    
        left = sequence[0]
        right = sequence[1:]
        
        _print(left, right)

        exec(left, right)

        get_permutations(right)


sequence = 'abcde'
get_permutations(sequence)