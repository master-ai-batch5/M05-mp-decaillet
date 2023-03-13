import src.preprocessing
from src.preprocessing import Preprocessor


class PreprocessorFactory:
    def __init__(self, type: str, polynomial_kwargs: dict = None):
        if type not in self.allowed_types:
            raise ValueError(f"Unknown preprocessor type '{type}'")
        if type != "polynomial" and polynomial_kwargs is not None:
            raise ValueError("polynomial_kwargs should be None for non-polynomial preprocessors")
        if polynomial_kwargs is None:
            polynomial_kwargs = {}
        if not isinstance(polynomial_kwargs, dict):
            raise TypeError("polynomial_kwargs should be a dict")
        self._type = type
        self._polynomial_kwargs = polynomial_kwargs

    def create(self) -> Preprocessor:
        if self._type == "min-max":
            return src.preprocessing.MinMaxPreprocessor()
        if self._type == "standard":
            return src.preprocessing.StandardPreprocessor()
        if self._type == "polynomial":
            return src.preprocessing.PolynomialPreprocessor(**self._polynomial_kwargs)

    @classmethod
    @property
    def allowed_types(cls) -> list[str]:
        return ["min-max", "standard", "polynomial"]
