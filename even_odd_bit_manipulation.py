def is_even_odd(x):
    if x & 1 == 0:
        return "EVEN"
    else:
        return "ODD"

print(is_even_odd(5))
print(is_even_odd(8))

import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
