class TuringMachine:
    def __init__(self):
        self.transitions = {
            'q0': {'0': ('q0', '0', 'R'), '1': ('q1', '1', 'R'), '_': ('accept', '_', 'R')},
            'q1': {'0': ('q2', '0', 'R'), '1': ('q0', '1', 'R'), '_': ('reject', '_', 'R')},
            'q2': {'0': ('q1', '0', 'R'), '1': ('q2', '1', 'R'), '_': ('reject', '_', 'R')},
            'accept': {},
            'reject': {}
        }
        self.current_state = 'q0'
        self.tape = []
        self.head_position = 0
    
    def run(self, input_string):
        self.tape = list(input_string) + ['_']
        self.head_position = 0
        self.current_state = 'q0'
        
        while self.current_state not in {'accept', 'reject'}:
            current_symbol = self.tape[self.head_position]
            if current_symbol not in self.transitions[self.current_state]:
                self.current_state = 'reject'
                break
                
            new_state, write_symbol, move = self.transitions[self.current_state][current_symbol]
            self.tape[self.head_position] = write_symbol
            self.current_state = new_state
            self.head_position += 1 if move == 'R' else -1
        
        return self.current_state == 'accept'