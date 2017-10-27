## Function definition
def check(numberArraySize, product, numbers): ##Checks if the given product can be obtained by multiplying any two numbers in the array
    for i in range(0, numberArraySize): ## Multiplies every number in the array by another element in the same array once.
        for j in range(i, numberArraySize): ## Numbers before the index 'i' have already been proven by the commutative law of multiplication (a*b=b*a)
            if int(numbers[i]) * int(numbers[j]) == product:
                print("Yes")
                return ##Interrupts the 'for' nesting and ends the test case if any evidence that satisfies the query is found
    print("No")

## Main
for x in range(0,int(input())):
    numberArraySizeAndProduct=input().split(" ") ## Both of these arguments are in a single input line, separated by space
    numbers=list(filter(None, input().split(" "))) ## Turns input line into a List. G4GPractice interface sometimes inputs empty strings into the input line, so it filters against that case.
    check(int(numberArraySizeAndProduct[0]), int(numberArraySizeAndProduct[1]), numbers)
        
