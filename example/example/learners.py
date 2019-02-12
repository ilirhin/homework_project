from sklearn.ensemble import RandomForestClassifier


class Simple(object):
    def __call__(self, X_data, y_data):
        """learns model on dataset

        :param X_data: features matrix
        :param y_data: targets
        :return: RandomForestClassifier
        """
        return RandomForestClassifier().fit(X_data, y_data)
