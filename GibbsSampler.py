import sys
import random

def PrintListLine(l):
    for i in l:
        print(i)
    print()

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

def WeightedChoice(choices, total):
    #print(total, choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.items():
        if upto + w > r:
            #print(c, w, upto, r)
            return c
        upto += w
    print(c, w, upto, r)
    assert False, "Shouldn't get here"

def ProfRandGenKmer(Text, k, Profile):
    kmerArray = {}
    totalProb = 0.0
    for i in range(len(Text) - k + 1):
        probability = 1.0
        kmer = Text[i: i + k]
        for j in range(k):
            t = kmer[j]
            probability = probability * Profile[t][j]
        kmerArray[kmer] = probability
        totalProb += probability
    total = 0.0
    for key in kmerArray.keys():
        kmerArray[key] = kmerArray[key]/totalProb
        total += kmerArray[key]
    return WeightedChoice(kmerArray, total)

def GibbsSampler(Dna, k, t, N):
    Motifs = []
    for i in range(t):
        MotifStart = random.randint(0, len(Dna[0]) - k)
        Motif = Dna[i][MotifStart : MotifStart + k]
        Motifs.append(Motif)
    BestMotifs = Motifs
    for j in range(N):
        i = random.randint(0, t-1)
        Profile = MakeLaplaceProfileMatrix(Motifs, k)
        prevMotif = Motifs[i]
        prevScore = Score(Motifs)
        Motifs[i] = ProfRandGenKmer(Dna[i], k, Profile)
        newScore = Score(Motifs)
        if prevScore <= newScore:
            Motifs[i] = prevMotif
        if newScore < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

def RepeatGibbs(Dna, k, t, N):
    BestMotifs = []
    for i in range(100):
        Motifs = GibbsSampler(Dna, k, t, N)
        if Score(Motifs) < Score(BestMotifs):
            print(i, 'changing', BestMotifs, 'to')
            PrintListLine(Motifs)
            sys.stdout.flush()
            BestMotifs = Motifs
    return BestMotifs

lines = sys.stdin.read().splitlines()
k,t,N = [int(x) for x in lines[0].split()]
PrintListLine(RepeatGibbs(lines[1:],k,t,N))
