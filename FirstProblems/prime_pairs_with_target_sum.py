from typing import List


def find_prime_pairs(n: int) -> List[List[int]]:
    #
    # if n < 2:
    #     return []
    #
    # is_prime = [True] * (n + 1)
    # is_prime[0] = is_prime[1] = False
    #
    # for i in range(2, int(n ** 0.5) + 1):
    #     if is_prime[i]:
    #         for j in range(i * i, n + 1, i):
    #             if j % i == 0:
    #                 is_prime[j] = False
    #
    # primes = [i for i in range(n+1) if is_prime[i]]
    # primes_set = set(primes)
    # best_pairs = []
    #
    # for p in primes:
    #     searched_el = n - p
    #
    #     if searched_el >= p and searched_el in primes_set:
    #         best_pairs.append([p, searched_el])
    #
    # return best_pairs
    prime = [True] * (n + 1)  # List to store whether a number is prime or not
    ans = []  # List to store the pairs of prime numbers

    prime[1] = False  # 1 is not a prime number
    prime[0] = False  # 0 is not a prime number

    # Finding prime numbers using the Sieve of Eratosthenes algorithm
    p = 2
    while p * p <= n:
        if prime[p]:
            # Marking multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    for i in range(2, n):
        j = n - i  # Finding the complement of i to make the sum n
        if prime[i] and prime[j] and i <= j:
            temp = [i, j]  # Creating a pair of prime numbers
            ans.append(temp)  # Adding the pair to the result list

    return ans  # Returning the list of prime pairs


print(find_prime_pairs(262))