
class CSPMap:

    def __init__(self, domain, assignments):
        self.domain = domain
        self.unassignedList = {}

        for state in assignments:
            if assignments[state] is None:
                self.unassignedList[state] = list(self.domain)

    def remove(self, state):
        return self.unassignedList.pop(state)

    def add(self, state):
        if state in self.unassignedList:
            print(state)
        assert state not in self.unassignedList, "State already exists in the unassigned list!"
        self.unassignedList[state] = list(self.domain)

    def set(self, state, domain):
        self.unassignedList[state] = domain

    def peek(self, command):
        # Returns the next unassigned state (does not remove it from the list)
        if command == "Simple":
            return list(self.unassignedList)[0]
        if command == "MVF":
            minVal, minState = float("inf"), None
            for state in self.unassignedList:
                if len(self.getDomain(state)) == 0:
                    return state
                if len(self.getDomain(state)) < minVal:
                    minVal, minState = len(self.getDomain(state)), state
            return minState
        return None

    def getDomain(self, state):
        assert state in self.unassignedList, "State not in the unassigned list!"
        return self.unassignedList[state]