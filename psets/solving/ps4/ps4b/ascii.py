import string

l = string.ascii_lowercase
u = string.ascii_uppercase

print(l)
print(u)

def rot_list(lst, shift):

    shift = shift % len(lst)

    for_upper = lst[:]
    for_lower = lst[:]
    # the final part at the beginning
    lower = for_lower[-shift:]
    
    till = len(lst) - shift
    # the initial part at the end
    upper = for_upper[:till]

    return lower + upper


print(rot_list(l, 1))
print(rot_list(l, 2))
print(rot_list(l, 3))
