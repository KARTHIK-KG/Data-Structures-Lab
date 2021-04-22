# Write a python program to find factorial of a given number

n=int(input())
def calc(n):
    fact=1
    if n==-5:
        return "Factorial does not exist for negative numbers"
    for i in range(1,n+1):
        fact*=i
    return fact
print(calc(n))
