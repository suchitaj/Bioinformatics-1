import sys
import random

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

def WeightedRandomChoiceKmer(text, k, profileMatrix):
    """
    Input: A string Text, an integer k, and a 4 × k matrix Profile
    Output: A Profile-most probable k-mer in Text.
    """
    kmerMap = {}
    cumProb = 0.0
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        prob = 1.0
        for j in range(len(kmer)):
            c = kmer[j]
            prob *= profileMatrix[c][j]
        kmerMap[kmer] = prob
        cumProb += prob
    # normalize probabilities
    total = 0.0
    for k in kmerMap.keys():
        #print(k, kmerMap[k], kmerMap[k] / cumProb)
        kmerMap[k] = kmerMap[k] / cumProb
        total += kmerMap[k]
    return WeightedChoice(kmerMap, total)

def InitProfileMatrix(k):
    profMat = {
        'A' : [],
        'T' : [],
        'G' : [],
        'C' : []
        }
    for key in profMat.keys():
        for i in range(k):
            profMat[key].append(float(1.0))
    return profMat

def MakeProfileMatrix(motifs, k, n):
    #print(motifs)
    profMat = InitProfileMatrix(k)
    for loc in range(len(motifs)):
        if loc == n:
            continue
        text = motifs[loc]
        total = 0.0
        for i in range(len(text)):
            profMat[text[i]][i] += 1.0
    t = 0.0
    for key in profMat.keys():
        t += profMat[key][0]
    for key in profMat.keys():
        #print(key, end=' ')
        for i in range(k):
            profMat[key][i] /= t
            #print(profMat[key][i], end=' ')
        #print()
    return profMat

def Score(lst):
    t = len(lst)
    if t == 0:
        return float("inf")
    score = 0
    k = len(lst[0])
    for i in range(k):
        count = {
            'A' : 0,
            'T' : 0,
            'G' : 0,
            'C' : 0
            }
        for l in lst:
            count[l[i]] += 1
        maxkey = 'A'
        maxv = count['A']
        for key,v in count.items():
            if v > maxv:
                maxkey = k
                maxv = v
        score += (t - maxv)
    #print(lst, score)
    return score

def MakeOneRandomMotif(dnaStr, k):
    start = random.randint(0, len(dnaStr) - k)
    return dnaStr[start : start + k]

def RandomMotifs(Dna, k):
    motifs = []
    for dnaStr in Dna:
        motifs.append(MakeOneRandomMotif(dnaStr, k))
    return motifs

def GibbsSampler(Dna, k, t, N):
    bestMotifs = RandomMotifs(Dna, k)
    motifs = bestMotifs
    #print(motifs)
    for j in range(N):
        i = random.randint(0, t-1)
        #print(j, 'skipping: ', i)
        profMat = MakeProfileMatrix(motifs, k, i)
        oldMotif = motifs[i]
        oldScore = Score(motifs)
        motifs[i] = WeightedRandomChoiceKmer(Dna[i], k, profMat)
        newScore = Score(motifs)
        if oldScore <= newScore:
            #print('Keeping old motif')
            motifs[i] = oldMotif
        #else:
            #print('Switching to new motif')
        if newScore < Score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def PrintList(l):
    for i in l:
        print(i)

def DoManyTimes(Dna, k, t, N):
    bestMotifs = []
    for i in range(1000):
        motifs = GibbsSampler(Dna, k, t, N)
        if Score(motifs) < Score(bestMotifs):
            print(i, 'switching best from', bestMotifs, 'to')
            PrintList(motifs)
            sys.stdout.flush()
            bestMotifs = motifs
    return bestMotifs

lines = sys.stdin.read().splitlines()

[k, t, N] = [int(x) for x in lines[0].split()]
PrintList(DoManyTimes(lines[1:], k, t, N))
