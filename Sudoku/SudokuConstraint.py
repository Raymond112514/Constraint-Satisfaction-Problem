from CSP.CSPConstraint import CSPConstraint

class rowConstraint(CSPConstraint):

    def __init__(self, assignments, size):
        super().__init__(assignments)
        self.size = size

    def satisfied(self):
        for row in range(1, self.size**2 + 1):
            storer = set()
            for col in range(1, self.size**2 + 1):
                if self.assignments[(row, col)] is not None:
                    if self.assignments[(row, col)] in storer:
                        return False
                    storer.add(self.assignments[(row, col)])
        return True


class columnConstraint(CSPConstraint):

    def __init__(self, assignments, size):
        super().__init__(assignments)
        self.size = size

    def satisfied(self):
        for col in range(1, self.size ** 2 + 1):
            storer = set()
            for row in range(1, self.size ** 2 + 1):
                if self.assignments[(row, col)] is not None:
                    if self.assignments[(row, col)] in storer:
                        return False
                    storer.add(self.assignments[(row, col)])
        return True

class blockConstraint(CSPConstraint):

    def __init__(self, assignments, size):
        super().__init__(assignments)
        self.size = size

    def satisfied(self):
        def check_block(start_x, start_y, size):
            storer = set()
            for row in range(start_x, start_x + size):
                for col in range(start_y, start_y + size):
                    if self.assignments[(row, col)] is not None:
                        if self.assignments[(row, col)] in storer:
                            return False
                        storer.add(self.assignments[(row, col)])
            return True
        for i in range(self.size):
            for j in range(self.size):
                start_row, start_col = 1 + self.size * i, 1 + self.size * j
                if not check_block(start_row, start_col, self.size):
                    return False
        return True