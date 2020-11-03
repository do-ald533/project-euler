from functools import lru_cache


@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


soma = 0  
for n in range(1,51):
    print(n, ":", fibonacci(n))
    if(fibonacci(n) % 2 == 0):
        soma+= fibonacci(n)
print(f"the sum of all even numbers is:{soma}")