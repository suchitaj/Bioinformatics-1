import sys
import random

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

def MakeMotifs(Profile, Dna, k):
    Motifs = []
    for strand in Dna:
        Motifs.append(ProfileMostProbableKmer(strand, k, Profile))
    return Motifs

def MakeLaplaceProfileMatrix(motifs, k):
    matrix = {'A': [], 'C': [], 'G': [], 'T': []}
    for key in matrix.keys():
        for i in range(k):
            matrix[key].append(float(1.0))
    for motif in motifs:
        for i in range(len(motif)):
            matrix[motif[i]][i] += 1
    t = 0.0
    for key in matrix.keys():
        t += matrix[key][0]
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

def RandomizedMotifSearch(Dna, k, t):
    Motifs = []
    for i in range(t):
        MotifStart = random.randint(0, len(Dna[0]) - k)
        Motif = Dna[i][MotifStart : MotifStart + k]
        Motifs.append(Motif)
    BestMotifs = Motifs
    while True:
        Profile = MakeLaplaceProfileMatrix(Motifs, k)
        Motifs = MakeMotifs(Profile, Dna, k)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
        else:
            return BestMotifs

def MotifSearchResults(Dna, k, t):
    lowestScore = float('inf')
    lowMotifs = []
    for i in range(1000):
        motifs = RandomizedMotifSearch(Dna, k, t)
        score = Score(motifs)
        if score < lowestScore:
            print(i, score, motifs)
            sys.stdout.flush()
            lowestScore = score
            lowMotifs = motifs
    return lowMotifs

def PrintListSpace(l):
    for i in sorted(l):
        print(i, end = ' ')
    print()

def PrintListLine(l):
    for i in l:
        print(i)
    print()

##lines = sys.stdin.read().splitlines()
##k,t = [int(x) for x in lines[0].split()]
##PrintListLine(MotifSearchResults(lines[1:],k,t))

Dna = ['TGACGTTC','TAAGAGTT','GGACGAAA','CTGTTCGC']
motifs = ['TGA','GTT','GAA','TGT']
k = 3
Profile = MakeLaplaceProfileMatrix(motifs, k)
PrintListSpace(MakeMotifs(Profile, Dna, k))

