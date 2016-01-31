#!/usr/bin/env python3
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Title: Minimum Skew Problem
Find a position in a genome where the skew diagram attains a minimum.
Input: 
URL (available to enrolled students only):
https://beta.stepic.org/Bioinformatics-Algorithms-2/Peculiar-Statistics-of-the-Forward-and-Reverse-Half-Strands-7/#step-6
'''

import sys

def SkewGenome(Genome):
    '''Skewi+1(Genome) from Skewi(Genome) according to the nucleotide in position i of Genome. If this nucleotide is G, then Skewi+1(Genome) = Skewi(Genome) + 1; if this nucleotide is C, then Skewi+1(Genome)= Skewi(Genome) – 1; otherwise, Skewi+1(Genome) = Skewi(Genome).
'''
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
     '''Minimum Sew are positions with lowest skew values'''
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
