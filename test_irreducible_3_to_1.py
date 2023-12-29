
def join_syllogisms_first_decompose(syl1, syl2): 
    if 'C' in syl1: # first decompose 
        syl1 = syl1.replace('C', 'B') 
        syl2 = syl2.replace('C', 'B') 
        syl2 = syl2.replace('D', 'C') 
    return [syl1, syl2] 

def left_shift_1(syls): 
    res = [] 
    for syl in syls: 
        res.append(syl.replace('B', 'A').replace('C', 'B').replace('D', 'C')) 
    
    return res 

def join_syllogisms_second_decompose(syl1, syl2): 
    if 'A' in syl2: # second decompose 
        syl2 = syl2.replace('A', 'B') 
    return [syl1, syl2] 


def syllogisms_are_equal(syl1, syl2): 
    syl1 = syl1.replace('D', 'C') 
    syl2 = syl2.replace('D', 'C') 
    if (syl1[0] == syl2[0] and syl2[0] == '2') or (syl1[0] == syl2[0] and syl2[0] == '4'): 
        return True # because can swap order 
    return syl1==syl2 


syl3to1s = [] 
fin = open('./counter_output/3-to-1/syllogisms.txt', 'r') 
for i in range(56): 
    syl = [] 
    for _ in range(4): 
        syl.append(fin.readline().strip()) 
    fin.readline() 
    syl3to1s.append(syl) 
fin.close() 

syl2to1_ins = [] 
syl2to1_outs = [] 
fin = open('./counter_output/2-to-1/syllogisms.txt', 'r') 
for i in range(30): 
    syl = [] 
    for _ in range(2): 
        syl.append(fin.readline().strip()) 
    syl2to1_ins.append(syl) 

    syl2to1_outs.append(fin.readline().strip()) 

    fin.readline() 

fin.close() 

#print(syl3to1s) 
#print(syl2to1_ins) 
#print(syl2to1_outs) 

for syl3 in syl3to1s: 
    # try first decompose 
    try: 
        i = syl2to1_ins.index(syl3[:2]) 
        j = syl2to1_ins.index(join_syllogisms_first_decompose(syl2to1_outs[i], syl3[2])) 
        if syllogisms_are_equal(syl2to1_outs[j], syl3[3]): 
            pass 
        else: 
            print("FIRST DECOMPOSE IS WRONG: ", end='') 
            print(syl3, i, j) 
            print("OUTPUT:",syl2to1_outs[j]) 
            print("TARGET:", syl3[3]) 
    except Exception as e: 
        print(e) 
        print("UNABLE TO FIRST DECOMPOSE: ", end='') 
        print(syl3, end=' ') 
        try: 
            print(i, end=' ') 
        except: 
            pass 
        try: 
            print(j, end=' ') 
        except: 
            pass 
        print() 

    # try second decompose 
    try: 
        i = syl2to1_ins.index(left_shift_1(syl3[1:3])) 
        j = syl2to1_ins.index(join_syllogisms_second_decompose(syl3[0], syl2to1_outs[i])) 
        if syllogisms_are_equal(syl2to1_outs[j], syl3[3]): 
            pass 
        else: 
            print("SECOND DECOMPOSE IS WRONG: ", end='') 
            print(syl3, i, j) 
            print("OUTPUT:",syl2to1_outs[j]) 
            print("TARGET:", syl3[3]) 
    except Exception as e: 
        print(e) 
        print("UNABLE TO SECOND DECOMPOSE: ", end='') 
        print(syl3, end=' ') 
        try: 
            print(i, end=' ') 
        except: 
            pass 
        try: 
            print(j, end=' ') 
        except: 
            pass 
        print() 

print("DONE!") 

# when run, this only prints "DONE!", proving that this irreducible 3-to-1 syllogisms cannot be definitly true. 
