import FrequencyMap


def frequent_words(text, k):
    words = []
    freq = FrequencyMap.frequency_map(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            words.append(key)
            words.sort()
    return words
