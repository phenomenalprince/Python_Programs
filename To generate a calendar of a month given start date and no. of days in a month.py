# To generate a calendar of a month given start date and no. of days in a month
start_day = int(input("Enter a start date :: ")) # enter from 1-7
n = int(input("Enter no. of days in a month :: "))
print("Mon","Tues","Wed","Thurs","Fri","Sat","Sun")
print("------------------------------------------")
for i in range(start_day-1):
    print(end="*****")
i = start_day-1
for j in range(1,n+1):
    if i>6:
        print()
        i = 1 
    else:
        i = i + 1
    print(str(j)+" ",end=" ")

import time
start_time = time.time()
print("\n--- %s seconds ---" % (time.time() - start_time))
