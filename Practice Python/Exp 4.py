# Write a Python program to delete particular element from the list

case=[10,20,30,40,50]
for num in case:
    if num==40:
        case.remove(40)
        
print(case)       


# Input:  10, 20, 30, 40, 50, 40 

# Output: [10, 20, 30, 50]
