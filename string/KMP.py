def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    positions = []
    M = len(pattern)
    N = len(text)

    lps = compute_lps(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == M:
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return positions


def main():
    text = "ABABDABACDABABCABAB"
    pattern = "ABAB"
    matches = kmp_search(text, pattern)
    print(matches)  # [0, 10, 15]


if __name__ == '__main__':
    main()
