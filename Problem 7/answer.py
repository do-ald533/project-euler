def is_prime(n):
    """
    return True if the number n is a prime number, else return False
    """
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


def prime_index(idx):
    """
    returns the prime number equivalent to the index input
    """
    n = 2
    n_primes = 1
    while n_primes < idx:
        n += 1
        if(is_prime(n)):
            n_primes += 1
    return n


print(prime_index(10001))
