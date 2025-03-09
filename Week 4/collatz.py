# collatz.py

# Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Author: David Scally


number = int(input('Please enter a positive integer: '))

while (number != 1):
    print(number)
    if number % 2 == 0: #Check if even number,  no remainder
        number = number // 2 # Divide even number by 2
    else:
        number = number * 3 + 1 # if not even number , multiply by 3 & add 1

print(1)

 