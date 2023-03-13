from sklearn.tree import DecisionTreeRegressor

from src.estimating import SkLearnEstimatorBase


class RegressionEstimator(SkLearnEstimatorBase):
    def _get_model(self):
        return DecisionTreeRegressor(max_depth=7, random_state=42)
