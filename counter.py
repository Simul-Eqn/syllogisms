import numpy as np
import copy 

import os 
from sys import stdin, stdout 

import caseGenerator
import syllogismEvaluator



class Empty(): 
    def write(self, *args): 
        return 

syllogismEvaluator.stdout = Empty() 
syllogismEvaluator.print = lambda *args: None 

parent_dir = os.path.join(os.getcwd(), "counter_output")

for n_in in range(2, 11): 
    
    deftrue_count = 0 
    deftrue_syllogisms = [] 
    deftrue_solves = [] 

    for n in range(0, 1 << (n_in*3 + 3), 8): 
        '''
        t = caseGenerator.get_nto1_syllogism(n_in, n)
        if syllogismEvaluator.eval_single_syllogism(t[0], t[1]) == 1: 
            deftrue_count += 1 
        '''

        inputs, res = caseGenerator.get_nto1_syllogism(n_in, n)
        
        varnames = set() 
        for s in inputs:
            varnames.add(s[1])
            varnames.add(s[2])

        varnames = list(varnames)

        res_varnames = res[1:] 

        if len(varnames) < 3:
            stdout.write("ERROR: MUST HAVE AT LEAST 3 VARIABLES\n\n\n")
            raise Exception("TOO LESS VARNAMES HUHHHH")

        #print(inputs, varnames)
        #print(syllogismEvaluator.process_single_syllogism(inputs, varnames)) 

        solve, errors, existances = syllogismEvaluator.process_single_syllogism(inputs, varnames) # "errors" actually means count of each existance 

        #print(solve, errors, existances)

        for a in res_varnames:
            for b in res_varnames:
                if a==b: continue 
                for n in range(1, 5):
                    #print(inputs, [n,a,b]) 
                    res, antires = syllogismEvaluator.eval_res(solve, varnames, [n, a, b], errors, existances)
                    #print(res, antires)
                    if res:
                        deftrue_count += 1 
                        deftrue_solves.append(copy.deepcopy(solve))
                        deftrue_syllogisms.append( inputs + [[n, a, b]]) 

    # save count 
    out = open('./counter_output/deftrue_counts.txt', 'a') 
    out.write(str(deftrue_count)) 
    out.write("\n") 
    out.close() 

    # save syllogisms 
    data_dir = os.path.join(parent_dir, str(n_in)+"-to-1") 
    os.mkdir(data_dir) 
    
    np.savez(os.path.join(data_dir, "solves.npz"), *deftrue_solves) 
    
    syllogism_out = open(os.path.join(data_dir, "syllogisms.txt"), 'w') 
    for syllogism_list in deftrue_syllogisms: 
        for syllogism in syllogism_list: 
            syllogism_out.write( str(syllogism[0]) + ' ' + str(syllogism[1]) + ' ' + str(syllogism[2]) + '\n') 
        syllogism_out.write('\n')
    syllogism_out.close() 

    #input() 


    print(n_in, ':', deftrue_count) 
