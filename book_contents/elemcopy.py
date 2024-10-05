# this makes the copy
# that strange behaviour in python (and they told me that also in another languages)
# that it keeps a reference, so must make copies of lists and dataframes, (and other data structures)
# for functions, for example
elems_copy = elems[:]

for item in elems_copy:
    if not condition:
        elems.remove(item)
