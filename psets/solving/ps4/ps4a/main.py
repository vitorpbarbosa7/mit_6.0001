def executor(left, right):

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

    # print(permutations)

    return permutations

def permutation(sequence):

    if len(sequence) == 1:
        return sequence

    else:
        left = sequence[0]
        right = sequence[1:]

        # recursive call for right permutations
        # em todos os niveis, tenho left e right

        # esquerda motra que ta voltando 
        # direta mostra que ta indo 
        right_permutations = permutation(right)

        # quando volto, o que tenho que fazer?
        permutations = []

        # fazer algo com o que está voltando, que é o right_permutation
        # pegando todas permutacoes que vieram da direita, quando volta
        for single_right_permutation in right_permutations:

            new_permutations = executor(left, single_right_permutation)

            for new_permutation in new_permutations:

                permutations.append(new_permutation)

        # onde eu sempre tenho dificuldade, de voltar
        return permutations
    

if __name__ == '__main__':
    sequence = 'abc'
    all_permutations = permutation(sequence)
    print(all_permutations)