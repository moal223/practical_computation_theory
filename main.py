from DFA import DFA
from TuringMachine import TuringMachine

def main():
    print("Automata Programs")
    print("1. DFA - Check for substring '101'")
    print("2. Turing Machine - Check if binary number is divisible by 3")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        dfa = DFA()
        input_str = input("Enter a binary string to check for '101' substring: ")
        result = dfa.accepts(input_str)
        print(f"Result: The string {'contains' if result else 'does not contain'} '101'")
    elif choice == '2':
        tm = TuringMachine()
        input_str = input("Enter a binary number to check divisibility by 3: ")
        result = tm.run(input_str)
        print(f"Result: The number {'is' if result else 'is not'} divisible by 3")
    else:
        print("Invalid choice")

if __name__ == '__main__':
    main()