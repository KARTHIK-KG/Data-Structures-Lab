# Write a python program to check whether a given number is prime number or not

num=int(input())
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            break
        else:
            print(num,"is a prime number")


# Input: 3  Output:  3 is a prime number

# Input: 6  Output:  6 is not a prime number
