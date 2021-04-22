# Write a PYTHON PROGRAM to check whether given number is a armstrong number or not

n=int(input())
q=n
num=0
sum=0
while q>0:
    rem=q%10
    sum=sum+rem**3
    q=q//10
if n==sum:
    print("ARMSTRONG NUMBER")
else:
  print ("NOT A ARMSTRONG NUMBER")


# Input: 153    Output:  ARMSTRONG NUMBER

# Input: 123    Output:  NOT A ARMSTRONG NUMBER
