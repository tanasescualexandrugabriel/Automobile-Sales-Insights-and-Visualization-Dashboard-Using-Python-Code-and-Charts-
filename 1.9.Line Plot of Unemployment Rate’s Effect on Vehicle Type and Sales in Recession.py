# Sample data for unemployment rate and vehicle sales by type during recession
years = [2010, 2011, 2012, 2013, 2014]
unemployment_rate = [9.6, 9.0, 8.1, 7.4, 6.2]
sales_sedan = [100000, 95000, 90000, 85000, 80000]
sales_suv = [50000, 48000, 46000, 44000, 42000]

# Plotting
plt.figure(figsize=(8,6))

plt.plot(years, unemployment_rate, label='Unemployment Rate', color='red', linestyle='--')
plt.plot(years, sales_sedan, label='Sedan Sales', color='blue')
plt.plot(years, sales_suv, label='SUV Sales', color='green')

# Add title and labels
plt.title("Unemployment Rate's Effect on Vehicle Sales During Recession")
plt.xlabel('Years')
plt.ylabel('Rate / Sales')

# Add legend
plt.legend()

# Show the plot
plt.show()
