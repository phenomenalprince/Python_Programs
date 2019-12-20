#sum of sqaures of even no.
n = int(input("Enter a number :: "))
s = 0
for i in range(1,n+1):
    if i%2 == 0 :
        term = i**2
    else:
        term = 0
    s = s + term
print(s)
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
