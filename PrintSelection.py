import FrequentWords
import FrequencyMap
import PatternCount

text = "TCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACA" \
       "TCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCT" \
       "TGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTG" \
       "ACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACG" \
       "GTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACG" \
       "ATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAG" \
       "CTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

k = 10

pattern = "TGT"

patternText = "ACTGTACGATGATGTGTGTCAAAG"


def print_frequent_words():
    print(FrequentWords.frequent_words(text, k))


def print_frequency_map():
    print(FrequencyMap.frequency_map(text, k))


def print_pattern_count():
    print(PatternCount.pattern_count(patternText, pattern))
