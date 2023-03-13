from random import seed as set_random_seed

from src import ArgParser, Evaluator


class Service:
    """
    Entry point for the application, responsible for creating the necessary objects and inject
    them into the Evaluator class.

    Usage:

    * ``Service().run()``
    * ``Service(["--dataset=wine", "--seed=42"]).run()``
    * etc.
    """

    def __init__(self, argv=None) -> None:
        arg_parser = ArgParser(argv=argv)

        set_random_seed(arg_parser.seed)
        self._preparator_factory = arg_parser.preparator_factory
        self._preprocessor_factory = arg_parser.preprocessor_factory
        self._estimator_factory = arg_parser.estimator_factory
        self._evaluation_count = arg_parser.evaluation_count

    def run(self) -> None:
        """Run the application."""
        evaluator = Evaluator(self._preparator_factory.create(),
                              self._preprocessor_factory.create(),
                              self._estimator_factory.create(),
                              self._evaluation_count)
        mae = evaluator.evaluate()
        print(f"MAE: {mae}")
