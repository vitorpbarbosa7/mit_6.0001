



# esquece a recursao, pensa na auxiliar que faz a simples de abc


def aux(left, right):

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


res = aux('a', 'bc')

print(res)

res = aux('d', 'abc')

print(res)