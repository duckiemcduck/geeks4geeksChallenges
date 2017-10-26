for x in range(0,int(input())): #Settles number of test cases
    arraySize = int(input()) #Defines top boundary for the array of the active test case
    elements = list(filter(None, input().split(" "))) #Turns element input into a List, removes empty strings from the List
    if elements[:arraySize][::-1] != elements[:arraySize] : #Compares if the reversed List up to the boundary is not equal to the standard List up to the boundary
        print("NOT PERFECT")
    else:
        print("PERFECT")
   
	#Retroactively speaking, the input for the top boundary could be less than the actual size of the array that got input, forcing the need for the split in the comparison,
	#which may or may not be redundant at times.
