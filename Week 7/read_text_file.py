# read_text_file.py

#Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.
#The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
#Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.


# Author: David Scally

import sys          # Import sys Module . The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
                    # This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. 

print(sys.argv) 

                  
#with open ()
#f = open("demofile.txt")
#print(f.read()) # By default the read() method returns the whole text, but you can also specify how many characters you want to return:
#f.close() # It is a good practice to always close the file when you are done with it.In some cases, due to buffering, changes made to a file may not show until you close the file.
#Avoid Error - 
#
#Lecture 7.1


# Functions that can be used with sys.argv

len()- function is used to count the number of arguments passed to the command line. Since the iteration starts with 0, it also counts the name of the program as one argument. If one just wants to deal with other inputs they can use (len(sys.argv)-1).
str()- this function is used to present the array as a string array. Makes displaying the command line array easier and better.


# Souce: https://www.w3schools.com/python/python_file_handling.asp
# Source: https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/
# Source: https://stackoverflow.com/questions/4117530/what-does-sys-argv1-mean-what-is-sys-argv-and-where-does-it-come-from
# Source: https://www.youtube.com/watch?v=rJCl7t3IIbA