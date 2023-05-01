from matcher.name_matcher import ExactScorer,JaccardScorer,LevenshteinScorer,TFIDF_matcher
import numpy as np
import pandas as pd
from matcher.utils.parse_tsv import TsvIterator

res1=[]
res2=[]
res3=[]
res4=[]
items=TsvIterator('tests/data/test.tsv')
for item in items:
    res1.append(ExactScorer(item.name1,item.name2).score())
    res2.append(JaccardScorer(item.name1,item.name2,threshold=0.028).score())
    res3.append(LevenshteinScorer(item.name1,item.name2,threshold=3).score())
    res4.append(TFIDF_matcher(item.name1,item.name2,threshold=0.4994).score())



assert np.allclose(res1, [0,0,0], atol=1e-8)

assert np.allclose(res2, [1,1,1], atol=1e-8)

assert np.allclose(res3, [1,1,1], atol=1e-8)

assert np.allclose(res4, [1,1,1], atol=1e-8)

