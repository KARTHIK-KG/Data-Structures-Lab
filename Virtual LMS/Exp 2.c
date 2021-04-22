// Write a C program to find the average of n elements in an array

#include<stdio.h>
int main()
{
    int a[100],n,sum=0,avg;
    scanf("%d",&n);
    for(int i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }
    for(int i=0; i<n; i++)
    {
        sum+=a[i];
    }
    avg=sum/n;
    printf("%d",avg);
    return 0;
}


// Input: 5, 5, 10, 15, 20, 25

// Output: 15