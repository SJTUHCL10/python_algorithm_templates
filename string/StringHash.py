class StringHash():
    def __init__(self, s: str, base: int = 131, mod: int = 1 << 64) -> None:
        self.BASE = base
        self.MOD = mod
        n = len(s)
        h = [0] * (n + 1)   # prefix hash
        p = [1] * (n + 1)   # p[i] = BASE ^ i % MOD
        for i in range(1, n + 1):
            p[i] = (p[i-1] * base) % mod
            h[i] = (h[i-1] * base + ord(s[i-1])) % mod
        self.h = h
        self.p = p

    def get_hash(self, left: int, right: int) -> int:
        """
        return hash of s[l:r]
        """
        return (self.h[right] - self.h[left] * self.p[right-left] % self.MOD) % self.MOD


def main():
    s = "abcdabcef"
    sh = StringHash(s)
    print(sh.get_hash(0, 3) == sh.get_hash(4, 7))   # True
    print(sh.get_hash(1, 4) == sh.get_hash(5, 8))   # False


if __name__ == '__main__':
    main()
