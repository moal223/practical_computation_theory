محمد العوضى احمد العوضى
section: 5
4537

terminal example:
Automata Programs 1. DFA - Check for substring '101' 2. Turing Machine - Check if binary number is divisible by 3
Enter your choice (1 or 2): 2
Enter a binary number to check divisibility by 3: 0101
Result: The number is not divisible by 3
PS E:\Collage\4th\second\computation theory\practical>

Code Explanation:
DFA Class:

        Implements a Deterministic Finite Automaton that checks if a binary string contains the     substring   "101"

        States represent progress in matching the pattern (0=no progress, 3=full match)

        Transitions define how the DFA moves between states based on input

    TuringMachine Class:

        Implements a Turing Machine that checks if a binary number is divisible by 3

        Uses states q0, q1, q2 to represent remainders 0, 1, 2 respectively

        Transitions update the remainder state based on each bit read

        Accepts if final state is q0 (remainder 0)
