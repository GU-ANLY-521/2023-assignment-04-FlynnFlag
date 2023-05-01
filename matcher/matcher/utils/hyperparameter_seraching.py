from matcher.utils.parse_tsv import TsvIterator
from matcher.name_matcher import ExactScorer,JaccardScorer,LevenshteinScorer,TFIDF_matcher
from matcher.eval import eval


# part1 generate scores
res1=[]
res2=[]
res3=[]
res4=[]
raw_score2,raw_score3,raw_score4=[],[],[]
file = "data/names.tsv"
items=TsvIterator(file)
for item in items:
    res1.append(ExactScorer(item.name1,item.name2).score())
    raw_score2.append(JaccardScorer(item.name1,item.name2)._score())
    res2.append(JaccardScorer(item.name1,item.name2,threshold=0.028).score())
    raw_score3.append(LevenshteinScorer(item.name1,item.name2)._score())
    res3.append(LevenshteinScorer(item.name1,item.name2,threshold=3).score())
    raw_score3.append(LevenshteinScorer(item.name1,item.name2)._score())
    raw_score4.append(TFIDF_matcher(item.name1,item.name2)._score())
    #res1.append(soundex(item.name1,item.name2).score())


ExactRes=[[1]*len(res1),res1]
print("The result of Exact Match is:", eval.evaluate(ExactRes,"precision"),eval.evaluate(ExactRes,"recall"),eval.evaluate(ExactRes,"F1"))


JacRes=[[1]*len(res2),res2]
print("The result of Jaccard Similarity is:",eval.evaluate(JacRes,"precision"),eval.evaluate(JacRes,"recall"),eval.evaluate(JacRes,"F1"))

LevenRes=[[1]*len(res3),res3]
print("The result of Levenshtein Similarity is:",eval.evaluate(LevenRes,"precision"),eval.evaluate(LevenRes,"recall"),eval.evaluate(LevenRes,"F1"))

tfidfRes=[[1]*len(res4),res4]
print("The result of Levenshtein Similarity is:",eval.evaluate(LevenRes,"precision"),eval.evaluate(LevenRes,"recall"),eval.evaluate(LevenRes,"F1"))

# part2 serach for best threhold 
# find the optimal threhold for jaccard
raw2=[[1]*len(raw_score2),raw_score2]
eval.plot_pr_curve(raw2)
print("0.028 is the best")

raw3=[[1]*len(raw_score3),raw_score3]
eval.plot_pr_curve(raw3)
print("3 is the best")

raw4=[[1]*len(raw_score4),raw_score4]
eval.plot_pr_curve(raw4)
print("0.4994 is the best")

