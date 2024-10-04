lst = ['a', 'b', 'c', 'd', 'e']

def rot_list(lst, shift):

    shift = shift % len(lst)
    
    for_upper = lst[:]
    for_lower = lst[:]
    # the final part at the beginning
    lower = for_upper[-shift:]
    
    # the initial part at the end
    upper = for_lower[:shift+1]

    return lower + upper

res = rot_list(lst, 2)
print(res)
