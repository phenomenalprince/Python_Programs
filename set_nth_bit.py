def set_nth_bit(x:int,n:int):
    return x|(1<<n),bin(x|(1<<n))[2:]

print(set_nth_bit(5,1))
print(set_nth_bit(15,4))

import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
