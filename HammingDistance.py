import sys

def PatternToNumber(Pattern):
    textValDict = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
        }
    sumNum = 0
    for i in range(len(Pattern)):
        textVal = textValDict[Pattern[i]]
        sumNum += textVal*(4**(len(Pattern) - i - 1))
    return sumNum

def NumberToPattern(index, k):
    textValDict = {
        '0': 'A',
        '1': 'C',
        '2': 'G',
        '3': 'T'
        }
    numString = ''
    pattern = ''
    quotient = index
    remainder = 0
    for i in range(k):
        remainder = quotient%4
        quotient = quotient//4
        numString += str(remainder)
    newString = numString[::-1]
    for l in range(len(newString)):
        textVal = textValDict[newString[l]]
        pattern += textVal
    return pattern

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

def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

def PatternMatching(Pattern, Text, d):
    matchList = []
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Pattern, Text[i: i + len(Pattern)]) <= d:
            matchList.append(i)
    return matchList

def NewFrequentWords(Pattern, Text, d):
    # ApproximatePatternCount is the same as NewFrequentWords
    return len(PatternMatching(Pattern, Text, d))

def ImmediateNeighbors(Pattern):
    nucleotides = ['A', 'C', 'G', 'T']
    Neighborhood = [Pattern]
    for i in range(len(Pattern)):
        symbol = Pattern[i]
        for x in nucleotides:
            if x != symbol:
                Neighbor = Pattern[: i] + x + Pattern[i + 1 :]
                Neighborhood.append(Neighbor)
    return Neighborhood

def Neighbors(Pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return Pattern
    if len(Pattern) == 1: 
        return nucleotides
    Neighborhood = []
    SuffixNeighbors = Neighbors(Pattern[1:], d)
    for text in SuffixNeighbors:
        if HammingDistance(Pattern[1:], text) < d:
            for x in nucleotides:
                Neighborhood.append(x + text)
        else:
            Neighborhood.append(Pattern[0] + text)
    return Neighborhood

def FrequentWordsWithMismatches(Text, k, d):
    FrequencyArray = {}
    Close = {}
    for i in range(4**k):
        Close[i] = 0
        FrequencyArray[i] = 0
    for i in range(len(Text) - k + 1):
        Neighborhood = Neighbors(Text[i: i + k], d)
        for Pattern in Neighborhood:
            index = PatternToNumber(Pattern)
            Close[index] = 1
    for i in range(4**k):
        if Close[i] == 1:
            Pattern = NumberToPattern(i, k)
            FrequencyArray[i] = NewFrequentWords(Pattern, Text, d)
    maxCount = 0
    for value in FrequencyArray.values():    
        if value > maxCount:
            maxCount = value
    FrequentPatterns = []
    for i in range(4**k):
        if FrequencyArray[i] == maxCount:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

def FrequentWordsWithMismatchesandRevComps(Text, k, d):
    FrequencyArray = {}
    Close = {}
    for i in range(4**k):
        Close[i] = 0
        FrequencyArray[i] = 0
    for i in range(len(Text) - k + 1):
        Neighborhood = Neighbors(Text[i: i + k], d)
        for Pattern in Neighborhood:
            index = PatternToNumber(Pattern)
            Close[index] = 1
    for i in range(4**k):
        if Close[i] == 1:
            Pattern = NumberToPattern(i, k)
            countkmer = NewFrequentWords(Pattern, Text, d)
            PatternRC = ReverseComplement(Pattern)
            countkmerRC = NewFrequentWords(PatternRC, Text, d)
            FrequencyArray[i] = countkmer + countkmerRC
    maxCount = 0
    for value in FrequencyArray.values():    
        if value > maxCount:
            maxCount = value
    FrequentPatterns = []
    for i in range(4**k):
        if FrequencyArray[i] == maxCount:
            Pattern = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return FrequentPatterns

def PrintListSpace(l):
    for i in l:
        print(i, end = ' ')
    print()

def PrintListLine(l):
    for i in l:
        print(i)
    print()

##lines = sys.stdin.read().splitlines()
##k,d = [int(x) for x in lines[1].split()]
##PrintListSpace(FrequentWordsWithMismatchesandRevComps(lines[0], k, d))
##
