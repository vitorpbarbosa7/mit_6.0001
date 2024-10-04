import string

l = string.ascii_lowercase
u = string.ascii_uppercase

print(l)
print(u)

i = 1
new_list = []
_len = 26
for ch in l:
    new_list.append(_len - i + 1)

