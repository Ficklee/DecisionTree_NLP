#coding:utf-8
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import logging

inFile = 'corpus.txt'
outFile = 'output_demoModel.out'
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = word2vec.Word2Vec(LineSentence(inFile),size=100,window=3,min_count=1)
print model.wv[u'理']