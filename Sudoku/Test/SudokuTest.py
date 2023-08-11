from Sudoku.Sudoku import Sudoku
import unittest

class TestBasicFunctionality(unittest.TestCase):

    def setUp(self):
        self.sudoku = Sudoku(2, {})

    def test1(self):
        assert self.sudoku.domain == [1, 2, 3, 4]
        assert self.sudoku.states == [(1, 1), (1, 2), (1, 3), (1, 4),
                                      (2, 1), (2, 2), (2, 3), (2, 4),
                                      (3, 1), (3, 2), (3, 3), (3, 4),
                                      (4, 1), (4, 2), (4, 3), (4, 4)]
        assignments = {}
        for state in self.sudoku.states:
            assignments[state] = None
        assert self.sudoku.assignments == assignments

        # Initial assignments
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------

    def test2(self):
        assert self.sudoku.complete() is False
        assert self.sudoku.consistent() is True

    def test3(self):
        assert self.sudoku.neighbor((1, 1)) == {(1, 2), (1, 3), (1, 4), (2, 1), (3, 1), (4, 1), (2, 2)}
        assert self.sudoku.neighbor((2, 2)) == {(2, 4), (1, 2), (2, 1), (1, 1), (4, 2), (2, 3), (3, 2)}

    def test4(self):
        # Assign (1,1) to 3:
        # Expect: assignment to change (1,1) entry becomes 3 and unassigned list without (1,1) entry
        self.sudoku.assign((1, 1), 3)
        assignments = {}
        unassignedList = {}
        for state in self.sudoku.states:
            assignments[state] = None
            unassignedList[state] = [1, 2, 3, 4]
        assignments[(1, 1)] = 3
        del unassignedList[(1, 1)]
        assert self.sudoku.assignments == assignments
        assert self.sudoku.unassigned.unassignedList == unassignedList
        assert self.sudoku.complete() is False
        assert self.sudoku.consistent() is True

        # --------------------
        # - 3 - -   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------

        # Unassign (1,1) from 3
        # Expect: assignment to change (1,1) entry becomes None and unassigned list with (1,1) entry
        self.sudoku.unassign((1, 1))
        assignments[(1, 1)] = None
        unassignedList[(1, 1)] = [1, 2, 3, 4]
        assert self.sudoku.assignments == assignments
        assert self.sudoku.unassigned.unassignedList == unassignedList

        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------

class TestConsistencySize2(unittest.TestCase):

    def setUp(self) -> None:
        self.sudoku = Sudoku(2, {})

    def test1(self):
        self.sudoku.assign((1, 1), 1)
        self.sudoku.assign((1, 2), 2)
        self.sudoku.assign((1, 3), 3)
        self.sudoku.assign((1, 4), 4)

        assignments = {}
        unassignedList = {}
        for state in self.sudoku.states:
            assignments[state] = None
            unassignedList[state] = [1, 2, 3, 4]
        assignments[(1, 1)] = 1
        assignments[(1, 2)] = 2
        assignments[(1, 3)] = 3
        assignments[(1, 4)] = 4
        del unassignedList[(1, 1)]
        del unassignedList[(1, 2)]
        del unassignedList[(1, 3)]
        del unassignedList[(1, 4)]

        assert self.sudoku.assignments == assignments
        assert self.sudoku.unassigned.unassignedList == unassignedList
        assert self.sudoku.consistent() is True

        # --------------------
        # - 1 -- 2 -- 3 -- 4 -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------

        self.sudoku.unassign((1, 4))
        assignments[(1, 4)] = None
        unassignedList[(1, 4)] = [1, 2, 3, 4]

        assert self.sudoku.assignments == assignments
        assert self.sudoku.unassigned.unassignedList == unassignedList
        assert self.sudoku.consistent() is True

        # --------------------
        # - 1 -- 2 -- 3 --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------

        self.sudoku.assign((1, 4), 3)
        assignments[(1, 4)] = 3
        del unassignedList[(1, 4)]

        assert self.sudoku.assignments == assignments
        assert self.sudoku.unassigned.unassignedList == unassignedList
        assert self.sudoku.consistent() is False

        # --------------------
        # - 1 -- 2 -- 3 -- 3 -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------

        self.sudoku.unassign((1, 4))
        self.sudoku.assign((2, 2), 2)

        assert self.sudoku.consistent() is False

        # --------------------
        # - 1 -- 2 -- 3 --   -
        # --------------------
        # -   -- 2 --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------
        # -   --   --   --   -
        # --------------------

class TestConsistencySize3(unittest.TestCase):

    def setUp(self) -> None:
        problem = {
            (1, 1): 5, (1, 7): 2, (1, 8): 8, (1, 9): 1,
            (2, 2): 8, (2, 6): 9, (2, 7): 7, (2, 8): 6,
            (3, 3): 9, (3, 6): 6, (3, 8): 4,
            (4, 2): 7, (4, 4): 6, (4, 7): 4, (4, 8): 2,
            (5, 5): 3, (5, 8): 1, (5, 9): 8,
            (6, 2): 6, (6, 5): 5, (6, 9): 7,
            (7, 2): 2, (7, 4): 8, (7, 7): 5, (7, 9): 6,
            (8, 1): 4, (8, 3): 5, (8, 6): 7, (8, 7): 1, (8, 9): 2,
            (9, 3): 3, (9, 4): 2, (9, 8): 7
        }
        self.sudoku = Sudoku(3, problem)

        # ---------------------------------------------
        # - 5 --   --   --   --   --   -- 2 -- 8 -- 1 -
        # ---------------------------------------------
        # -   -- 8 --   --   --   -- 9 -- 7 -- 6 --   -
        # ---------------------------------------------
        # -   --   -- 9 --   --   -- 6 --   -- 4 --   -
        # ---------------------------------------------
        # -   -- 7 --   -- 6 --   --   -- 4 -- 2 --   -
        # ---------------------------------------------
        # -   --   --   --   -- 3 --   --   -- 1 -- 8 -
        # ---------------------------------------------
        # -   -- 6 --   --   -- 5 --   --   --   -- 7 -
        # ---------------------------------------------
        # -   -- 2 --   -- 8 --   --   -- 5 --   -- 6 -
        # ---------------------------------------------
        # - 4 --   -- 5 --   --   -- 7 -- 1 --   -- 2 -
        # ---------------------------------------------
        # -   --   -- 3 -- 2 --   --   --   -- 7 --   -
        # ---------------------------------------------

    def test1(self):
        assert self.sudoku.consistent() is True

    def test2(self):
        self.sudoku.assign((1, 2), 4)
        assert self.sudoku.consistent() is True

    def test3(self):
        assert self.sudoku.unassigned.getDomain((1, 3)) == [4, 6, 7]
        assert self.sudoku.neighborValues((1, 3)) == [1, 2, 3, 5, 8, 9]
        self.sudoku.localFilter((1, 3))
        assert self.sudoku.unassigned.getDomain((1, 3)) == [4, 6, 7]

class TestFilter(unittest.TestCase):

    def setUp(self) -> None:
        self.sudoku = Sudoku(2, {(1, 1): 1, (1, 2): 2, (1, 3): 3, (1, 4): 4})

    def test1(self):
        assert self.sudoku.unassigned.unassignedList == {(2, 1): [3, 4], (2, 2): [3, 4], (2, 3): [1, 2], (2, 4): [1, 2], (3, 1): [2, 3, 4], (3, 2): [1, 3, 4], (3, 3): [1, 2, 4], (3, 4): [1, 2, 3], (4, 1): [2, 3, 4], (4, 2): [1, 3, 4], (4, 3): [1, 2, 4], (4, 4): [1, 2, 3]}

    def test2(self):
        self.sudoku.assign((2, 1), 3)
        self.sudoku.filter("Local", (2, 1))
        assert self.sudoku.unassigned.unassignedList == {(2, 2): [4], (2, 3): [1, 2], (2, 4): [1, 2], (3, 1): [2, 4], (3, 2): [1, 3, 4], (3, 3): [1, 2, 4], (3, 4): [1, 2, 3], (4, 1): [2, 4], (4, 2): [1, 3, 4], (4, 3): [1, 2, 4], (4, 4): [1, 2, 3]}
        assert self.sudoku.unassigned.peek("MVF") == (2, 2)
