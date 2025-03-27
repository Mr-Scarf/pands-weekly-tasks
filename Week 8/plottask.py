# plottask.py 
# Write a program called plottask.py that displays:a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10,

#Author: David Scally

#Import libraries
import matplotlib.pyplot as plt
import numpy as np



# Step 1 - Write a program called plottask.py that displays:a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2

#Inputs from Instruction. Create dynamic variables, easier for code if inputs need to be updated.
Mean = 5
standard_deviation = 2
number_of_values = 1000

# np.random.normal shows a normal distribution in format (mean,standard deviation,size), also described as (loc, scale,size)
# Generate 1000 values. 
values = np.random.normal(Mean,standard_deviation,number_of_values)

# Plot histogram
# Add bins : size of histogram,  alpha: how translucent the plot , color: state the color, label: reprentation on the legend 
plt.hist(values,bins = 5, alpha = 0.8, color = 'green',label = 'Normal Distribution')

# Add title & position to left hand side
plt.title('Week 8 - Plot Task',loc = 'left')

# Name x & y axis
plt.xlabel('Value')
plt.ylabel('Count')

# Add gridlines + legend
plt.grid(True)


# Step 2 -  plot of the function  h(x)=x3 in the range 0 to 10,


# Map x & y points. xpoints = points in range between 0-10 inclusive , y = 'xpoints' cubed.
xpoints = np.array(range(0,11))
ypoints = (xpoints*xpoints*xpoints)

# Plot the x & y points, add 'o' marker , & lable name.
plt.plot(xpoints,ypoints,marker = 'o', label = 'h(x)=x3')

# Display Legend - shows labels
plt.legend()

# Show plot
plt.show()





# Reference: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# Reference https://campus.datacamp.com/courses/intermediate-python/matplotlib?ex=18
# Reference https://www.w3schools.com/python/matplotlib_labels.asp
# Reference https://www.w3schools.com/python/matplotlib_subplot.asp
# Reference https://www.w3schools.com/python/matplotlib_markers.asp



