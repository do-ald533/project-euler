from functools import lru_cache
import time
startTime = time.time()


@lru_cache(maxsize = 1000)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

soma = 0
    
for n in range(1,51):
    print(n, ":", fib(n))
    if(fib(n) % 2 == 0):
        soma+= fib(n)
print(f"the sum of all even numbers is:{soma}")