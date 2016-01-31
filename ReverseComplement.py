import sys

def PatternMatching(pattern, text):
    pattAppear = []
    pattLen = len(pattern)
    for i in range(len(text) - pattLen  + 1):
        if text[i: i + pattLen] == pattern:
            pattAppear.append(i)
    return pattAppear

def PatternCount(text, pattern):
    return len(PatternMatching(pattern, text))

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

def ReverseComplement(text):
    revComp = ''
    complement = {
        'A' : 'T',
        'G' : 'C',
        'T' : 'A',
        'C' : 'G'
        }
    for i in range(len(text)):
        newLetter = text[-i - 1]
        if newLetter in complement:
            revComp += complement[newLetter]
    return revComp

print(ReverseComplement('GCTAGCT'))

def PrintList(l):
    for i in l:
        print(i, end = ' ')

def ClumpFinding(Genome, k, L, t):
    output = {}
    for i in range(len(Genome) - L + 1):
        count = {}
        for j in range(L - k + 1):
            kmer = Genome[i + j : i + j + k]
            if kmer in count:
                count[kmer] += 1
            else:
                count[kmer] = 1
            if count[kmer] >= t:
                output[kmer] = count[kmer]
    return len(output.keys())

##lines = sys.stdin.read().splitlines()
###[k, L, t] = [ int(x) for x in lines[1].split()] 
##PrintList(ClumpFinding(lines[0], 9, 500, 3))

