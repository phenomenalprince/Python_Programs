num = int(input("Enter a number :: "))
if num==0:
    print("Factorial is ",1)
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial of",num,"is",fact,".")
import time
start_time = time.time()
print("\n--- %s seconds ---" % (time.time() - start_time))
