def filter_list(l):
    'return a new list with the strings filtered out'
    l2 = []
    for i in l:
        if type(i) == int:
            l2.append(i)

    return l2
print(filter_list([1,2,'a','b']))