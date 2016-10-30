def insertion_sort(array):
    """ Sorts an array using the insertion sorting algorithm """

    if len(array) < 1:
        print("Error : Array is empty")
        return

    sorted_array = []
    sorted_array.append(array[0])

    for i in range(1, len(array)):

        # insert at the end of sorted array
        sorted_array.append(array[i])
        for j in reversed(range(0, len(sorted_array)-1)):

            # move last number at the correct index
            if sorted_array[j] > sorted_array [j+1]:
                sorted_array[j], sorted_array[j+1] = sorted_array[j+1], sorted_array[j]

        print("sorted list is : " + str(sorted_array))

    return sorted_array

def test_equal_arrays(result, expected):
	"""Checks if both array are the same"""

	if result == expected:
		print(', '.join(str(e) for e in result))
	else:
		print("ERROR, sorting failed : ")
		print(', '.join(str(e) for e in result))

array1 = [5,4,3,2,1]
print(array1)
sorted_array = insertion_sort(array1)
test_equal_arrays(sorted_array, sorted([5,4,3,2,1]))

array2 = [1,4,3,5,2]
print(array2)
sorted_array = insertion_sort(array2)
test_equal_arrays(sorted_array, sorted([1,4,3,5,2]))

array3 = [11,6,2,8,10]
print(array3)
sorted_array = insertion_sort(array3)
test_equal_arrays(sorted_array, sorted([11,6,2,8,10]))
