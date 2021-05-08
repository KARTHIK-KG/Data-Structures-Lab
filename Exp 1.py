# Write a Python program to find the largest and smallest number in an unsorted array.

array=[int(x) for x in input().split()]
n=len(array)
big=small=array[0]
for i in range(1,n):
    if (array[i]>big):
        big=array[i]
    if (array[i]<small):
        small=array[i]
print("Largest value =", big)
print("Smallest value =", small)


# Input: 10, 2, 3, 15, 8

# Output: Largest value = 15,     Smallest value = 2git 