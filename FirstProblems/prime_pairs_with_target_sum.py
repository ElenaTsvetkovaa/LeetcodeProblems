from typing import List


def find_prime_pairs(n: int) -> List[List[int]]:

    if n < 2:
        return []

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                if j % i == 0:
                    is_prime[j] = False

    primes = [i for i in range(n+1) if is_prime[i]]
    primes_set = set(primes)
    best_pairs = []

    for p in primes:
        searched_el = n - p

        if searched_el >= p and searched_el in primes_set:
            best_pairs.append([p, searched_el])

    return best_pairs

print(find_prime_pairs(262))