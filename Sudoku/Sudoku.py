from CSP.CSP import CSP
from Sudoku.SudokuConstraint import rowConstraint, columnConstraint, blockConstraint

class Sudoku(CSP):

    def __init__(self, size, assignments):
        self.size = size
        domain = [_ for _ in range(1, self.size ** 2 + 1)]
        states = [(row, col) for row in range(1, self.size ** 2 + 1) for col in range(1, self.size ** 2 + 1)]
        super().__init__(domain, states, assignments)

        # Setting up constraint
        constraints = [rowConstraint(self.assignments, size),
                       columnConstraint(self.assignments, size),
                       blockConstraint(self.assignments, size)]
        self.addConstraint(constraints)

        # Initial global filter
        self.filter("Global")

    def neighbor(self, state):
        neighbors = set()

        # Get row neighbors
        for row in range(1, self.size ** 2 + 1):
            neighbors.add((row, state[1]))

        # Get column neighbors
        for col in range(1, self.size ** 2 + 1):
            neighbors.add((state[0], col))

        # Get block neighbors
        startX = (state[0] - 1) // self.size
        startY = (state[1] - 1) // self.size
        for row in range(startX * self.size + 1, (startX + 1) * self.size + 1):
            for col in range(startY * self.size + 1, (startY + 1) * self.size  + 1):
                neighbors.add((row, col))
        neighbors.remove(state)
        return neighbors

    def neighborValues(self, state):
        neighbors = self.neighbor(state)
        returnSet = set()
        for neighbor in neighbors:
            if self.assignments[neighbor] is not None:
                returnSet.add(self.assignments[neighbor])
        return list(returnSet)

    # ========================================================================================================
    # ========================================================================================================
    # ========================================================================================================

    def printAssignment(self):
        print("-----" * self.size ** 2)
        for row in range(1, self.size ** 2 + 1):
            row_string = ""
            for col in range(1, self.size ** 2 + 1):
                value = self.assignments[(row, col)]
                if value is not None:
                    row_string += "- " + str(value) + " -"
                else:
                    row_string += "- " + " " + " -"
            print(row_string)
            print("-----" * self.size ** 2)
