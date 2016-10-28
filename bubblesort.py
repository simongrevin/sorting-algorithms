

def bubbleSortThis(array):
	print("Sorting...")
	for i in range(0, len(array)-1):
		change=False
		for x in range(0, len(array)-1):
			if array[x] > array[x+1]:
				change=True
				array[x], array[x+1] = array[x+1], array[x]
		if not change:
			break

def testEqualArrays(result, expected):
	if result == expected:
		print(', '.join(str(e) for e in result))
	else:
		print("ERROR during sorting : ")
		print(', '.join(str(e) for e in result))




print(array1)
array1 = [5,4,3,2,1]
bubbleSortThis(array1)
testEqualArrays(array1, sorted([5,4,3,2,1]))

array2 = [1,4,3,5,2]
print(array2)
bubbleSortThis(array2)
testEqualArrays(array2, sorted([1,2,3,4,5]))

array3 = [11,6,2,8,10]
print(array3)
bubbleSortThis(array3)
testEqualArrays(array3, sorted([11,6,2,8,10]))
