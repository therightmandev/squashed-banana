# todo
# find element's index 
# bsearch(3, [1, 2, 3]) returns 2
# bsearch(5, [1, 2, 3]) returns -1


def bsearch(value, array):
    index = len(array) // 2
    if array[index] == value:
        return index
    elif value < array[index]:
        index = index // 2
        if array[index] == value:
            return index
    else:
        index += (len(array) - index) // 2
        return index



assert bsearch(3, [1, 2, 3, 4]) == 2
assert bsearch(2, [1, 2, 3, 4]) == 1
assert bsearch(4, [1, 2, 3, 4]) == 3
