from sklearn.model_selection import cross_val_score


def run(estimator, X_data, y_data):
    for metric in ['accuracy', 'precision', 'recall', 'f1']:
        print(metric, cross_val_score(estimator, X_data, y_data, scoring=metric, cv=2).mean())
