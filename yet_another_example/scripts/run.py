import os

import pandas
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

from yet_another_example import evaluation
from yet_another_example import features_extractors


if __name__ == '__main__':
    df = pandas.read_csv(
        os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'HR.csv'))
    for with_mean in [False, True]:
        for with_std in [False, True]:
            for algo in [LogisticRegression(solver='lbfgs'), RandomForestClassifier(n_estimators=50)]:
                print(type(algo).__name__)
                print('with_mean={}, with_std={}'.format(with_mean, with_std))
                X_data = features_extractors.Scaler(with_mean, with_std)(df)
                y_data = np.array(df['left'])
                evaluation.run(algo, X_data, y_data)
                print()
