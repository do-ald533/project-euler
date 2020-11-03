def is_prime(n):
    """
    Returns True if the number n is a prime number. Otherwise returns False
    """
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


prime = 0
number = 1555
for n in range(1, number + 1):
    if(is_prime(n) == True):
       if number % n == 0:
            if n > prime:
                prime = n
print(f"{prime} is the largest prime factor for the number {number}")