B:

|                    | Threshold | Precision   | Recall              | F1                 |
| -------------------|-----------|-------------|---------------------|--------------------|
| Exact Match        |     /     | 1.0         |2.001641345903641e-05|4.00320256204964e-05|
| Jaccard Similarity |    0.028  | 1.0         |0.6870033427410477   |0.81446589385508    |
| Levenshtein        |     3     | 1.0         |0.9999799835865409   |0.9999899916931053  |
| Nearest Neighbors  |    0.4994 | 1.0         |0.6888248363658199   |0.8157445598065708  |
| Soundex            |     /     | 1.0         |0.3782901979623291   |0.5489267768451015  |


D:
If we increase the threshold, then less pairs will be consider as matched. The recall and F1 will decrease. If we decrease the threshold, the situation will be opposite.

1.0 means the two names should be exactly the same, which is the same as "Exact Match" method.
precision:1, Recall:0.017254148401689387, F1:0.033922984592983214

0.01 means most of the pairs will be considered as matched.
precision:1, Recall: 0.6870033427410477, F1:0.81446589385508 

E:
The function is written and run in the `hyperparameter_setting`file 

G:(a)
If we use full name as tokens, there will be only one or two features for most of names, which will make our result useless.

K:
It seems that the algorithmn in our practice do not apply. However, I found that the prounication between English name and Russian name is still similar. For example, `Robert` and `Роберт`. So we may apply soundex algorithmn, which I used in the bonus part, to paired the names. Russian is consists of alphabets, so it can also be encoded as numbers.


Bonus
a:
The method I find is called `Soundex algorithm`.The Soundex algorithm is a phonetic algorithm that was originally developed in 1918 by Robert C. Russell and Margaret King Odell as a way to index and search U.S. census records by surname. It encode the letters to numbers based on their pronunciation. Names that sound similiar are matched. It first do some word normalization: upper the words, remove consecutive duplicates, and then encode the letters based on empirical observations of how certain letters in English names tend to be pronounced similarly. 

b. 
If I don't use the multiprocessing library, the time is 63.31148109998321 second. When using the multiprocessing library, the time is 63.877323499997146.

My machine only have one CPU. Multiprocessing will not provide any performance benefits since it requires multiple CPU cores to run tasks in parallel. So the result makes sense.