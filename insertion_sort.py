

def insertion_sort(array):

    print(array)



def test_equal_arrays(result, expected):
	"""Checks if both array are the same"""

	if result == expected:
		print(', '.join(str(e) for e in result))
	else:
		print("ERROR during sorting : ")
		print(', '.join(str(e) for e in result))

array1 = [5,4,3,2,1]
print(array1)
insertion_sort(array1)
test_equal_arrays(array1, sorted([5,4,3,2,1]))

array2 = [1,4,3,5,2]
print(array2)
insertion_sort(array2)
test_equal_arrays(array2, sorted([1,2,3,4,5]))

array3 = [11,6,2,8,10]
print(array3)
insertion_sort(array3)
test_equal_arrays(array3, sorted([11,6,2,8,10]))
