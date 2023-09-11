import numpy as np
from sys import stdin, stdout
import caseGenerator

def genQuery(varnames, syllogism, value1, value2):
    query = "solve"
    query += '['
    for i in varnames:
        if syllogism[1] == i:
            #query += "["+str(value1)+"]"
            query += str(value1)+','
        elif syllogism[2] == i:
            #query += '['+str(value2)+']'
            query += str(value2)+',' 
        else:
            #query += '[:]'
            query += ":,"
    #query += ']' 
    #query += " = "+str(given) 
    return query[:-1] + ']' 

stdout.write('SYLLOGISM EVALUATOR !!!!!!!!!! \n\n')
while True:
    stdout.write(
"""MENU:
1) AUTOTEST SYLLOGISM LIST 
2) EVALUATE 2-TO-1 SYLLOGISM BY NUMBER 
3) EVALUATE SYLLOGISM (MANUAL)
4) GENERATE TRUE, FALSE, MAYBE SYLLOGISMS (MANUAL)
5) DISPLAY SYLLOGISM MEANINGS
Choice: """) 
    try:
        n = int(stdin.readline())
    except:
        stdout.write("Invalid input format. \n\n")
        continue
    
    if n==1:
        stdout.write("That's work in progress. \n\n")
        
    elif n==2:
        stdout.write("That's work in progress. \n\n")
        
    elif n==3:
        stdout.write("Number of input syllogisms: ")
        try:
            n = int(stdin.readline())
            if n<2: 1/0 
        except:
            stdout.write("Invalid input. \n\n")
            continue
        inputs = []
        cancelled = False
        syllogism_count = n 
        while len(inputs) < syllogism_count:
            stdout.write("\nType of input syllogism(0 to display help): ")
            try:
                n = int(stdin.readline())
                if n == -1:
                    #cancelled = True
                    #stdout.write("Quit operation. \n\n\n") 
                    break
                    #1/0 
                if n == 0:
                    #display help
                    stdout.write("-1: quit \n0: show syllogism formats \n1: all [] are [] \n2: some [] are [] \n3: some [] are not [] \n4: no [] are []\n\n")
                    continue 
                if n<-1 or n>4:
                    1/0
                    
                #n is the syllogism type, from 1 to 4.
                stdout.write("Variable names (space separated): ") 
                while True:
                    try:
                        temp = stdin.readline()
                        if temp.lower() == "quit":
                            cancelled = true
                            1/0 
                            #break 
                        a, b = temp.split() 
                        break
                    except:
                        1/0 
                        #stdout.write("Invalid input format. \n\n")
                #if cancelled: break;
                
                #a and b are the variable names (string) 
                stdout.write("Confirm syllogism? (y/n): ")
                temp = stdin.readline()
                if temp[0].lower() == 'y':
                    inputs.append([n, a, b])
                    stdout.write("Syllogism appended successfully. \n\n") 
                else:
                    stdout.write("Syllogism cancelled. \n\n") 
            except:
                if cancelled:
                    stdout.write("CANCELLED\n\n\n")
                else: 
                    stdout.write("Invalid input format. \n\n")

        if len(inputs) != syllogism_count:
            stdout.write("Quit operation. \n\n\n") 
            continue 

        #now, get input on what the syllogism to evaluate is
        res_syllogism = [] 
        cancelled = False
        #syllogism_count = n 
        while len(res_syllogism) < 3:
            stdout.write("\nSyllogism to evaluate(0 to display help): ")
            try:
                n = int(stdin.readline())
                if n == -1:
                    #cancelled = True
                    #stdout.write("Quit operation. \n\n\n") 
                    break
                    #1/0 
                if n == 0:
                    #display help
                    stdout.write("-1: quit \n0: show syllogism formats \n1: all [] are [] \n2: some [] are [] \n3: some [] are not [] \n4: no [] are []\n\n")
                    continue 
                if n<-1 or n>4:
                    1/0
                    
                #n is the syllogism type, from 1 to 4.
                stdout.write("Variable names (space separated): ") 
                while True:
                    try:
                        temp = stdin.readline()
                        if temp.lower() == "quit":
                            cancelled = true
                            1/0 
                            #break 
                        a, b = temp.split() 
                        break
                    except:
                        1/0 
                        #stdout.write("Invalid input format. \n\n")
                #if cancelled: break;
                
                #a and b are the variable names (string) 
                stdout.write("Confirm syllogism? (y/n): ")
                temp = stdin.readline()
                if temp[0].lower() == 'y':
                    res_syllogism = [n, a, b] 
                    stdout.write("Syllogism set successfully. \n\n") 
                else:
                    stdout.write("Syllogism cancelled. \n\n") 
            except:
                if cancelled:
                    stdout.write("CANCELLED\n\n\n")
                else: 
                    stdout.write("Invalid input format. \n\n")

        if len(inputs) != syllogism_count:
            stdout.write("Quit operation. \n\n\n") 
            continue
        
        
        #syllogism list obtained
        print("SYLLOGISM LIST:", inputs)
        print("OUTPUT SYLLOGISM:", res_syllogism) 

        #generate variable list
        varnames = set() 
        for s in inputs:
            varnames.add(s[1])
            varnames.add(s[2])

        varnames = list(varnames) 
        
        #get syllogism array 
        solve = np.zeros([2 for _ in range(len(varnames))], dtype=np.dtype(list)) #each one is to each varname
        existances = 1 #let 1 be the wildcard existances
        error = False 
        for syllogism in inputs:
            print("\nEVALUATING SYLLOGISM:", syllogism) 
            if syllogism[0] == 1:
                #all [] are []
                print("all [] are []") 
                q = genQuery(varnames, syllogism, 1, 0)
                '''if eval("not (("+q+" <= 0).all())"):
                    #something is -1, contradiction
                    #stdout.write("Contradicting syllogisms found, please retry. \n\n\n")
                    error = True
                    break'''
                exec(q+" = [-1]")
                print(q+" = [-1]") 
            elif syllogism[0] == 2:
                #some [] are []
                print("some [] are []") 
                q = genQuery(varnames, syllogism, 1, 1)
                '''if eval("not (("+q+" != -1).all())"):
                    #something is -1, contradiction
                    #stdout.write("Contradicting syllogisms found, please retry. \n\n\n")
                    error = True
                    break'''
                existances += 1
                exec(q+" = [i if i==[-1] else i+["+str(existances)+"] for i in "+q] 
                #exec(q+" = "+str(existances))
                print(q+" = [i if i==[-1] else i+["+str(existances)+"] for i in "+q) 
            elif syllogism[0] == 3:
                #some [] are not []
                pritn("some [] are not []") 
                #existances += 1
                #exec(genQuery(varnames, syllogism, 1, -1)+" = "+str(existances))
                q = genQuery(varnames, syllogism, 1, 0)
                '''if eval("not (("+q+" != -1).all())"):
                    #something is -1, contradiction
                    #stdout.write("Contradicting syllogisms found, please retry. \n\n\n")
                    error = True
                    break'''
                existances += 1
                exec(q+" = [i if i==[-1] else i+["+str(existances)+"] for i in "+q] 
                #exec(q+" = "+str(existances))
                print(q+" = [i if i==[-1] else i+["+str(existances)+"] for i in "+q) 
            elif syllogism[0] == 4:
                #no [] in []
                print("no [] in []") 
                q = genQuery(varnames, syllogism, 1, 1) 
                '''if eval("not (("+q+" <= 0).all())"):
                    #something is -1, contradiction
                    #stdout.write("Contradicting syllogisms found, please retry. \n\n\n")
                    error = True
                    break'''
                exec(q+" = [-1]")
                print(q+" = [-1]") 
        if error:
            stdout.write("Contradicting syllogisms found, please retry. \n\n\n")
            continue 

        print() 
        print("VARNAMES:", varnames)
        print("SOLVE:", solve)

        #so existances as a number is 1 more than the actl amount of existances there are 

        #evaluate result syllogism - not done yet 
        res = False
        antires = True
        print("\nEVALUATING SYLLOGISM:", res_syllogism) 
        if res_syllogism[0] == 1:
            #all [] are []
            #res = eval("numpy.sum("genQuery(varnames, syllogism, 0, 1)+"=-1) == "+str(2**(len(varnames)-2)))
            #antires = eval("numpy.sum("genQuery(varnames, syllogism, 0, 1)+">0) == "+str(2**(len(varnames)-2)))
            res = eval("("+genQuery(varnames, syllogism, 1, 0)+"==-1).all()")
            antires = eval("("+genQuery(varnames, syllogism, 1, 0)+">0).all()")
            print("("+genQuery(varnames, syllogism, 1, 0)+"==-1).all()")
            print("("+genQuery(varnames, syllogism, 1, 0)+">0).all()") 
        elif res_syllogism[0] == 2:
            #some [] are []
            #eval(genQuery(varnames, syllogism, 1, 1)+" = "+str(existances))
            pass 
        elif res_syllogism[0] == 3:
            #existances += 1
            #eval(genQuery(varnames, syllogism, 1, -1+" = "+str(existances))
            pass 
        elif res_syllogism[0] == 4:
            #res = eval("numpy.sum("genQuery(varnames, syllogism, 1, 1)+"=-1) == "+str(2**(len(varnames)-2)))
            #antires = eval("numpy.sum("genQuery(varnames, syllogism, 1, 1)+">0) == "+str(2**(len(varnames)-2)))
            res = eval("("+genQuery(varnames, syllogism, 1, 1)+"==-1).all()")
            antires = eval("("+genQuery(varnames, syllogism, 1, 1)+">0).all()")
            print("("+genQuery(varnames, syllogism, 1, 1)+"==-1).all()")
            print("("+genQuery(varnames, syllogism, 1, 1)+">0).all()") 

        print(res, antires) 
        
        if res:
            stdout.write("This syllogism is definitely true. \n\n\n")
        elif antires:
            stdout.write("This syllogism is definitely false. \n\n\n")
        else:
            stdout.write("This syllogism may be true or false. \n\n") 
    
    elif n==4:
        stdout.write("That's work in progress. \n\n")

    elif n==5:
        stdout.write("That's work in progress. \n\n")

    else:
        #stdout.write("Invalid choice. \n\n")
        break 

    
