import PatternCount


def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        freq[pattern] = PatternCount.pattern_count(text, pattern)
    return freq
