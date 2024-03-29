from sklearn import preprocessing

from decm05.preprocessing import SkLearnPreprocessorBase


class StandardPreprocessor(SkLearnPreprocessorBase):
    @property
    def name(self) -> str:
        return "standard"

    def _get_scaler(self):
        return preprocessing.StandardScaler()
