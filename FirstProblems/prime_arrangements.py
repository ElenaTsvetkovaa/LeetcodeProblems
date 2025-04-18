

def num_prime_arrangements(n: int) -> int:
    MOD = 10 ** 9 + 7
    def factorial(num):
        res = 1
        for j in range(1, num + 1):
            res *= j
        return res

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

        p += 1

    primes = sum(is_prime)
    return factorial(primes) * factorial(n-primes)  % MOD

print(num_prime_arrangements(5))








