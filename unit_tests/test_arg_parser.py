import unittest.mock

from src import ArgParser
from src.estimating import EstimatorFactory
from src.preparator import PreparatorFactory
from src.preprocessing import PreprocessorFactory


class TestArgParser(unittest.TestCase):
    def setUp(self) -> None:
        self.addCleanup(unittest.mock.patch.stopall)

        self._preparator_factory_class_mock = unittest.mock.patch('src.arg_parser.PreparatorFactory').start()
        self._preparator_factory_class_mock.allowed_types = PreparatorFactory.allowed_types
        self._preparator_factory_class_mock.allowed_sources = PreparatorFactory.allowed_sources

        self._preprocessor_factory_class_mock = unittest.mock.patch('src.arg_parser.PreprocessorFactory').start()
        self._preprocessor_factory_class_mock.allowed_types = PreprocessorFactory.allowed_types

        self._estimator_factory_class_mock = unittest.mock.patch('src.arg_parser.EstimatorFactory').start()
        self._estimator_factory_class_mock.allowed_types = EstimatorFactory.allowed_types

    def test__has_defaults(self) -> None:
        argv = []

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, None)
        self._preparator_factory_class_mock.assert_called_once_with('boston', 'file')
        self.assertEqual(arg_parser.preparator_factory, self._preparator_factory_class_mock.return_value)
        self._preprocessor_factory_class_mock.assert_called_once_with('standard', None)
        self.assertEqual(arg_parser.preprocessor_factory, self._preprocessor_factory_class_mock.return_value)
        self._estimator_factory_class_mock.assert_called_once_with('decision-tree')
        self.assertEqual(arg_parser.estimator_factory, self._estimator_factory_class_mock.return_value)
        self.assertEqual(arg_parser.evaluation_count, 3)

    def test__can_set_values(self) -> None:
        argv = ['--seed', '-12',
                '--evaluation-count', '15',
                '--dataset', 'red-wine',
                '--dataset-source', 'url',
                '--preprocessor-type', 'polynomial',
                '--polynomial-preprocessor-kwargs', 'degree: 2, interaction_only: False, include_bias: True, order: F',
                '--estimator-type', 'linear-regression']  # This is the default, but it's the only allowed type.

        arg_parser = ArgParser(argv)

        self.assertEqual(arg_parser.seed, -12)
        self._preparator_factory_class_mock.assert_called_once_with('red-wine', 'url')
        self.assertEqual(arg_parser.preparator_factory, self._preparator_factory_class_mock.return_value)
        self._preprocessor_factory_class_mock.assert_called_once_with('polynomial', {
            "degree": 2, "interaction_only": False, "include_bias": True, "order": "F"
        })
        self.assertEqual(arg_parser.preprocessor_factory, self._preprocessor_factory_class_mock.return_value)
        self._estimator_factory_class_mock.assert_called_once_with('linear-regression')
        self.assertEqual(arg_parser.estimator_factory, self._estimator_factory_class_mock.return_value)
        self.assertEqual(arg_parser.evaluation_count, 15)

    def test__seed_must_be_int(self) -> None:
        argv = ['--seed', '1.3']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--seed', 'forty-two']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__preparator_type_must_be_allowed(self) -> None:
        argv = ['--preparator-type', 'file']  # 'file' is a valid source, not a valid type
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__preparator_source_must_be_allowed(self) -> None:
        argv = ['--preparator-source', 'boston']  # 'boston' is a valid type, not a valid source
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__preprocessor_type_must_be_allowed(self) -> None:
        argv = ['--preprocessor-type', 'foo']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__preprocessor_kwargs_must_be_valid(self) -> None:
        argv = ['--preprocessor-type', 'polynomial',
                '--polynomial-preprocessor-kwargs', 'this string is not interpretable as a dict']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__estimator_type_must_be_allowed(self) -> None:
        argv = ['--estimator-type', 'foo']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

    def test__evaluation_count_must_be_positive(self) -> None:
        argv = ['--evaluation-count', '0']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--evaluation-count', '-1']
        with self.assertRaises(SystemExit):
            ArgParser(argv)

        argv = ['--evaluation-count', '12.8']
        with self.assertRaises(SystemExit):
            ArgParser(argv)
