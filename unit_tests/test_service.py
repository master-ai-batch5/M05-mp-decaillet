import unittest.mock

from src import Service
from src.estimating import Estimator, EstimatorFactory
from src.preparator import Preparator, PreparatorFactory
from src.preprocessing import Preprocessor, PreprocessorFactory


class TestService(unittest.TestCase):
    def setUp(self) -> None:
        self.addCleanup(unittest.mock.patch.stopall)

        arg_parser_mock = unittest.mock.patch('src.service.ArgParser').start().return_value
        arg_parser_mock.seed = 12345
        arg_parser_mock.preparator_factory = unittest.mock.Mock(spec=PreparatorFactory)
        arg_parser_mock.preprocessor_factory = unittest.mock.Mock(spec=PreprocessorFactory)
        arg_parser_mock.estimator_factory = unittest.mock.Mock(spec=EstimatorFactory)
        arg_parser_mock.evaluation_count = 54321

        self._evaluator_class_mock = unittest.mock.patch('src.service.Evaluator').start()
        self._evaluator_mock = self._evaluator_class_mock.return_value

        self._preparator_mock = unittest.mock.Mock(spec=Preparator)
        arg_parser_mock.preparator_factory.create.return_value = self._preparator_mock

        self._preprocessor_mock = unittest.mock.Mock(spec=Preprocessor)
        arg_parser_mock.preprocessor_factory.create.return_value = self._preprocessor_mock

        self._estimator_mock = unittest.mock.Mock(spec=Estimator)
        arg_parser_mock.estimator_factory.create.return_value = self._estimator_mock

        self._print_mock = unittest.mock.patch('builtins.print').start()

    def test__constructor_sets_random_seed(self) -> None:
        with unittest.mock.patch('src.service.set_random_seed') as set_random_seed_mock:
            Service()

        set_random_seed_mock.assert_called_once_with(12345)

    def test_runs(self) -> None:
        self._evaluator_mock.evaluate.return_value = 42
        service = Service()
        service.run()
        self._evaluator_class_mock.assert_called_once_with(self._preparator_mock,
                                                           self._preprocessor_mock,
                                                           self._estimator_mock,
                                                           54321)
        self._evaluator_mock.evaluate.assert_called_once()
        self._print_mock.assert_called_once_with('MAE: 42')
