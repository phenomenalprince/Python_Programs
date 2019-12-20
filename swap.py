def swap(a,b):
    print("Before swap")
    print(a,b)
    a,b = b,a
    print("After Swap")
    print(a,b)
a = int(input("Enter a no. :: ))
b = int(input("Enter a no. :: ))
swap(a,b)
