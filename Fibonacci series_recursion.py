def Fibionacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return Fibionacci(n-1) + Fibionacci(n-2)

n = int(input("Enter the range of numbers: "))
for i in range(0, n):
    print(Fibionacci(i))