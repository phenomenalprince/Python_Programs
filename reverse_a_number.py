num = int(input("Enter a number :: "))
while num!=0:
    rem = num%10
    print(rem,end="")
    num //= 10 # num = num//10

import time
start_time = time.time()
print("\n--- %s seconds ---" % (time.time() - start_time))
