def get_primes(n):
    """Get all primes p <= n. O(n) complexity."""
    is_prime = [1] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if p * i > n:
                break
            is_prime[p * i] = 0
            if i % p == 0:
                break
    return primes


def main():
    print(get_primes(100))


if __name__ == '__main__':
    main()
