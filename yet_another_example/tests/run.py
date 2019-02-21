import unittest
import os

import pandas
import numpy as np

from yet_another_example import features_extractors


class TestFeaturesExtractors(unittest.TestCase):

    def setUp(self):
        self.df = pandas.read_csv(
            os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, 'HR.csv'))

    def test_trivial_features_number(self):
        self.assertEqual(
            len(features_extractors.FEATURES_NAMES),
            features_extractors.Trivial()(self.df).shape[1]
        )

    def test_scaler_features_number(self):
        for with_mean in [False, True]:
            for with_std in [False, True]:
                self.assertEqual(
                    len(features_extractors.FEATURES_NAMES),
                    features_extractors.Scaler(with_mean, with_std)(self.df).shape[1]
                )

    def test_scaler_mean(self):
        for with_std in [False, True]:
            self.assertTrue(np.max(np.abs(np.mean(
                features_extractors.Scaler(True, with_std)(self.df),
                axis=0
            ))) < 1e-10)

    def test_scaler_std(self):
        for with_mean in [False, True]:
            self.assertTrue(np.max(np.abs(np.std(
                features_extractors.Scaler(with_mean, True)(self.df),
                axis=0
            ) - 1)) < 1e-10)


if __name__ == '__main__':
    unittest.main()
