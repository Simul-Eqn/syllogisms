'''
structure 1: all A are B 
structure 2: some A are B 
structure 3: some A are not B 
structure 4: no A are B
so each structure is s1 + s2 + s3 + s4 
format:

given that:
all A are B
some B are C
is it true that:
some A are not C

'''

'''
DEFINITIONS:
all A are B:
everything in A are also in B

some A are B:
>= 1 thing in A is also in B

some A are not B:
>= 1 thing in A is not also in B

no A are B:
0 things in A are also in B AND A has at least one thing 
'''

s1 = ""
s2 = ""
s3 = ""
s4 = ""

def getText(n, s2, s4):
    if (n%4 == 1): #so n%8 will be 1 or 5
        #all A are B
        s1 = "all "
        #s2 = "A" 
        s3 = " are "
        #s4 = "B"
    elif (n%4 == 2):
        #some A are B 
        s1 = "some "
        #s2 = "A"
        s3 = " are "
        #s4 = "B" 
    elif (n%4 == 3):
        #some A are not B
        s1 = "some "
        #s2 = "A"
        s3 = " are not "
        #s4 = "B" 
    else:
        #no A are B
        s1 = "no "
        #s2 = "A" 
        s3 = " are "
        #s4 = "B"
    if (((n%8)//4) > 0):
        s2, s4 = s4, s2 
    s = s1+s2+s3+s4
    return s

def getPrintText(n):
    s_in1 = getText(n, "A", "B")
    n //= 8 
    s_in2 = getText(n, "B", "C")
    n //= 8 
    s_out = getText(n, "A", "C")
    n //= 8

    res = "" 
    res += "Given that: \n"
    res += (s_in1) + '\n' 
    res += (s_in2) + '\n' 
    res += "is it true that: \n"
    res += (s_out) + '\n' 
    #res += '\n'
    return res 

def getSyllogism(n):
    inputs = []
    #res_syllogism = []
    syllogism = []
    
    t = (n%4)
    if t==0: t=4
    syllogism.append(t) 
    if (((n%8)//4) == 0):
        syllogism.append("A")
        syllogism.append("B")
    else:
        syllogism.append("B")
        syllogism.append("A")
    inputs.append([i for i in syllogism])
    n //= 8
    syllogism = [] 

    t = (n%4)
    if t==0: t=4
    syllogism.append(t) 
    if (((n%8)//4) == 0):
        syllogism.append("B")
        syllogism.append("C")
    else:
        syllogism.append("C")
        syllogism.append("B")
    inputs.append([i for i in syllogism])
    n //= 8
    syllogism = [] 

    t = (n%4)
    if t==0: t=4
    syllogism.append(t) 
    if (((n%8)//4) == 0):
        syllogism.append("A")
        syllogism.append("C")
    else:
        syllogism.append("C")
        syllogism.append("A")
    #syllogism.append([i for i in syllogism])
    #n //= 8

    return (inputs, syllogism) 

def printSyllogism(l):
    if (l[0]%4 == 1): 
        #all A are B
        s1 = "all "
        s3 = " are "
    elif (l[0]%4 == 2):
        #some A are B 
        s1 = "some "
        s3 = " are "
    elif (l[0]%4 == 3):
        #some A are not B
        s1 = "some "
        s3 = " are not "
    else:
        #no A are B
        s1 = "no "
        s3 = " are "
    return s1+str(l[1])+s3+str(l[2]) 

if __name__ == "__main__": 
    while True:
        n = int(input("Number: ")) 
        '''s_in1 = getText(n, "A", "B")
        n //= 4 
        s_in2 = getText(n, "B", "C")
        n //= 4 
        s_out = getText(n, "A", "C")
        n //= 4
        print("Given that: ")
        print(s_in1)
        print(s_in2)
        print("is it true that: ")
        print(s_out)
        print() '''
        #s2 = "A"
        #s4 = "B"
        print(getPrintText(n)) 
    
