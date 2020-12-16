# Summation of primes
### The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
### Find the sum of all the primes below two million.

## Solution:
i've approached this problem utilizing a algorithm called "Sieve of Eratosthenes". This algorithm takes in a number(in our case 2000000) and goes through every prime number taking out it's multiples, so when the prime number is 2, the algorithm "deletes" it's multiples(4,6,8).

Since this problem is a math intensive problem i used *Golang* as my language of choice.