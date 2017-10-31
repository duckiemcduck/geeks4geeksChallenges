## This code was written by a different participant from myself named Akhilayamala, and proposes an interesting and elegant solution to the proposed challenge 
# Link to submission: http://practice.geeksforgeeks.org/viewSol.php?subId=4354407&pid=1533&user=Akhilyamala

#code
t = int(input())
for _ in range(t): #Number of test cases
    n = int(input()) #Amount of numbers
    a = [int(s) for s in input().split()] #Split input of numbers into a list, returning integers converted from the input elements to an implicit list constructor
    print(round(n*(n+1)/2 - sum(a))) #This mathematical equation will return the missing number in the sequence


## Proof under construction ##

## Since the sequence follows the set
# a_n = {n, n ∈  ℤ} (not sure if this set is correct?)

#a_1..4 = 1, 2, 3, 4 (n=4)
#sum(a_n) = 10

#b_1..5 = 1, 2, 3, 4, 5 (n=5)
#sum(b_n) = 15

#c_1..6 = 1, 2, 3, 4, 5, 6 (n=6)
#sum(c_n) = 21

#d_1..7 = 1, 2, 3, 4, 5, 6, 7 (n=7)
#sum(d_n) = 28

## We can observe that
#sum(A_n) = n * (n+1) / 2
