import pandas as pd


class BostonPreparator():  # pragma: no cover TODO add unit tests
    def load_data(self) -> pd.DataFrame:
        features_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                          'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
        targets_names = ['MEDV']
        data = pd.read_csv('data/housing.data', delim_whitespace=True, names=features_names + targets_names)
        dataset = {"dataset": data, "features_names": features_names, "targets_names": targets_names}
        return dataset