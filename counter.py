import numpy as np
from sys import stdin, stdout 

import caseGenerator
import syllogismEvaluator

class Empty(): 
    def write(self, *args): 
        return 

syllogismEvaluator.stdout = Empty() 
syllogismEvaluator.print = lambda *args: None 

for n_in in range(6, 11): 
    deftrue_count = 0 
    for n in range(1 << (n_in*3 + 3)): 
        t = caseGenerator.get_nto1_syllogism(n_in, n)
        if syllogismEvaluator.eval_single_syllogism(t[0], t[1]) == 1: 
            deftrue_count += 1 
    
    out = open('deftrue_counts.txt', 'a') 
    out.write(str(deftrue_count)) 
    out.write("\n") 
    out.close() 

    print(n_in, ':', deftrue_count) 
