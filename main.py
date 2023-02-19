def pattern_count(text, pattern):
    count = 0
    for i in range(len(Text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count = count + 1
    return count


def frequency_map(text, k):
    freq = {}
    n = len(Text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        freq[pattern] = pattern_count(Text, pattern)
    return freq


def frequent_words(text, k):
    words = []
    freq = frequency_map(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
            words.sort()
    return words


Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

print(frequent_words(Text, k))
