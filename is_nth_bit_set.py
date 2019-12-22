def is_nth_bit_set(x: int,n: int):
    if x & (1<<n):
        return True
    else:
        return False
print(is_nth_bit_set(6,2))
print(is_nth_bit_set(6,0))
print(is_nth_bit_set(15,3))

import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
