def isPalindrome(s):
    return s == s[::-1]  # [::-1] means that we are reading the string fronm right to left taking each element.

s = input("Enter the string: ")
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")