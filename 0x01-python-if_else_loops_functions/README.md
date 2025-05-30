# 0x01. Python - if/else, loops, functions

## Description
This project focuses on fundamental Python programming concepts including conditional statements, loops, and functions. It covers essential control flow structures and introduces basic function creation and usage in Python.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without external help:

### General
- Why Python programming is awesome
- Why indentation is so important in Python
- How to use the `if`, `if ... else` statements
- How to use comments
- How to assign values to variables
- How to use the `while` and `for` loops
- How Python's `for` loop differs from C's `for` loop
- How to use the `break` and `continue` statements
- How to use `else` clauses on loops
- What the `pass` statement does and when to use it
- How to use `range`
- What is a function and how to use functions
- What a function returns when it doesn't use any return statement
- Scope of variables
- What's a traceback
- What are the arithmetic operators and how to use them

## Requirements

### Python Scripts
- **Allowed editors**: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the pycodestyle (version 2.8.*)
- All files must be executable
- File length will be tested using `wc`

## Tasks

### 0. Positive anything is better than negative nothing
**File**: `0-positive_or_negative.py`
- Program assigns a random signed number to variable `number`
- Print whether the number is positive, negative, or zero
- **Output format**: 
  - `[number] is positive` (if > 0)
  - `[number] is zero` (if = 0)
  - `[number] is negative` (if < 0)

### 1. The last digit
**File**: `1-last_digit.py`
- Program assigns a random signed number to variable `number`
- Print the last digit of the number with appropriate message
- **Output format**: `Last digit of [number] is [last_digit] and is [condition]`

### 2. I sometimes suffer from insomnia...
**File**: `2-print_alphabet.py`
- Print ASCII alphabet in lowercase, not followed by a new line
- **Constraints**: One print function, one loop, no character storage, no imports

### 3. When I was having that alphabet soup...
**File**: `3-print_alphabt.py`
- Print ASCII alphabet in lowercase except 'q' and 'e'
- **Constraints**: One print function, one loop, no character storage, no imports

### 4. Hexadecimal printing
**File**: `4-print_hexa.py`
- Print numbers from 0 to 98 in decimal and hexadecimal
- **Format**: `[decimal] = 0x[hex]`
- **Constraints**: One print function, one loop, no variable storage, no imports

### 5. 00...99
**File**: `5-print_comb2.py`
- Print numbers from 0 to 99 with two digits, separated by ", "
- **Constraints**: Max 2 print functions, one loop, no variable storage, no imports

### 6. Inventing is a combination of brains and materials...
**File**: `6-print_comb3.py`
- Print all possible different combinations of two digits
- Numbers must be different, print only smallest combination
- **Constraints**: Max 3 print functions, max 2 loops, no variable storage, no imports

### 7. islower
**File**: `7-islower.py`
- Function that checks for lowercase character
- **Prototype**: `def islower(c):`
- **Returns**: True if lowercase, False otherwise
- **Hint**: Use `ord()`

### 8. To uppercase
**File**: `8-uppercase.py`
- Function that prints a string in uppercase
- **Prototype**: `def uppercase(str):`
- **Constraints**: Max 2 print functions, one loop, use `ord()`

### 9. There are only 3 colors, 10 digits, and 7 notes...
**File**: `9-print_last_digit.py`
- Function that prints the last digit of a number
- **Prototype**: `def print_last_digit(number):`
- **Returns**: Value of the last digit

### 10. a + b
**File**: `10-add.py`
- Function that adds two integers
- **Prototype**: `def add(a, b):`
- **Returns**: Value of a + b

### 11. a ^ b
**File**: `11-pow.py`
- Function that computes a to the power of b
- **Prototype**: `def pow(a, b):`
- **Returns**: Value of a ^ b

### 12. Fizz Buzz
**File**: `12-fizzbuzz.py`
- Function that prints numbers 1 to 100 with FizzBuzz logic
- **Prototype**: `def fizzbuzz():`
- Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both

## Advanced Tasks

### 14. Smile in the mirror
**File**: `100-print_tebahpla.py`
- Print ASCII alphabet in reverse, alternating lowercase and uppercase

### 15. Remove at position
**File**: `101-remove_char_at.py`
- Function that creates a copy of string, removing character at position n
- **Prototype**: `def remove_char_at(str, n):`

## Repository Information
- **GitHub repository**: alx-higher_level_programming
- **Directory**: 0x01-python-if_else_loops_functions

## Author
Ismail OUZAL

## Usage
To run any Python script:
```bash
./filename.py
```

## Notes
- Remember to make Python files executable: `chmod +x filename.py`
- Follow pycodestyle guidelines for Python code
- Test your functions thoroughly before submission
