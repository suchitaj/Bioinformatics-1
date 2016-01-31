#!/usr/bin/env python3
'''
Solutions to programming assignments for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic

Problem Titles and Related URLs (available to enrolled students only)
- Compute Reverse Complement of a DNA fragment.
https://stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Surprising-than-Others-3/#step-2

- Clump finding problem
https://stepic.org/Bioinformatics-Algorithms-2/An-Explosion-of-Hidden-Messages-4/#step-4

- Frequent words problems in a DNA string (allowing for mismatches)
https://beta.stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Elusive-than-Others-9/#step-5

- Approximate Pattern matching and Pattern counting
  https://stepic.org/Bioinformatics-Algorithms-2/Some-Hidden-Messages-are-More-Surprising-than-Others-3/#step-5

'''

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
    '''Find the reverse complement of a DNA string.'''
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

