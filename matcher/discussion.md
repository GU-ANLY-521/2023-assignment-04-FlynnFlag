B:

|                    | Threshold | Precision   | Recall              | F1                 |
| -------------------|-----------|-------------|---------------------|--------------------|
| Exact Match        |     /     | 1.0         |2.001641345903641e-05|4.00320256204964e-05|
| Jaccard Similarity |    0.028  | 1.0         |0.6870033427410477   |0.81446589385508    |
| Levenshtein        |     3     | 1.0         |0.9999799835865409   |0.9999899916931053  |
| Nearest Neighbors  |           | 1.0         |0.2702816309373686   |0.4255459960291198  |


D:
If we increase the threshold, then less pairs will be consider as matched. The recall and F1 will decrease. If we decrease the threshold, the situation will be opposite.

1.0 means the two names should be exactly the same, which is the same as "Exact Match" method.
precision:1, Recall:0.004163413999479573

0.1 means most of the pairs will be considered as matched.
precision:1, Recall: 0.5627614644008087


