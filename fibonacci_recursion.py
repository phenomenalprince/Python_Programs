def fib(n):
    if n<2:
        return 1
    else:
        return (fib(n-1)+fib(n-2))
n = int(input("Enter a no. :: "))
for i in range(n):
    print("Fibonacci(",i,") = ",fib(i))
