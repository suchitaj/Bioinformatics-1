def PatternCount(text, pattern):
    count = 0
    pattLen = len(pattern)
    for i in range(len(text) - pattLen  + 1):
        check = text[i : i + pattLen]
        if check == pattern:
            count += 1
    return count

def FrequentWords(text, k):
    count = {}
    maxCount = 0
    textLen = len(text)
    for i in range(textLen - k + 1):
        pattern = text[i: i + k]
        count[i] = PatternCount(text, pattern)
        if count[i] > maxCount:
            maxCount = count[i]
    frequentPatterns = {}
    for i in range(textLen - k + 1):
        if count[i] == maxCount:
            frequentPatterns[text[i: i + k]] = i
    return frequentPatterns.keys()

print(FrequentWords('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4))
