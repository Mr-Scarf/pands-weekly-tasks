# plottask.py 
# Write a program called plottask.py that displays:a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10,

#Author: David Scally

#Import libraries
import matplotlib.pyplot as plt
import numpy as np

#Inputs from Instruction
Mean = 5
standard_deviation = 2
number_of_values = 1000

# Generate 1000 values
values = np.random.normal(Mean,standard_deviation,number_of_values)

# Plot histogram
plt.hist(values,bins = 20, alpha = 0.8, color = 'green',label = 'Normal Distribution')

# Add title + name x& y axis
plt.title('Week 8 - Plot Task')
plt.xlabel('Value')
plt.ylabel('Count')

# Add gridlines + legend
plt.grid(True)
plt.legend()

# Show Data
plt.show()

# plot of the function  h(x)=x3 in the range 0 to 10,





# Reference: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# Reference https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=18



#min_salary = 20000
#max_salary = 80000
#number_of_entries = 10

#np.random.seed(1) # this makes the random numbers are the same each time to make it eas

#salaries = np.random.randint(min_salary,max_salary,number_of_entries)
#ages = np.random.randint(21,65,number_of_entries)  # format is (low,high,iterations)

#print(salaries)  for #1

#6 

#plt.hist(salaries)
#plt.show()

#7
#plt.scatter(ages,salaries)
#plt.title('Scatter Graph - Ages & Wages')
#plt.xlabel('Ages')
#plt.ylabel('Wages')


#8 Add x squared
#xpoints = np.array(range(1,101))
#ypoints = xpoints * xpoints
#plt.plot(xpoints, ypoints, color = 'pink',label = 'x squared')
#plt.legend()
#plt.show()
#plt.savefig('prettier-plot.png')

