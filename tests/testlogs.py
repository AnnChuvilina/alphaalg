import logs.csv
import unittest


class TestCsvLogs(unittest.TestCase):
    def setUp(self):
        self.log = logs.csv.CsvBpmLog('./../datasets/training_log_1.csv')

    def test_1_initcsv(self):
        pass

    def test_2_read(self):
        assert len(self.log.cases()) == 3

    def test_3_readact(self):
        assert len(self.log.activities()) == 5

    def test_4_trace(self):
        assert len(self.log.traces()) == 3

    def test_5_count(self):
        assert self.log.traces().count('aed') == 1

class Test2CsvLogs(unittest.TestCase):
    def setUp(self):
        self.logb = logs.csv.CsvBpmLog('./../datasets/training_log_2.csv')

    def test_2_1_read(self):
        assert self.logb.trace('1') == 'fihrmtqenjd'

    def test_2_2_read(self):
        assert self.logb.trace('2') != 'fdsfjdsfjkdsj'

    def test_3_1_case(self):
        assert len(self.logb.cases()) == 1000

    def test_4_1_trace(self):
        assert len(self.logb.traces()) == 1000

if __name__ == '__main__':
    unittest.main()