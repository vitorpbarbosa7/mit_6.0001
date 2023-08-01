


def sum(lista):

    if len(lista) == 1:
        # Base Case
        # se soh tem um elemento, retorne ele
        return lista[0]

    left = lista[0]
    right = lista[1:]

    # ligar a descida com a volta
    right = sum(right)

    # Inductive Step
    return left + right


test_data = [1,2,3,4,5,6]
res = sum(test_data)
print(res)

