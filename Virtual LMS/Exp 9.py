year=int(input())
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
            print("Not a Leap Year")
else:
    print("Not a Leap Year")    


# Input:  2000   Output:  Leap Year