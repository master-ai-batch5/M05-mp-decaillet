import abc

import pandas as pd

from decm05.preprocessing import Preprocessor


class SkLearnPreprocessorBase(Preprocessor):
    def __init__(self) -> None:
        super().__init__()
        self._scaler = None
        self._columns = []

    def fit_transform(self, features: pd.DataFrame) -> pd.DataFrame:
        self._columns = features.columns
        self._scaler = self._get_scaler()

        scaled_features = self._scaler.fit_transform(features)

        return pd.DataFrame(data=scaled_features,
                            index=features.index,
                            columns=self._get_scaled_columns_names())

    def transform(self, features: pd.DataFrame) -> pd.DataFrame:
        if self._scaler is None:
            raise RuntimeError("Preprocessor has not been fitted yet.")
        if not self._columns.equals(features.columns):
            raise ValueError("Features have different columns than training features.")

        scaled_features = self._scaler.transform(features)

        return pd.DataFrame(data=scaled_features,
                            index=features.index,
                            columns=self._get_scaled_columns_names())

    @abc.abstractmethod
    def _get_scaler(self):
        raise NotImplementedError("override me")  # pragma: no cover

    def _get_scaled_columns_names(self) -> list[str]:
        return [f"{column} (scaled)" for column in self._columns]
