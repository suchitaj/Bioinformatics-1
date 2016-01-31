import sys

def SkewGenome(Genome):
    genList = []
    for i in range(len(Genome) + 1):
        if i == 0:
            skew = 0
        elif Genome[i - 1] == 'G':
            skew = genList[i - 1] + 1
        elif Genome[i - 1] == 'C':
            skew = genList[i - 1] - 1
        else:
            skew = genList[i - 1]
        genList.append(skew)
    return genList

def MinimumSkew(Genome):
    genList = []
    minNum = 0
    minList = []
    for i in range(len(Genome) + 1):
        if i == 0:
            skew = 0
        elif Genome[i - 1] == 'G':
            skew = genList[i - 1] + 1
        elif Genome[i - 1] == 'C':
            skew = genList[i - 1] - 1
        else:
            skew = genList[i - 1]
        genList.append(skew)
        if skew < minNum:
            for j in range(len(minList)):
                minList.remove(minList[0])
            minNum = skew
            minList.append(i)
        elif skew == minNum:
            minList.append(i)
    return minList

def PrintList(l):
    for i in l:
        print(i, end = ' ')
    print()

lines = sys.stdin.read().splitlines()
PrintList(MinimumSkew(lines[0]))

##PrintList(MinimumSkew('TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT'))
