import unittest
from DFA import DFA
from TuringMachine import TuringMachine

class TestAutomata(unittest.TestCase):
    def setUp(self):
        self.dfa = DFA()
        self.tm = TuringMachine()
    
    def test_dfa_accepts(self):
        self.assertTrue(self.dfa.accepts("101"))
        self.assertTrue(self.dfa.accepts("0101"))
        self.assertTrue(self.dfa.accepts("1101011"))
        self.assertFalse(self.dfa.accepts("100"))
        self.assertFalse(self.dfa.accepts("010010"))
    
    def test_tm_divisible_by_3(self):
        self.assertTrue(self.tm.run("0"))
        self.assertTrue(self.tm.run("11"))
        self.assertTrue(self.tm.run("110"))
        self.assertFalse(self.tm.run("1"))
        self.assertFalse(self.tm.run("10"))
        self.assertFalse(self.tm.run("111"))

if __name__ == '__main__':
    unittest.main()