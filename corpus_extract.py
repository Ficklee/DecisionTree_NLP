import re
import sys
import numpy as np
import multiprocessing
from multiprocessing import Pool
def WriteOut(line):
    content_start = re.compile(r'^<content>')
    content_end = re.compile(r'</content>$')
    if re.match(content_start,line):
        return re.sub(content_end,'',re.sub(content_start,'',line)).decode('gbk','ignore').encode('utf-8')
    else:
        return ''
    
if len(sys.argv)!=2:
    print "usage:python "+sys.argv[0]+' [imported]'
    exit(1)
Infile = sys.argv[1]
doc_start = re.compile(r'^<doc>')
doc_end  =re.compile(r'^</doc>')
content_start = re.compile(r'^<content>')
content_end = re.compile(r'</content>$')

fread=open(Infile,'r')
pool=Pool(3)
resultlst = pool.map(WriteOut,fread)
pool.close()
pool.join()
fread.close()
fout=open('outfile.dat','w')
fout.writelines(resultlst)
fout.close()