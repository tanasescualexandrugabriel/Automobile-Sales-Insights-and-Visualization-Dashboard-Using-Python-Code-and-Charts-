import matplotlib.pyplot as plt

# Sample data for sales of different vehicle types during recession
data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
    'SUV': [800, 850, 780, 900, 950, 980, 1000, 1100],
    'Sedan': [600, 680, 670, 720, 750, 800, 820, 830],
    'Truck': [300, 350, 320, 400, 450, 500, 550, 600]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create line plots for each vehicle type
plt.figure(figsize=(8, 6))
plt.plot(df['Year'], df['SUV'], marker='o', linestyle='-', label='SUV')
plt.plot(df['Year'], df['Sedan'], marker='o', linestyle='-', label='Sedan')
plt.plot(df['Year'], df['Truck'], marker='o', linestyle='-', label='Truck')

# Add title and labels
plt.title('Line Plot of Sales Trends for Different Vehicle Types During Recession Periods', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sales Volume', fontsize=12)
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
