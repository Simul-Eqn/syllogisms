import os

parent_dir = os.path.join(os.getcwd(), 'counter_output') 

for i in range(2,7): 
    path = os.path.join(parent_dir, str(i)+"-to-1", "syllogisms.txt") 
    fin = open(path, 'r') 
    syls = fin.readlines() 
    fin.close() 

    count = 0
    out_syl = [] 
    for syl_part in syls:
        if syl_part.strip() == "":
            
            # save out_syl to a .syl file 
            outfile = open(os.path.join(parent_dir, str(i)+"-to-1", "syl"+str(count)+".syl"), 'w') 
            for sidx in range(len(out_syl)-1): 
                outfile.write(out_syl[sidx]) 
            outfile.write("eval 1\n") 
            outfile.write(out_syl[-1]) 
            outfile.close()
            count += 1 

            # re-initialize for next one 
            out_syl = []
        else:
            out_syl.append(syl_part)
    

    

