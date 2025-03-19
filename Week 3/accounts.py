# accounts.py
# Write a python program called accounts.py that reads in a 10 character account number and outputs the account number
# with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: David Scally



# Asking user input for 10 digit a/c number
account_number = (input("Please enter a 10 digit account number: "))

# Six 'x' to represent the 6 blocked numbers
blocked_number = 'xxxxxx'

print(f'Account number is:  {blocked_number}{account_number[-4:]}') # f-string to combine blocked number & last 4 numbers, slice function used to start count 4 digits from the end of the inout number.

#Source: 
# https://realpython.com/python-f-strings/
# https://www.w3schools.com/python/ref_func_slice.asp

#Review
#Currently, is no limit on how many digits a user can enter, needs to be limited to 10. Review subsequent lectures for revision on while,if,else functions.
# Also needs to be integer input only