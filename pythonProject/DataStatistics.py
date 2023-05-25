import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Sample data
x = np.arange(10)
y = np.array([2, 4, 5, 7, 8, 9, 10, 12, 14, 15])

# Calculate the slope and intercept of the regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Create the line plot
plt.plot(x, y, 'o', label='Data')
plt.plot(x, intercept + slope*x, 'r', label='Regression line')
plt.legend()

# Add labels and title
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Line chart of sample data')

# Display the plot
plt.show()