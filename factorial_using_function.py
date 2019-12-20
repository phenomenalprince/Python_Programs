def fact(n):
    f = 1
    if n==0 or n==1:
        print(1)
    else:
        for i in range(1,n+1):
            f = f*i
    return f
n = int(input("Enter a number :: "))
print(fact(n))
