num1 = int(input("Enter a number :: "))
num2 = int(input("Enter a number :: "))
if num1>num2:
    dividend = num1
    divisor = num2
else:
    dividend = num2
    divisor = num1
while(divisor!=0):
    rem = dividend%divisor
    dividend = divisor
    divisor = rem
print("GCD of",num1,"and",num2,"=",dividend,".")
import time
start_time = time.time()
print("\n--- %s seconds ---" % (time.time() - start_time))
