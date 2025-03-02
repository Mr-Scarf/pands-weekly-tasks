# accounts.py
# Write a python program called accounts.py that reads in a 10 character account number and outputs the account number
# with only the last 4 digits showing (and the first 6 digits replaced with Xs).
# Author: David Scally


#Currently, is no limit on how many digits a user can enter, needs to be limited to 10.
#Source : https://www.w3schools.com/python/ref_func_slice.asp
#Source : https://realpython.com/python-f-strings/

account_number = (input("Please enter a 10 digit account number: "))
# Six 'x' to represent the 6 blocked numbers
blocked_number = 'xxxxxx'
print( blocked_number + account_number[-4:])
