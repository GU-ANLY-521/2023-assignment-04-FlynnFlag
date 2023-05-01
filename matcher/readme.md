## Function
This is a Fuzzy Name Matching package. It calculate the similarity of two names and output whether they are similiar.

The input should be a file containing two names, and the output is the scores

## How to use
To implement this package, you should run the main file with argparse.

## Parameters
There are four parameters in this package.
1. The path of the file input
2. The algorithmn used for calculate the similarity score. There are four candidate algorithmns: Exact Match, Jaccard Similarity,Levenshtein and Nearest Neighbors, you should input. The options are [`ExactMatch`, `Jaccard`, `Levenshtein`, `tfidf`,`Soundex`]
3. The threshold for each algorithmn. It should be a number
4. Whether to print the evaluation.

## Command
To implement it, run the following code:
python main.py -f <path_to_dataset> -s <scoring_algorithm> -t <threshold> -p 

where -t and -p is not necessary. If you want to include these two parameter, use `-t 1` or `-p` for example.