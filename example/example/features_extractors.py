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
