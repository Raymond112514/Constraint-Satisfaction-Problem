from CSP.CSP import CSP
import unittest

class TestBasicFunctionality(unittest.TestCase):

    def setUp(self):
        self.CSP1 = CSP([0, 1], [(0, 0), (0, 1), (1, 0), (1, 1)], {})
        self.CSP2 = CSP([0, 1], [(0, 0), (0, 1), (1, 0), (1, 1)], {(1, 1): 0})

    def test1(self):
        assert self.CSP1.domain == [0, 1]
        assert self.CSP1.assignments == {(0, 0): None, (0, 1): None, (1, 0): None, (1, 1): None}
        assert self.CSP1.numAssigned == 0
        assert self.CSP2.assignments == {(0, 0): None, (0, 1): None, (1, 0): None, (1, 1): 0}
        assert self.CSP2.numAssigned == 1

    def test2(self):
        assert self.CSP1.getUnassignedList() == {(0, 0): [0, 1], (0, 1): [0, 1], (1, 0): [0, 1], (1, 1): [0, 1]}
        assert self.CSP2.getUnassignedList() == {(0, 0): [0, 1], (0, 1): [0, 1], (1, 0): [0, 1]}

    def test3(self):
        assert self.CSP1.assign((0, 0), 0) == [0, 1]
        assert self.CSP1.assignments == {(0, 0): 0, (0, 1): None, (1, 0): None, (1, 1): None}
        assert self.CSP1.getUnassignedList() == {(0, 1): [0, 1], (1, 0): [0, 1], (1, 1): [0, 1]}
        assert self.CSP1.assign((0, 1), 1) == [0, 1]
        assert self.CSP1.assignments == {(0, 0): 0, (0, 1): 1, (1, 0): None, (1, 1): None}
        assert self.CSP1.getUnassignedList() == {(1, 0): [0, 1], (1, 1): [0, 1]}

    def test4(self):
        self.CSP1.assign((0, 0), 0)
        self.CSP1.assign((0, 1), 1)
        assert self.CSP1.numAssigned == 2
        assert self.CSP1.unassign((0, 1)) is None
        assert self.CSP1.numAssigned == 1
        assert self.CSP1.assignments == {(0, 0): 0, (0, 1): None, (1, 0): None, (1, 1): None}
        assert self.CSP1.getUnassignedList() == {(0, 1): [0, 1], (1, 0): [0, 1], (1, 1): [0, 1]}

    def test5(self):
        assert self.CSP1.complete() is False
        assert self.CSP2.complete() is False


