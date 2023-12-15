import caseGenerator 
import syllogismEvaluator 

from sys import stdin, stdout 
import os 

import numpy as np 

min_n = 2 # inclusive 
max_n = 7 # exclusive 

debug = True 


solvess = [[], []] # indexes 0 and 1 are filled 
# preload solves 
for n in range(min_n, max_n): 
    solves = [] 
    with np.load(os.path.join(os.getcwd(), "counter_output", str(n)+"-to-1", "solves.npz")) as data: 
        for k, v in list(data.items()):
            solves.append(v)
    solvess.append(solves) 
    solves = [] 


if __name__ == "__main__": 
    while True: 
        stdout.write("\nVISUALIZING COUNTER OUTPUTS!\n") 

        try: 
            n = int(input("Number of in syllogisms: "))
            if debug and n==-1: break # for debug 
            if n < min_n or n >= max_n: 
                1/0 
        except ZeroDivisionError: 
            stdout.write("THAT IS OUT OF RANGE.\n") 
            continue 
        except: 
            stdout.write("INVALID INPUT. \n")
            continue 
            
        try: 
            v = int(input("Succeeded syllogism number: ")) 
            if v<0 or v>len(solvess[n]): 
                1/0 
        except ZeroDivisionError: 
            stdout.write("THAT IS OUT OF RANGE. \n")
            continue 
        except: 
            stdout.write("INVALID INPUT. \n")
            continue 
            
        # try opening the file 
        try: 
            inputs, res_count, getting_res, res_syllogisms, res_varnames = syllogismEvaluator.load_sylfile(os.path.join(os.getcwd(), "counter_output", str(n)+"-to-1", "syl"+str(v)+".syl")) 
        except FileNotFoundError: 
            stdout.write("File not found. Make sure you did not exceed the syllogism number...") 
            continue 
            
        #show inputs
        stdout.write("\nINPUT SYLLOGISMS: \n") 
        for syllogism in inputs:
            stdout.write(caseGenerator.printSyllogism(syllogism))
            stdout.write("\n")

        # show output 
        stdout.write("OUTPUT SYLLOGISM: \n")
        stdout.write(caseGenerator.printSyllogism(res_syllogisms[0]))
        stdout.write("\n\n")


        #generate variable name list
        varnames = set() 
        for s in inputs:
            varnames.add(s[1])
            varnames.add(s[2])

        for s in res_varnames:
            varnames.add(s)

        varnames = list(varnames) 

        # see if try resolving or try loading 
        re_solve = False 
        temp = input("Try re-solving syllogisms? (y/n): ") 
        if temp[0].lower() == 'y':
            re_solve = True

        if re_solve: 
            # TRY RE-SOLVING THIS 
            
            # try solving it 
            try: 
                solve, errors, existances = syllogismEvaluator.process_single_syllogism(inputs, varnames)
            except Exception as e: 
                if debug: 
                    print(e) 
                stdout.write("ERROR RE-SOLVING SYLLOGISM\n\n") 
                continue 
            stdout.write("Successfully re-solved. \n")

            syllogismEvaluator.show_visualization(solve, varnames, "RE-SOLVE OF "+str(n)+"-to-1 case "+str(v)) 
            stdout.write("Visuaslization shown. \n\n") 
        
        else: 
            syllogismEvaluator.show_visualization(solvess[n][v], varnames, "SAVED SOLVE OF "+str(n)+"-to-1 case "+str(v)) 
            stdout.write("Visuaslization shown. \n\n") 

