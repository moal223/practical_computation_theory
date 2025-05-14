import unittest

from DFA import DFA
from TuringMachine import TuringMachine

class TestAutomataProblems(unittest.TestCase):
    def test_dfa_substring_101(self):
        dfa = DFA()
        self.assertTrue(dfa.accepts("101"))
        self.assertTrue(dfa.accepts("0101"))
        self.assertTrue(dfa.accepts("1010"))
        self.assertTrue(dfa.accepts("1101011"))
        self.assertFalse(dfa.accepts(""))
        self.assertFalse(dfa.accepts("100"))
        self.assertFalse(dfa.accepts("010010"))
        self.assertFalse(dfa.accepts("11"))
    
    def test_tm_divisible_by_3(self):
        tm = TuringMachine()
        self.assertTrue(tm.run("0"))     
        self.assertTrue(tm.run("11"))    
        self.assertTrue(tm.run("110"))   
        self.assertTrue(tm.run("1001"))  
        self.assertFalse(tm.run("1"))    
        self.assertFalse(tm.run("10"))   
        self.assertFalse(tm.run("101"))  
        self.assertFalse(tm.run("111"))  
    

if __name__ == '__main__':
    unittest.main()