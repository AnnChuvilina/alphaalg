import unittest
import logs
from miners.alphaminer import *
from logs.csv import CsvBpmLog

class AlphaMinerTest(unittest.TestCase):

    def test_1(self):
        self.log = logs.csv.CsvBpmLog('./../datasets/training_log_1.csv')
        assert alphaminer(self.log).transition('b')


