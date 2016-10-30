

def bubble_sort(array):
	"""Sorts an array using the buble sort algorithm"""

	print("Sorting...")

	for i in range(0, len(array)-1):
		change = False
		for x in range(0, len(array)-1):
			if array[x] > array[x+1]:
				change = True
				array[x], array[x+1] = array[x+1], array[x]
		if not change:
			break

def test_equal_arrays(result, expected):
	"""Checks if both array are the same"""
	
	if result == expected:
		print(', '.join(str(e) for e in result))
	else:
		print("ERROR during sorting : ")
		print(', '.join(str(e) for e in result))




print(array1)
array1 = [5,4,3,2,1]
bubble_sort(array1)
test_equal_arrays(array1, sorted([5,4,3,2,1]))

array2 = [1,4,3,5,2]
print(array2)
bubble_sort(array2)
test_equal_arrays(array2, sorted([1,2,3,4,5]))

array3 = [11,6,2,8,10]
print(array3)
bubbleSortThis(array3)
test_equal_arrays(array3, sorted([11,6,2,8,10]))
