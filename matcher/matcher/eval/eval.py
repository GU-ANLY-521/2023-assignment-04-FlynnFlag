from sklearn.metrics import precision_score,recall_score,f1_score,precision_recall_curve
import matplotlib.pyplot as plt
def evaluate(res,metric):
    if metric == "precision":
        return precision_score(res[0], res[1])
    elif metric == "recall":
        return recall_score(res[0], res[1])
    elif metric == "F1":
        return f1_score(res[0], res[1])

def plot_pr_curve(res):
    precision, recall, thresholds = precision_recall_curve(res[0], res[1])
    plt.plot(thresholds,recall[:-1])
    plt.plot(thresholds,precision[:-1])
    plt.xlabel('Thresholds')
    plt.ylabel('Recall and Precision')
    plt.show()

