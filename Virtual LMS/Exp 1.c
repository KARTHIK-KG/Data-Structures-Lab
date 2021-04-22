// Write a C program to find the search element in an array using Linear Search.

#include <stdio.h>
int main()
{
  int array[100], search, c, n;

 
  scanf("%d", &n);

 
  for (c = 0; c < n; c++)
    scanf("%d", &array[c]);

 
  scanf("%d", &search);

  for (c = 0; c < n; c++)
  {
    if (array[c] == search)
    {
      printf("%d \n", c+1);
      break;
    }
  }
  if (c == n)
    printf("%d isn't present in the array.\n", search);

  return 0;
}


// Input: 5, 10, 20, 30, 40, 50, 20

// Output: 2

