 # bank.py
# Prompt the user and read in two money amounts (in cent)
# cont. Add the two amounts
# cont. Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author: David Scally

# Prompt User for two money amounts
# Int type used to allow for amount in cents only. Float type would be used if decimal places allowed.
# input is standard format where question is asked by code for user to return reply.

amount1 = int(input("Enter first amount in cents : "))
amount2 = int(input("Enter second amount in cents : "))

# Add two amounts returned by user.
total_amount = amount1 + amount2

# Convert total_amount in cents to Euro, required for final answer.
answer = total_amount/100

# f-string used as combining integer (Answer variable) & string(€) .
# Round fucntion used to display answer to two decimal places. Same as Microsoft excel function. 
print(f'€{round(answer,2)}')

# Sources:
# f-string source : https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

#Review
# Rounds whole number down to 1 decimal place. https://www.w3schools.com/python/python_string_formatting.asp