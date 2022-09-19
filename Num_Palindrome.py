num = int(input("Enter the number: "))
num = str(num)

if num == num[::-1]:
    print(num, "is palindrome")
else:
    print(num, "is not palindrome")