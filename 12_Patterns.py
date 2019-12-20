# Pattern 1
for i in range(1,6):
    print()
    for j in range(1,6):
        print("*",end="")
print()
# Pattern 2
for i in range(1,6):
    print()
    for j in range(i):
        print("*",end="")
print()
# Pattern 3
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(j,end=" ")
print()
# Pattern 4
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(i,end=" ")
print()
# Pattern 5
count = 0
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(count,end=" ")
        count += 1
print()
# Pattern 6
N = 5
for i in range(1,N+1):
    print()
    for k in range(N,i,-1):
        print(" ",end=" ")
    for j in range(1,i):
        print(j,end=" ")
print()
# Pattern 7
N = 5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for l in range(i-1,0,-1):
        print(l,end=" ")
    print()
print()
# Pattern 8
N = 5
for i in range(1,N+1):
    for k in range(N,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
print()
# Pattern 9
N = 5
for i in range(1,N+1):
    if i==1 or i==N:
        for j in range(1,N+1):
            print("*",end=" ")
    else:
        for k in range(1,N+1):
            if k==1 or k==N:
                print("*",end=" ")
            else:
                print("",end="  ")
    print()
print()
# Pattern 10
N = 5
for i in range(1,N+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,N+1):
    for k in range(N,i,-1):
        print("*",end="")
    print()
print()
# Pattern 11
N = 5
for i in range(1,N+1):
    for j in range(1,N+1):
        if i!=j:
            print("*",end=" ")
        else:
            print("$",end=" ")
    print()
print()
# Pattern 12
N = 5
for i in range(1,N+1):
    if i==1 or i==N:
        for j in range(1,N+1):
            if i!=j:
                print("*",end=" ")
            else:
                print("$",end=" ")
    else:
        for j in range(1,N+1):
            if j==1 or j==N:
                print("*",end=" ")
            elif j==i:
                print("$",end=" ")
            else:
                print(" ",end=" ")

    print()
print()
