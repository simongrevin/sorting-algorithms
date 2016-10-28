

def binarySearch(array, toFind):
    print("searching...")
    found=False
    high = len(array)
    searched = len(array)/2
    print("len/2 = " + str(searched) )
    while(not found):
        print("trying " + str(array[searched]))
        if array[searched] == toFind:
            found = True
            return searched
        else:
            if array[searched] > toFind:
                high = searched
                searched = searched / 2
            else:
                high = high
                searched = searched + ((high - searched) / 2)


array = [1, 3, 4, 6, 8, 9, 10, 14, 34]
result = binarySearch(array, 6)
print("Result = " + str(result))
