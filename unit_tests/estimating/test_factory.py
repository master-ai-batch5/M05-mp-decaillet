import unittest.mock

from src.estimating import EstimatorFactory


class TestEstimatorFactory(unittest.TestCase):
    def test__can_init_linear_regression(self):
        estimator_factory = EstimatorFactory("linear-regression")
        self.assertIsNotNone(estimator_factory)

    def test__can_init_decision_tree(self):
        estimator_factory = EstimatorFactory("decision-tree")
        self.assertIsNotNone(estimator_factory)

    def test__init_fails__on_bad_type(self):
        with self.assertRaisesRegex(ValueError, "^Unknown estimator type 'foo'$"):
            EstimatorFactory("foo")

    def test__can_create_linear_regression(self):
        estimator_factory = EstimatorFactory("linear-regression")

        with unittest.mock.patch("src.estimating.LinearRegressionEstimator") as mock:
            estimator = estimator_factory.create()

        mock.assert_called_once_with()
        self.assertIsInstance(estimator, mock.return_value.__class__)

    def test__can_create_decision_tree(self):
        estimator_factory = EstimatorFactory("decision-tree")

        with unittest.mock.patch("src.estimating.DecisionTreeEstimator") as mock:
            estimator = estimator_factory.create()

        mock.assert_called_once_with()
        self.assertIsInstance(estimator, mock.return_value.__class__)
