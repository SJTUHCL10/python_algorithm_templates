# Binary Exponentiation
# 快速幂
# a ^ b mod p

# iteration version
def binpow(a, b, p):
    res = 1
    t = a
    while b:
        if b % 2:
            res = res * t % p
        t = t * t % p
        b >>= 1
    return res

# recursion version
def binpow_rec(a, b, p):
    if b == 0:
        return 1
    res = binpow_rec(a, b//2, p)
    res = res * res % p
    if b % 2:
        res = res * a % p
    return res
