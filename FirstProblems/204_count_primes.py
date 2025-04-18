from math import sqrt, ceil


def count_primes(num):
    if num <= 2:
        return 0

    non_primes = set()

    for n in range(2, int(num ** 0.5) + 1):
        if n not in non_primes:
            for p in range(n * n, num, n):
                if p % n == 0:
                    non_primes.add(p)
    return len([x for x in range(2, num) if x not in non_primes])


print(count_primes(10))
