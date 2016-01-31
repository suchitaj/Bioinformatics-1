'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic
Problem Title: Greedy Motif Search with Pseudocounts
Find all (k,d) motifs in a collection of strings.
Input: A collection of strings, Dna, and integers, k, and d,
Output:All (, d) motifs in a Dna

URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Motif-Finding-Is-More-Difficult-Than-You-Think-156/#step-7

'''

import sys

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

def MotifEnumeration(Dna, k, d):
    Patterns = []
    for Pattern in Dna:
        for i in range(len(Pattern) - k + 1):
            kmer = Pattern[i: i + k]
            for newPattern in Neighbors(kmer, d):
                count = 0
                for Pattern in Dna:
                    if len(PatternMatching(newPattern, Pattern, d)) != 0:
                        count += 1
                if count == len(Dna):
                    Patterns.append(newPattern)
    return list(set(Patterns))

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    distance = 0
    for Text in Dna:
        Hamming = float("inf")
        for i in range(len(Text) - k + 1):
            newPattern = Text[i: i + k]
            if Hamming > HammingDistance(Pattern, newPattern):
                Hamming = HammingDistance(Pattern, newPattern)
        distance += Hamming
    return distance

def MedianString(Dna, k):
    distance = float("inf")
    for i in range(4**k):
        Pattern = NumberToPattern(i, k)
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median = Pattern
    return Median

def ProfileMostProbableKmer(Text, k, Profile):
    greatestProbability = 0.0
    newPattern = Text[:k]
    for i in range(len(Text) - k + 1):
        Pattern = Text[i: i + k]
        Probability = 1.0
        for j in range(k):
            Probability = Probability * Profile[Pattern[j]][j]
        if Probability > greatestProbability:
            greatestProbability = Probability
            newPattern = Pattern
    return newPattern

def MakeProfileMatrix(motifs, k):
    matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    for key in matrix.keys():
        for i in range(k):
            matrix[key].append(float(0.0))
    for motif in motifs:
        for i in range(len(motif)):
            matrix[motif[i]][i] += 1
    t = len(motifs)
    for key in matrix.keys():
        for i in range(k):
            matrix[key][i] /= t
    return matrix
    

def Score(motifs):
    score = 0
    l = len(motifs[0])
    for i in range(l):
        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            count[motif[i]] += 1
        score += sum(count.values()) - max(count.values())
    return score
            
def GreedyMotifSearch(Dna, k, t):
    bestMotifs = []
    for dnaStr in Dna:
        bestMotifs.append(dnaStr[:k])
    for j in range(len(Dna[0]) - k + 1):
        kmer = Dna[0][j: j + k]
        motifs = [kmer]
        for dnaStr in Dna[1:]:
            profile = MakeProfileMatrix(motifs, k)
            motifs.append(ProfileMostProbableKmer(dnaStr, k, profile))
        if Score(motifs) < Score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def MakeLaplaceProfileMatrix(motifs, k):
    matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    for key in matrix.keys():
        for i in range(k):
            matrix[key].append(float(1.0))
    for motif in motifs:
        for i in range(len(motif)):
            matrix[motif[i]][i] += 1
    for key in matrix.keys():
        t += matrix[key[i]][0]
    for key in matrix.keys():
        for i in range(k):
            matrix[key][i] /= t
    return matrix

def GreedyMotifSearchWithPsuedocounts(Dna, k, t):
    bestMotifs = []
    for dnaStr in Dna:
        bestMotifs.append(dnaStr[:k])
    for j in range(len(Dna[0]) - k + 1):
        kmer = Dna[0][j: j + k]
        motifs = [kmer]
        for dnaStr in Dna[1:]:
            profile = MakeLaplaceProfileMatrix(motifs, k)
            motifs.append(ProfileMostProbableKmer(dnaStr, k, profile))
        if Score(motifs) < Score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def PrintListSpace(l):
    for i in sorted(l):
        print(i, end = ' ')
    print()

def PrintListLine(l):
    for i in l:
        print(i)
    print()

lines = sys.stdin.read().splitlines()
k,t = [int(x) for x in lines[0].split()]

PrintListLine(GreedyMotifSearchWithPsuedocounts(lines[1:], k, t))

##Profile = {}
##Profile['A'] = [float(x) for x in lines[2].split()]
##Profile['C'] = [float(x) for x in lines[3].split()]
##Profile['G'] = [float(x) for x in lines[4].split()]
##Profile['T'] = [float(x) for x in lines[5].split()]
