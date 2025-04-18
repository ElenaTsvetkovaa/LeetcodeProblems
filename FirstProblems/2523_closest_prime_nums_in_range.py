from typing import List


def closest_primes(left: int, right: int) -> List[int]:
    is_prime = [True] * (right + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(right ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, right + 1, i):
                if j % i == 0:
                    is_prime[j] = False

    primes = []
    for i in range(max(2, left), right + 1):
        if is_prime[i]:
            primes.append(i)

    if len(primes) < 2:
        return [-1, -1]

    res = []
    min_change = 10 ** 6
    for i in range(len(primes) - 1):
        if primes[i+1] - primes[i] < min_change:
            min_change = primes[i+1] - primes[i]
            res = [primes[i], primes[i+1]]
    return res

print(closest_primes(10, 50))










