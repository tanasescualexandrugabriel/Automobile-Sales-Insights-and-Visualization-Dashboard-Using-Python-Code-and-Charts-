# Sample data for average vehicle price and sales volume during recession
vehicle_prices = [15000, 20000, 25000, 30000, 35000, 40000, 45000]
sales_volume = [700, 650, 600, 500, 400, 300, 200]

# Create scatter plot
plt.scatter(vehicle_prices, sales_volume, color='green')

# Add title and labels
plt.title('Scatter Plot of Average Vehicle Price vs Sales Volume During Recession')
plt.xlabel('Average Vehicle Price ($)')
plt.ylabel('Sales Volume')

# Show the plot
plt.show()
