
#   Create an array containing 250 random floats between 0 and 5:
import matplotlib.pyplot as plt
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)
print(x)
plt.hist(x, 5)
plt.show()

#   We use the array from the example above to draw a histogram with 5 bars.
#   The first bar represents how many values in the array are between 0 and 1.
#   The second bar represents how many values are between 1 and 2.
#   Which gives us this result:
#   52 values are between 0 and 1
#   48 values are between 1 and 2
#   49 values are between 2 and 3
#   51 values are between 3 and 4
#   50 values are between 4 and 5

y = numpy.random.uniform(0.0, 5.0, 100000)
print (y)
plt.hist(y, 100)
plt.show()

