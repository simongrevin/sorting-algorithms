import numpy as np

def merge_sort(array):
    """ Sorts an array using the merge sorting algorithm """

    print("==========")
    print("array is : " + str(array))
    return merge(np.array_split(array, 2)[0], np.array_split(array, 2)[1])


def merge(left, right):

    print("------------------>")
    print ("left is : " + str(left))
    print ("right is : " + str(right))


    if len(left) == 1 and len(right) == 1:
        if left[0] < right[0] :
            print("Sorting : is : " + str(np.append(left, right)))
            return np.append(left, right)
        else:
            print("Sorting : is : " + str(np.append(right, left)))
            return np.append(right, left)
    elif len(left) == 1 and len(right) > 1:
        return np.append(left, merge(np.array_split(right, 2)[0], np.array_split(right, 2)[1]))
    elif len(left) > 1 and len(right) == 1:
        return np.append(merge(np.array_split(left, 2)[0], np.array_split(left, 2)[1]), right)
    elif len(left) > 1 and len(right) > 1:
        return np.append(merge(np.array_split(left, 2)[0], np.array_split(left, 2)[1]), merge(np.array_split(right, 2)[0], np.array_split(right, 2)[1]))


# TODO : use both merge and merge_sort recursively



array = np.array([38, 27, 43, 3, 9, 82, 10])
array1 = np.array([10, 5])

final = merge_sort(array)

print("final : " + str(final))
