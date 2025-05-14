class DFA:
    def __init__(self):
        self.transitions = {
            0: {'0': 0, '1': 1},
            1: {'0': 2, '1': 1},
            2: {'0': 0, '1': 3},
            3: {'0': 3, '1': 3}  
        }
        self.accept_state = 3
    
    def accepts(self, input_string):
        current_state = 0
        for char in input_string:
            if char not in {'0', '1'}:
                return False
            current_state = self.transitions[current_state][char]
        return current_state == self.accept_state