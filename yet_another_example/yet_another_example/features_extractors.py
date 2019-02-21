from sklearn import preprocessing


FEATURES_NAMES = [
    'last_evaluation', 'number_project', 
    'average_montly_hours', 'time_spend_company', 
    'Work_accident', 'promotion_last_5years'
]


class Trivial(object):
    def __call__(self, df):
        """extracts features from data

        :param df: pandas.DataFrame with original HR.csv data
        :return: numpy.array for features_matrix
        """
        return df[FEATURES_NAMES].to_numpy()


class Scaler(object):
    def __init__(self, with_mean=True, with_std=True):
        """
        :param with_mean: option for sklearn.preprocessing.StandardScaler
        :param with_std: option for sklearn.preprocessing.StandardScaler
        """
        self.with_mean = with_mean
        self.with_std = with_std

    def __call__(self, df):
        """extracts features from data

        :param df: pandas.DataFrame with original HR.csv data
        :param with_mean: option for sklearn.preprocessing.StandardScaler
        :param with_std: option for sklearn.preprocessing.StandardScaler
        :return: numpy.array for features_matrix
        """
        return preprocessing.StandardScaler(
            with_mean=self.with_mean, with_std=self.with_std
        ).fit_transform(df[FEATURES_NAMES].to_numpy())
