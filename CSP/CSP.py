from abc import ABC, abstractmethod
from CSP.CSPMap import CSPMap


class CSP(ABC):

    def __init__(self, domain, states, assignment: {}):
        # Initializing instance variables
        self.domain = domain
        self.states = states
        self.constraints = []
        self.assignments = {}
        self.numAssigned = 0

        # Setting up initial assignments
        for state in self.states:
            if state in assignment:
                self.assignments[state] = assignment[state]
                self.numAssigned += 1
            else:
                self.assignments[state] = None

        # Setting up unassigned CSPMap
        self.unassigned = CSPMap(self.domain, self.assignments)

    def addConstraint(self, constraint):
        self.constraints = constraint

    def complete(self):
        return self.numAssigned == len(self.states)

    def consistent(self):
        for constraint in self.constraints:
            if not constraint.satisfied():
                return False
        return True

    def neighbor(self, state):
        return []

    def neighborValues(self, state):
        return []

    def assign(self, state, value):
        # Assign first adds (state, value) to current assignment, then remove state from unassigned
        assert state in self.assignments, "State not in state space!"
        assert value in self.domain, "Value not in domain!"
        self.numAssigned += 1
        self.assignments[state] = value
        return self.unassigned.remove(state)

    def unassign(self, state):
        # Unassign first remove (state, value) from current assignment, then add state to unassigned
        assert state in self.assignments, "State not in state space!"
        self.numAssigned -= 1
        self.assignments[state] = None
        self.unassigned.add(state)

    def nextState(self, command):
        return self.unassigned.peek(command)

    def backtrack(self):
        if self.complete():
            return self.assignments

        # Does not remove state from unassigned!
        state = self.nextState("Simple")
        for value in self.unassigned.getDomain(state):
            self.assign(state, value)
            if self.consistent():
                output = self.backtrack()
                if output is not None:
                    return output
            self.unassign(state)
        return None

    def backtrackFilter(self):
        if self.complete():
            return self.assignments

        # Does not remove state from unassigned!
        state = self.nextState("Simple")
        for value in self.unassigned.getDomain(state):
            self.assign(state, value)
            self.filter("Local", state)
            if self.consistent():
                output = self.backtrackFilter()
                if output is not None:
                    return output
            self.unassign(state)
            self.filter("Local", state)
        return None

    def backtrackFilterMVF(self):
        if self.complete():
            return self.assignments

        # Does not remove state from unassigned!
        state = self.nextState("MVF")
        for value in self.unassigned.getDomain(state):
            self.assign(state, value)
            self.filter("Local", state)
            if self.consistent():
                output = self.backtrackFilterMVF()
                if output is not None:
                    return output
            self.unassign(state)
            self.filter("Local", state)
        return None

    def filter(self, command, state=None):
        if command == "Local":
            for neighbor in self.neighbor(state):
                if self.assignments[neighbor] is None:
                    self.localFilter(neighbor)
        if command == "Global":
            for state in self.getUnassignedList():
                self.localFilter(state)

    def localFilter(self, state):
        domain = set(self.domain).difference(set(self.neighborValues(state)))
        domain = list(domain)
        self.unassigned.set(state, domain)

    # ========================================================================================================
    # ========================================================================================================
    # ========================================================================================================

    def getUnassignedList(self):
        return self.unassigned.unassignedList

    def printAssignment(self):
        pass