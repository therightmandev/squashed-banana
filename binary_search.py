# todo
# find element's index 
# bsearch(3, [1, 2, 3]) returns 2
# bsearch(5, [1, 2, 3]) returns -1


def bsearch(value, array, add_to_index=0):
    if len(array) == 0:
        return -1

    index = len(array) // 2

    if array[index] == value:
        return index + add_to_index
    elif value < array[index]:
        return bsearch(value, array[:index], add_to_index)
    else:
        return bsearch(value, array[index+1:], add_to_index + index + 1)



assert bsearch(3, [1, 2, 3, 4]) == 2
assert bsearch(2, [1, 2, 3, 4]) == 1
assert bsearch(4, [1, 2, 3, 4]) == 3
assert bsearch(1, [1, 2, 3, 4]) == 0
assert bsearch(1, [1, 2, 3, 4, 5]) == 0
assert bsearch(5, [1, 2, 3, 4, 5]) == 4
assert bsearch(4, [1, 2, 3, 4, 5]) == 3
assert bsearch(3, []) == -1
assert bsearch(4, [4]) == 0
assert bsearch(4, [4], 3) == 3
assert bsearch(6, [1, 2, 3, 4, 5]) == -1
assert bsearch(3, [1, 2, 4, 5]) == -1
assert bsearch(6, [1, 2, 3, 4, 5, 6]) == 5
assert bsearch(2, [1, 2, 3, 4, 5, 6]) == 1
assert bsearch(3, [1, 2, 3, 4, 5, 6]) == 2
assert bsearch(4, [1, 2, 3, 4, 5, 6]) == 3
assert bsearch(2, [1, 2, 3, 4, 5]) == 1
