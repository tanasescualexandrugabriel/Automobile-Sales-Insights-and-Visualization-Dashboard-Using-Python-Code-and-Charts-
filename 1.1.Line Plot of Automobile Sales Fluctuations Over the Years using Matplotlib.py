import matplotlib.pyplot as plt
import pandas as pd

# Sample data for automobile sales over the years
data = {'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
        'Sales': [1500, 1800, 1700, 2000, 2100, 2300, 2500, 2400]}

# Create DataFrame
df = pd.DataFrame(data)

# Create a line plot
plt.figure(figsize=(8, 6))
plt.plot(df['Year'], df['Sales'], marker='o', linestyle='-', color='b')

# Add title and labels
plt.title('Line Plot of Automobile Sales Fluctuations Over the Years', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales Volume', fontsize=12)
plt.grid(True)

# Show the plot
plt.show()