from Sudoku.Sudoku import Sudoku

# Backtrack only: >5 min
# Backtrack + filter: >5 min
# Backtrack + filter: <1 sec

problem = {
            (1, 5): 8, (1, 6): 3, (1, 8): 9,
            (2, 1): 6, (2, 3): 7, (2, 7): 3,
            (3, 1): 9, (3, 2): 1,
            (4, 2): 7, (4, 4): 1, (4, 8): 8, (4, 9): 5,
            (5, 4): 5, (5, 5): 9,
            (6, 3): 8, (6, 4): 7,
            (7, 2): 4, (7, 5): 7, (7, 6): 1,
            (8, 3): 6, (8, 8): 5,
            (9, 1): 8, (9, 9): 3
          }

sudoku = Sudoku(3, problem)
sudoku.printAssignment()
result = sudoku.backtrackFilterMVF()
sudoku.printAssignment() if result is not None else print(result)

# Problem
# ---------------------------------------------
# -   -- 3 --   -- 6 --   --   --   -- 8 --   -
# ---------------------------------------------
# -   --   -- 9 -- 8 --   -- 1 -- 7 --   -- 2 -
# ---------------------------------------------
# -   --   --   -- 5 --   --   --   --   -- 6 -
# ---------------------------------------------
# -   --   --   --   -- 1 --   --   --   -- 3 -
# ---------------------------------------------
# -   -- 8 -- 5 --   --   --   -- 9 --   -- 4 -
# ---------------------------------------------
# -   -- 7 --   --   -- 2 --   --   --   --   -
# ---------------------------------------------
# -   -- 9 --   --   --   -- 7 --   --   --   -
# ---------------------------------------------
# -   -- 5 -- 3 --   --   --   --   --   --   -
# ---------------------------------------------
# -   --   --   --   -- 9 --   --   -- 4 -- 7 -
# ---------------------------------------------

# Solution
# ---------------------------------------------
# - 5 -- 3 -- 1 -- 6 -- 7 -- 2 -- 4 -- 8 -- 9 -
# ---------------------------------------------
# - 6 -- 4 -- 9 -- 8 -- 3 -- 1 -- 7 -- 5 -- 2 -
# ---------------------------------------------
# - 8 -- 2 -- 7 -- 5 -- 4 -- 9 -- 3 -- 1 -- 6 -
# ---------------------------------------------
# - 9 -- 6 -- 2 -- 4 -- 1 -- 5 -- 8 -- 7 -- 3 -
# ---------------------------------------------
# - 1 -- 8 -- 5 -- 7 -- 6 -- 3 -- 9 -- 2 -- 4 -
# ---------------------------------------------
# - 3 -- 7 -- 4 -- 9 -- 2 -- 8 -- 1 -- 6 -- 5 -
# ---------------------------------------------
# - 4 -- 9 -- 6 -- 1 -- 5 -- 7 -- 2 -- 3 -- 8 -
# ---------------------------------------------
# - 7 -- 5 -- 3 -- 2 -- 8 -- 4 -- 6 -- 9 -- 1 -
# ---------------------------------------------
# - 2 -- 1 -- 8 -- 3 -- 9 -- 6 -- 5 -- 4 -- 7 -
# ---------------------------------------------