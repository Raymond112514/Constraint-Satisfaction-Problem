from abc import ABC, abstractmethod

class CSPConstraint(ABC):

    def __init__(self, assignments):
        self.assignments = assignments

    @abstractmethod
    def satisfied(self):
        pass
