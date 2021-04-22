# Write a Python program to check whether the given character is vowel or consonant.

ch=input()
if(ch in('a','A','e','E','i','I','o','O','u','U')):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")