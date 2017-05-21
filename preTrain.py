import re
import multiprocessing
from multiprocessing import Pool
def Preprocess(line):
    tmpline = line.decode('utf-8')
    a=list(tmpline)
    result =' '.join(a).encode('utf-8')
    return result
f = open('outfile.dat','r')
pool = Pool(3)
result_lst = pool.map(Preprocess,f,chunksize=400)
pool.close()
pool.join()
f.close()
fout = open('Pre_Train.txt','w')
fout.writelines(result_lst)
fout.close()
