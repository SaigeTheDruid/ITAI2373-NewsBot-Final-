from sklearn.metrics import classification_report, accuracy_score

def get_classification_report(y_true, y_pred):
    report = classification_report(y_true, y_pred, output_dict=True)
    return report

def print_accuracy(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    print(f"Accuracy: {accuracy:.4f}")
    return accuracy

