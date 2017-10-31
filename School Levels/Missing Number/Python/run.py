def check(array,numIntegers): ##Checks if the missing number is 1; if not, check if the following number isn't a successor to current number, returning the missing successor if not
    if array[0]!='1':
        return 1
    for y in range(0,len(array)):
        if int(array[y])+1 != int(array[y+1 if numIntegers > y else numIntegers]):
            return int(array[y])+1 ## Returns the missing sucessor

for x in range(0,int(input())):
    numIntegers = int(input())-2 # Array of integers starts indexing from 0, minus the missing number index
    array = sorted(list(filter(None,input().split(" "))), key=int) #Sort the array to enable search logic of looking for a missing successor
    print(check(array,numIntegers))
