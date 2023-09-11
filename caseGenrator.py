'''
structure 1: all A are B 
structure 2: some A are B 
structure 3: not some A are B 
structure 4: some A are not B
so each structure is s1 + s2 + s3 + s4 
format:

given that:
all A are B
some B are C
is it true that:
some A are not C

'''
s1 = ""
s2 = ""
s3 = ""
s4 = "" 
while True:
    n = input("Number: ")
    s = "" 
    if (n%4 == 1): #so n%8 will be 1 or 5
        
        #all A are B
        if (((n%8)//4) == 0):
            
