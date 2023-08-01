


def sum(lista):

    if len(lista) == 1:

        # check if exists a list inside the list
        if isinstance(lista[0], list):
            lista = lista[0]
        else:
            # Base Case
            # se soh tem um elemento, retorne ele
            return lista[0]

    left = lista[0]
    right = lista[1:]

    print(f'left is {left} and right is {right}')

    # ligar a descida com a volta
    right = sum(right)

    print(f'right going back is {right}')
    
    return left + right


test_data = [1, 2, [3,4], [5,6]]
res = sum(test_data)
print(res)















def flatten_list_recursive(lst):
    flattened = []
    for item in lst:
        if isinstance(item, list):
            flattened.extend(flatten_list_recursive(item))
        else:
            flattened.append(item)
    return flattened


