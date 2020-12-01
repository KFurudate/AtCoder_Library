def sieve_eratosthenes(num):
    import numpy as np

    primes = np.zeros(num + 1, dtype=np.bool)
    primes[2] = 1
    primes[3::2] = 1
    for p in range(3, num + 1, 2):
        if primes[p]:
            primes[p * p::2 * p] = 0
    return primes


n = int(input())
if n <= 2:
  print(0)
  exit()
ans = sieve_eratosthenes(n-1).sum()
print(ans)