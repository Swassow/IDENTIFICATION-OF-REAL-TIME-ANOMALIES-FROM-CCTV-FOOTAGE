import matplotlib.pyplot as plt

def plot(mean_fpr,mean_tpr,mean_auc):
    plt.figure(figsize=(8, 8))
    plt.plot(mean_fpr, mean_tpr, color='darkorange', lw=2, label=f'Mean ROC curve (AUC = {mean_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'Receiver Operating Characteristic (ROC) Curve - ')
    plt.legend(loc='lower right')
    plt.show()