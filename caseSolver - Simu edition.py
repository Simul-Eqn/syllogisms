import caseGenerator

answers = [-10 for _ in range(256)] 

caseNumber = 256

def do(caseN = -1):
    global caseNumber
    if caseN == -1:
        caseN = caseNumber 
    res = input(caseGenerator.getPrintText(caseN)+"Result: ")
    answers[caseN-256] = int(res)
    #print("CASEN:", caseN, "CASENUMBER:", caseNumber, "SAME:", caseN==caseNumber) 
    if (caseN == caseNumber):
        caseNumber += 1
    print() 

def show(): 
    print(answers)
    print() 

def save():
    fout = open('simuCases.txt', 'w')
    for i in range(256):
        fout.write(str(answers[i])+'\n')
    fout.close() 

def load():
    global caseNumber 
    fin = open('simuCases.txt', 'r')
    caseNumber = 512
    caseNotSet = True 
    for i in range(256):
        answers[i] = int(fin.readline())
        if caseNotSet and answers[i] == -10:
            caseNumber = i+256
            caseNotSet = False
