import numpy as np
from sys import stdin, stdout 

import caseGenerator
import syllogismEvaluator

def test_n(n, v):

    deftrue = []
    deffalse = []
    dontknow = []

    
    inputs, toadd = caseGenerator.get_nto1_syllogism(n-1, v-1)

    inputs.append(toadd) 
    
    varnames = set() 
    for s in inputs:
        varnames.add(s[1])
        varnames.add(s[2])

    varnames = list(varnames)

    res_varnames = [varname for varname in varnames] 

    if len(varnames) < 3:
        stdout.write("ERROR: MUST HAVE AT LEAST 3 VARIABLES\n\n\n")
        return 

    try: 
        solve, errors, existances = syllogismEvaluator.process_single_syllogism(inputs, varnames)
    except:
        return 

    for a in res_varnames:
        for b in res_varnames:
            if a==b: continue 
            for n in range(1, 5):
                res, antires = syllogismEvaluator.eval_res(solve, varnames, [n, a, b], errors, existances)
                if res:
                    deftrue.append([n, a, b]) 
                elif antires:
                    deffalse.append([n, a, b]) 
                else:
                    dontknow.append([n, a, b]) 
    
    #stdout.write("\n\nSUMMARY: \n")
    stdout.write("\n\nGIVEN THAT: \n")
    for syllogism in inputs:
        stdout.write(caseGenerator.printSyllogism(syllogism))
        stdout.write("\n")

    
    stdout.write("\n\nDefinitely true syllogisms: \n")
    for syllogism in deftrue:
        stdout.write(caseGenerator.printSyllogism(syllogism))
        stdout.write("\n")

    stdout.write("\n\nDefinitely false syllogisms: \n")
    for syllogism in deffalse:
        stdout.write(caseGenerator.printSyllogism(syllogism))
        stdout.write("\n")

    stdout.write("\n\nPossibly true or false syllogisms: \n")
    for syllogism in dontknow:
        stdout.write(caseGenerator.printSyllogism(syllogism))
        stdout.write("\n")

    stdout.write("\n\n\n") 
