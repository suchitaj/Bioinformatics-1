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
        
#print(NumberToPattern(5353, 7))

def PrintList(l):
    for i in l:
        print(i, end = ' ')
    print()
    return

def ComputingFrequencies(Text, k):
    freqArray = {}
    for i in range((4**k)):
        freqArray[i] = 0
    for i in range(len(Text) - k + 1):
        Pattern = Text[i: i + k]
        j = PatternToNumber(Pattern)
        freqArray[j] += 1
    return freqArray

#lines = sys.stdin.read().splitlines()
#PrintList(ComputingFrequencies(lines[0], int(lines[1])).values())

lines = sys.stdin.read().splitlines()
print(NumberToPattern(int(lines[0]), int(lines[1])))
      
#print(PatternToNumber('CTTCTCACGTACAACAAAATC'))
