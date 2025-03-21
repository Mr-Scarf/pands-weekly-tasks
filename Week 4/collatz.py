# collatz.py

# Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

# Author: David Scally


number = int(input('Please enter a positive integer: ')) #Prompts user to input positive integer.

while number <= 0: # Condition to run when user input number is 0 or less. Prompts user to re-enter a positive integer.
    number = int(input('Not a positive integer - please enter a positive integer: '))

while (number != 1): # Condition to run when user input number is not 1
    print(number) # Initial input number will be printed + additional numbers that follow the if & else condition.
    if number % 2 == 0: #Checks if even number,  no remainder after division
        number = number // 2 # Divides even number by 2
    else: # Will be odd number if not divisable by 2
        number = number * 3 + 1 # if not even number the else condition will run , multiply by 3 & add 1

print(number) #While loop ends when the condition is True that number == 1


#Source : https://www.w3schools.com/python/python_conditions.asp
#Source : https://www.youtube.com/watch?v=ysED_5pY_ZY
# Review - Need to add code to ensure a string can't be input

 