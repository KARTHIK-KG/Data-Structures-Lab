# Write a  Python program to perform linear search and find the element in the list 

arr=[int(x) for x in input().split()]
n= int(input())
c=0
for i in range(len(arr)):
    if n==arr[i]:
        print(i+1)
        c=1
        break
if c==0:
    print("The Element is not found")


# Input: 10, 25, 45, 12, 75, 45        Output:  3

# Input: 10, 25, 45, 12, 75, 45, 77    Output:  The Element is not found

