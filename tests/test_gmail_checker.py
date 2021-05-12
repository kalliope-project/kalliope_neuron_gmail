import unittest

from kalliope.core.NeuronModule import MissingParameterException
from kalliope.neurons.gmail_checker.gmail_checker import Gmail_checker


class TestGmail_Checker(unittest.TestCase):

    def setUp(self):
        self.client_secret_file="client_secret_file"

    def testParameters(self):
        def run_test(parameters_to_test):
            with self.assertRaises(MissingParameterException):
                Gmail_checker(**parameters_to_test)

        # empty
        parameters = dict()
        run_test(parameters)

        # missing password
        parameters = {
            "client_secret_file": self.client_secret_file
        }
        run_test(parameters)


if __name__ == '__main__':
    unittest.main()

