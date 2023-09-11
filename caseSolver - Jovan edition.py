import caseGenerator

answers = [-10 for _ in range(256)] 

caseNumber = 0

def do(caseN = -1):
    global caseNumber
    if caseN == -1:
        caseN = caseNumber 
    res = input(caseGenerator.getPrintText(caseN)+"Result: ")
    answers[caseN] = int(res)
    #print("CASEN:", caseN, "CASENUMBER:", caseNumber, "SAME:", caseN==caseNumber) 
    if (caseN == caseNumber):
        caseNumber += 1
    print() 

def show(): 
    print(answers)
    print() 

def save():
    fout = open('jovanCases.txt', 'w')
    for i in range(256):
        fout.write(str(answers[i])+'\n')
    fout.close() 

def load():
    global caseNumber 
    fin = open('jovanCases.txt', 'r')
    caseNumber = 256
    caseNotSet = True 
    for i in range(256):
        answers[i] = int(fin.readline())
        if caseNotSet and answers[i] == -10:
            caseNumber = i
            caseNotSet = False
