"""Knuth-Morris-Pratt (KMP) algorithm for pattern matching."""

def preprocess(process_string: str) -> list:
    m = len(process_string)
    lps = [0] * m
    max_lps = 0
    i = 1

    while i < m:
        if process_string[i] == process_string[max_lps]:
            max_lps += 1
            lps[i] = max_lps
            i += 1
        else:
            if max_lps != 0:
                max_lps = lps[max_lps - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_algorithm(pattern: str, text: str):
    m = len(pattern)
    n = len(text)

    lps = preprocess(pattern)

    i, j = 0, 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
            if j == m:
                print("Pattern found at index", (i - j))
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
