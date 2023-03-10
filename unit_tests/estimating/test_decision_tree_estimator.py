import unittest

import pandas as pd

from src.estimating import DecisionTreeEstimator


class TestDecisionTreeEstimator(unittest.TestCase):
    def test__happy_path(self):
        estimator = DecisionTreeEstimator()

        with self.subTest("fit"):
            training_features = pd.DataFrame(data={
                "feature 1": [1.0, 2.0, 3.0],
                "feature 2": [4.0, 5.0, 6.0]
            })
            training_targets = pd.DataFrame(data={
                "target 1": [7.0, 8.0, 9.0]
            })

            actual = estimator.fit(training_features, training_targets)

            self.assertIsNone(actual)

        with self.subTest("predict"):
            test_features = pd.DataFrame(data={
                "feature 1": [4.0, 5.0, 6.0],
                "feature 2": [7.0, 8.0, 9.0]
            })

            actual = estimator.predict(test_features)

            pd.testing.assert_frame_equal(actual, pd.DataFrame(data={
                "target 1": [9.0, 9.0, 9.0]
            }))

    def test__fails_it_not_fit(self):
        estimator = DecisionTreeEstimator()
        test_features = pd.DataFrame(data={"feature 1": [4.0, 5.0, 6.0]})

        with self.assertRaisesRegex(RuntimeError, "^Estimator has not been fitted yet.$"):
            estimator.predict(test_features)

    def test__fails_if_columns_dont_match(self):
        estimator = DecisionTreeEstimator()
        training_features = pd.DataFrame(data={
            "feature 1": [1.0, 2.0, 3.0],
            "feature 2": [4.0, 5.0, 6.0]
        })
        training_targets = pd.DataFrame(data={
            "target 1": [7.0, 8.0, 9.0]
        })
        test_features = pd.DataFrame(data={
            "feature 1": [4.0, 5.0, 6.0],
            "feature 3": [7.0, 8.0, 9.0]  # <-- different column name
        })

        estimator.fit(training_features, training_targets)

        with self.assertRaisesRegex(ValueError, "^Features have different columns than training features.$"):
            estimator.predict(test_features)
