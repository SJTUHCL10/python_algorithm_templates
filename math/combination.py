class Combination:
    def __init__(self, mx: int=10000, mod: int=10**9+7) -> None:
        self.fact = [1] * (mx + 1)
        self.inv_fact = [1] * (mx + 1)
        self.mod = mod
        for i in range(2, mx + 1):
            self.fact[i] = self.fact[i-1] * i % mod
            self.inv_fact[i] = self.inv_fact[i-1] * self.pow(i, mod-2, mod) % mod

    def pow(self, a: int, k: int, p: int) -> int:
        res = 1
        t = a
        while k:
            if k % 2:
                res = res * t % p
            k >>= 1
            t = t * t % p
        return res
    
    def combination(self, a: int, b: int) -> int:
        return (self.fact[a] * self.inv_fact[b] % self.mod * self.inv_fact[a-b] % self.mod)
    

def main():
    comb = Combination()
    print(comb.combination(6, 2))   # 15
    print(comb.combination(10, 7))  # 120


if __name__ == '__main__':
    main()
