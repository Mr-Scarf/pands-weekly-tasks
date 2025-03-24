# squareroot.py

#Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
#This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).
#I suggest that you look at the newton method at estimating square roots.


# Author: David Scally


def sqrt(x): #Function that is called. x = User input - 'Selection' variable.

    guess = x/2   # User selection divided by 2 for ths first guess in Newton Method calculation
    while (guess * guess -x) > .00000001 : # While loop continues to run until final 'guess' is within the tolerance level(.00000001). This leads to more accurate result.
        guess = (guess + x /guess) / 2 # Newton Method calculation

    return round(guess,5) # Input to return 'guess' from function when called. Rounded to 5 decimal places.



# User input
selection = float(input('Please enter a positive number: '))

answer = sqrt(selection)
print(f'The square root of {selection} is approx. {answer}')
      

  # Source https://www.youtube.com/watch?v=99ABkygm2Xg&t=273s 
  # Source https://www.geeksforgeeks.org/square-root-of-a-number-without-using-sqrt-function/
  # Source https://chortle.ccsu.edu/java5/Notes/chap73/ch73_18.html  