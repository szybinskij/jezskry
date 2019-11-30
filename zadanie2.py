def sortSecond(list_element): return list_element[1]


def sortThird(list_element): return list_element[2]


list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 0, 3]]
print(list_to_sort)

list_to_sort.sort(key=sortThird)
print(list_to_sort)
list_to_sort.sort(key=sortSecond)
print(list_to_sort)


print('wer2 lambda')
list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 0, 3]]
print(list_to_sort)

list_to_sort.sort(key=lambda x: (x[1],x[2]))
print(list_to_sort)