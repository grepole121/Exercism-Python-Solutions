def primes(limit):
    not_primes = []
    prime = []
    for num in range(2, limit+1):
        if num not in not_primes:
            prime.append(num)
            for not_prime in range(num*num, limit+1, num):
                not_primes.append(not_prime)
    return prime
