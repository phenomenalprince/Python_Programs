for n in range(1,100):
    count = 0
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            count+=1
            break
    if count==0 and n!=1:
        print(n,end=" ")  

import time
start_time = time.time()
print("\n--- %s seconds ---" % (time.time() - start_time))
