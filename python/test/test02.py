import unittest
from test.test01 import soma

class TesteSoma(unittest.TestCase):
    def test_retorno_soma_10_10(self):
        self .assertEqual(soma(10, 10), 20)
