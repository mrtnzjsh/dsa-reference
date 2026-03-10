"""
Robin-Karp algorithm for pattern matching using rolling hash technique.

Algorithm Overview:
- Uses rolling hash to efficiently compare pattern against text substrings
- Calculates hash of pattern and compares with hash of text window
- If hashes match, performs direct character comparison to verify
- Rolling hash allows O(1) hash update when moving to next position
- Best for multiple pattern matching due to hash-based filtering

Rolling Hash Technique:
- Hash of string s = (s[0] × b^(m-1) + s[1] × b^(m-2) + ... + s[m-1] × b^0) mod p
- Where b = base, p = prime
- Precompute highest power: h = b^(m-1) mod p
- This precomputed value allows efficient hash updates

Hash Computation Steps:
1. Initialize pattern_hash and text_hash to 0
2. For each character in pattern/text (length m):
   - pattern_hash = (base × pattern_hash + char) mod prime
   - text_hash = (base × text_hash + char) mod prime
   - This builds hash value iteratively

Matching Process:
1. For each possible starting position s (0 to n-m):
   - Compare pattern_hash with text_hash
   - If hashes equal: potentially a match, verify with direct comparison
     * If all characters match: print "Pattern found at index", s
   - Calculate rolling hash for next position:
     * text_hash = (base × (text_hash - text[s] × h) + text[s+m]) mod prime
     * Subtract contribution of outgoing character: text_hash - text[s] × h
     * Multiply by base to shift remaining hash
     * Add contribution of new character: text[s+m]
   - Handle negative hash: add prime if result < 0

Rolling Hash Formula Derivation:
- Current hash H = (s[0] × b^(m-1) + s[1] × b^(m-2) + ... + s[m-1]) mod p
- For next position s+1: new characters are s[1] to s[m]
- H_next = (s[1] × b^(m-1) + s[2] × b^(m-2) + ... + s[m]) mod p
- H = s[0] × b^(m-1) + H_before_remove + s[m-1]
- H_before_remove = (s[1] × b^(m-1) + s[2] × b^(m-2) + ... + s[m-2]) mod p
- H_next = (base × (H - text[s] × h) + text[s+m]) mod p

Why Use Different Base and Prime:
- Base: Typically 101, 256 (number of characters in alphabet)
- Prime: Large prime (10^9+7) to reduce hash collisions
- Choice affects collision frequency and speed

Time Complexity Analysis:
- Hash computation: O(m) for pattern + O(m) for initial text window = O(m)
- Each hash comparison: O(1) average (just integer comparison)
- Verification (when hashes match): O(m) in worst case
- Rolling hash update: O(1) per position
- Total: O(n + m) for hash operations + O(n × m) for verifications
- Average case: O(n + m) (hashes rarely collide)
- Worst case: O(n × m) (many hash collisions requiring full comparison)

Space Complexity: O(1)
- Only stores hash values and precomputed powers
- No additional data structures proportional to input size

Collision Handling:
- Hash collisions can occur but are unlikely with good base and prime
- Direct character comparison resolves collisions
- Raising base and prime reduces collision probability

Advantages:
- Faster than naive O(n × m) when most hash comparisons are O(1)
- Handles multiple patterns efficiently (compare hashes first)
- Rolling hash makes hash updates O(1)
- No backtracking needed

Disadvantages:
- Hash collisions can degrade performance to O(n × m)
- Requires careful choice of base and prime
- Not as efficient as KMP for single pattern matching
- More complex implementation

Use Cases:
- Multiple pattern matching (e.g., find many words in text)
- DNA sequence matching
- File content detection (similar files have similar hashes)
- When hash comparison is expected to be much faster than direct comparison

Typical Parameters:
- base = 101 or 256 (number of characters)
- prime = 10^9+7 or 2^31-1 (large prime)
- Works well for lowercase English letters
"""

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
