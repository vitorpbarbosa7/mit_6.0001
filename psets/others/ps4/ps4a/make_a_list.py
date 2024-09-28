
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

    
class Node:

    def __init__(self, string, parent = None):

        self.string = string
        self._parent = parent

        if self._parent is None:
            self.listas = []
        else:
            self.listas = self._parent.listas

        print(f'self.string is {self.string}')

        if len(self.string) == 1:
            self.listas = [self.string]
        
        else:
            # rule to go down
            
            self.left = self.string[0]

            print(f'left is {self.left} \n\n')
            self.right = Node(string = self.string[1:], parent = self)

        # regra para voltar
        if len(self.listas) > 0 and self.left is not None:

            upward_left = self._parent.left
            upward_right = self._parent.right
            print(f'\n\nUpward left is {upward_left}')
            print(f'\n\nUpward right is {upward_right}')

            for each_lista in self.listas:

                print(f'single list: {each_lista}')

                outputs = exec(upward_left, each_lista)

            for output in outputs:
                self.listas.append(output)



node = Node('abc')


    

