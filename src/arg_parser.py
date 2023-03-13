import argparse

from src.estimating import EstimatorFactory
from src.preparator import PreparatorFactory
from src.preprocessing import PreprocessorFactory


class ArgParser:
    def __init__(self, argv=None):
        parser = argparse.ArgumentParser(
            description="M05-mp-decaillet (https://github.com/master-ai-batch5/M05-mp-decaillet)")

        parser.add_argument("--seed",
                            help="seed to lock random number generation",
                            type=int, default=None)

        parser.add_argument("--dataset",
                            help="which dataset to use",
                            choices=PreparatorFactory.allowed_types, default="boston")

        parser.add_argument("--dataset-source",
                            help="where to get the dataset from",
                            choices=PreparatorFactory.allowed_sources, default="file")

        parser.add_argument("--preprocessor-type",
                            help="type of preprocessor to use",
                            choices=PreprocessorFactory.allowed_types, default="standard")

        help_polynomial_preprocessor_kwargs = (
            "kwargs to pass to PolynomialFeatures. "
            "Only valid if --preprocessor-type=polynomial. "
            "Format: comma-separated 'field:position' pairs (e.g. 'degree: 2, interaction_only: False, include_bias: True, order: F'). "
            "See https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html for more details.")
        parser.add_argument("--polynomial-preprocessor-kwargs",
                            help=help_polynomial_preprocessor_kwargs,
                            type=self._kwargs, default=None)

        parser.add_argument("--estimator-type",
                            help="type of estimator to use",
                            choices=EstimatorFactory.allowed_types, default="decision-tree")

        parser.add_argument("--evaluation-count",
                            help="number of times to evaluate the model",
                            type=self._strictly_positive_int, default=3)

        args = parser.parse_args(argv)

        self._seed = args.seed
        self._preparator_factory = PreparatorFactory(args.dataset, args.dataset_source)
        self._preprocessor_factory = PreprocessorFactory(args.preprocessor_type, args.polynomial_preprocessor_kwargs)
        self._estimator_factory = EstimatorFactory(args.estimator_type)
        self._evaluation_count = args.evaluation_count

    @property
    def seed(self) -> int:
        return self._seed

    @property
    def preparator_factory(self) -> None:
        return self._preparator_factory

    @property
    def preprocessor_factory(self) -> PreprocessorFactory:
        return self._preprocessor_factory

    @property
    def estimator_factory(self) -> EstimatorFactory:
        return self._estimator_factory

    @property
    def evaluation_count(self) -> int:
        return self._evaluation_count

    @classmethod
    def _kwargs(cls, str_value) -> dict:
        try:
            dict_value = {k.strip(): v.strip() for k, v in (i.split(':') for i in str_value.split(','))}
            for k, v in dict_value.items():
                if v == "True":
                    dict_value[k] = True
                elif v == "False":
                    dict_value[k] = False
                elif v.isdigit():
                    dict_value[k] = int(v)
            return dict_value
        except ValueError:
            pass
        raise argparse.ArgumentTypeError(f"{str_value} is not a dictionary")

    @classmethod
    def _strictly_positive_int(cls, str_value) -> bool:
        try:
            int_value = int(str_value)
            if int_value > 0:
                return int_value
            raise ValueError
        except ValueError:
            pass
        raise argparse.ArgumentTypeError(f"{str_value} is not a positive integer")
