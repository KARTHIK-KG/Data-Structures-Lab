# Write a Python program to swap first and last element of a list

List=[int(x) for x in input().split()]
i=len(List)-1
List[0],List[i]=List[i],List[0]
print(List)


# Input: 10, 25, 45, 12, 75

# Output: [75, 25, 45, 12, 10]
