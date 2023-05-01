import argparse
import logging
import sys
sys.path.append(".")

from matcher.utils.parse_tsv import TsvIterator
from matcher.name_matcher import ExactScorer,JaccardScorer,LevenshteinScorer,TFIDF_matcher,Soundex
from matcher.eval import eval
logger = logging.getLogger(__name__)

def matcher(filepath,scorer,t=False,p=False):
    res=[]
    items=TsvIterator(filepath)
    if scorer=="ExactMatch":
        for item in items:
            res.append(ExactScorer(item.name1,item.name2).score())
        if p==True:
            ExactRes=[[1]*len(res),res]
            print("The result of Exact Match is:", eval.evaluate(ExactRes,"precision"),eval.evaluate(ExactRes,"recall"),eval.evaluate(ExactRes,"F1"))
        return res
    elif scorer=="Jaccard":
        if t==False:      
            for item in items:
                res.append(JaccardScorer(item.name1,item.name2,threshold=0.028).score())
        else:
            thres=float(t)
            for item in items:
                res.append(JaccardScorer(item.name1,item.name2,threshold=thres).score())
        if p ==True:
            JacRes=[[1]*len(res),res]
            print("The result of Jaccard Similarity is:",eval.evaluate(JacRes,"precision"),eval.evaluate(JacRes,"recall"),eval.evaluate(JacRes,"F1"))
        return res
    elif scorer=="Levenshtein":
        if t==False:      
            for item in items:
                res.append(LevenshteinScorer(item.name1,item.name2,threshold=3).score())
        else:
            thres=float(t)
            for item in items:
                res.append(LevenshteinScorer(item.name1,item.name2,threshold=thres).score())
        if p== True:
            LevenRes=[[1]*len(res),res]
            print("The result of Levenshtein Similarity is:",eval.evaluate(LevenRes,"precision"),eval.evaluate(LevenRes,"recall"),eval.evaluate(LevenRes,"F1"))
        return res
    elif scorer=="TFIDF":
        if t==False:      
            for item in items:
                res.append(TFIDF_matcher(item.name1,item.name2,threshold=0.4994).score())
        else:
            thres=float(t)
            for item in items:
                res.append(TFIDF_matcher(item.name1,item.name2,threshold=thres).score())
        if p== True:
            TFIDFRes=[[1]*len(res),res]
            print("The result of Levenshtein Similarity is:",eval.evaluate(TFIDFRes,"precision"),eval.evaluate(TFIDFRes,"recall"),eval.evaluate(TFIDFRes,"F1"))
        return res
    elif scorer=="Soundex":
        for item in items:
            res.append(Soundex(item.name1,item.name2).score())
        if p==True:
            SoundRes=[[1]*len(res),res]
            print("The result of Exact Match is:", eval.evaluate(SoundRes,"precision"),eval.evaluate(SoundRes,"recall"),eval.evaluate(SoundRes,"F1"))
        return res






if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="location of names.tsv file"
    )
    parser.add_argument("-f", "--data", required=True, help="path to data set")
    parser.add_argument("-s", "--scorer", required=True,help="name of algorithmn",
                        choices=["ExactMatch", "Jaccard", "Levenshtein", "TFIDF","Soundex"])
    parser.add_argument("-t", "--threshold", required=False, help="threshold for scorers,should be a number or False")
    parser.add_argument("-p","--print", required=False, action='store_true', help="prints out results,should be a boolen value")
    args = parser.parse_args()
    logger.info(f"{args.scorer} has started")
    if args.threshold and args.print:
        print(matcher(args.data,args.scorer,t=args.threshold,p=args.print))
    elif args.threshold:
        print(matcher(args.data,args.scorer,t=args.threshold))
    elif args.print:
        print(matcher(args.data,args.scorer,p=args.print))
    else:
        print(matcher(args.data,args.scorer))
    logger.info(f"{args.scorer} has finished")


            
