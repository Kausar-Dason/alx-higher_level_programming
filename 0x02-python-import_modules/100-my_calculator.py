#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    num = len(sys.argv) - 1

    if (num == 3):
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif operator == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
