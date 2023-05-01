from matcher.utils.parse_tsv import TsvIterator
from matcher.name_matcher import ExactScorer,JaccardScorer,LevenshteinScorer,TFIDF_matcher

file = "data/names.tsv"
items=TsvIterator(file)
def task1():
    file = "data/names.tsv"
    items=TsvIterator(file)
    for item in items:
        ExactScorer(item.name1,item.name2).score()

def task2():
    file = "data/names.tsv"
    items=TsvIterator(file)
    for item in items:
        JaccardScorer(item.name1,item.name2).score()

def task3():
    file = "data/names.tsv"
    items=TsvIterator(file)
    for item in items:
        LevenshteinScorer(item.name1,item.name2).score()

def task4():
    file = "data/names.tsv"
    items=TsvIterator(file)
    for item in items:
        TFIDF_matcher(item.name1,item.name2).score()

task1()