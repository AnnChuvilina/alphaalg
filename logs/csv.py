import csv
from logs.log import BpmLog

class CsvBpmLog (BpmLog):
    def __init__(self, filename):
        BpmLog.__init__(self)
        self._cases = dict()
        self._activities = set()
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(reader)
            for row in reader:
                self._cases[row[1]] = self._cases.get(row[1], '')+row[0]
                self._activities.add(row[0])
        self.name = filename

    def cases(self):
        return list(sorted(list(self._cases.keys())))

    def activities(self):
        return list(sorted(list(self._activities)))

    def trace(self, caseid):
        return self._cases[caseid]

    def traces(self):
        return list(self._cases.values())
