#!/usr/bin/python3
import calculator_1 as cal
from sys import argv
if __name__ == "__main__":
    lent = int(len(argv) - 1)
    if lent > 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>") 
            exit("1")
    else:
        for i in range(1, lent + 1):
            a = int(argv[1])
            b = int(argv[3])
            if argv[2] == "+":
                result = cal.add(a, b)
            elif argv[2] == "-":
                result = cal.sub(a, b)
            elif argv[2] == "*":
                result = cal.mul(a, b)
            elif argv[2] == "/":
                result = cal.div(a, b)
            else:
                print("Unknown operator. Available operators: +, -, * and /") 
                exit("1") 
            
    print(result)
