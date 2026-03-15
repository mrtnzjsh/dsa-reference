

def robin_karp(pattern: str, text: str, base: int, prime: int):
    m = len(pattern)
    n = len(text)

    h = 1
    for i in range(0, m - 1):
        h = (h * base) % prime

    pattern_hash = 0
    text_hash = 0

    for i in range(0, m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for s in range(0, (n - m) + 1):
        if pattern_hash == text_hash:
            for i in range(0, m):
                if text[s + i] != pattern[i]:
                    break
                else:
                    print("Pattern found at index", s)

        if s < n - m:
            text_hash = (base * (text_hash - ord(text[s]) * h) + ord(text[s + m])) % prime
            if text_hash < 0:
                text_hash += prime
