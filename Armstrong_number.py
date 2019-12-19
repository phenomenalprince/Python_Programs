n = int(input("Enter a number :: "))
num = n
s = 0
while(n>0):
    r = n%10
    s = s + (r**3)
    n = n//10
print(s)
if (s==num):
    print("Yes, an armstrong number.")
else:
    print("Not an armstrong number.")
import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
