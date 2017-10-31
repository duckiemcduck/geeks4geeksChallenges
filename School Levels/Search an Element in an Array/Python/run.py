#code
for x in range(0,int(input())):
    sizeArray = int(input())
    array = input().split(" ")
    try:
        print(array[:sizeArray].index(input())) #Python's index() basically destroys this challenge, returning the index of the requested value
    except ValueError: #if the value is not in the array, it will raise this exception
        print(-1)
