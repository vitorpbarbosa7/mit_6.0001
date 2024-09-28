# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


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

def _aux(left, right):

    print(f''' Left {left} and right {right}''')

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return sequence

    else:
        left = sequence[0]
        right = sequence[1:]

        # recursive call for right permutations
        # em todos os niveis, tenho left e right

        # esquerda motra que ta voltando 
        # direta mostra que ta indo 
        right_permutations = get_permutations(right)

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
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    #TODO Implement as UnitTest in python instead of Assert

    # Example Test Case 1 
    example_input = 'abc'
    expected_output = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    out = get_permutations(example_input)
    assert(set(out)) == expected_output


