import matplotlib.pyplot as plt
import numpy as np

# Sample data for non-recession periods (fictional data)
years = np.array([2011, 2012, 2013, 2014, 2015])
auto_sales = np.array([80000, 85000, 87000, 89000, 92000])
gdp_growth = np.array([2.1, 2.4, 2.7, 3.0, 2.9])
unemployment_rate = np.array([8.5, 7.9, 7.2, 6.8, 5.5])

# Plot 1: Auto Sales Outside of Recession
plt.figure(figsize=(8, 6))
plt.plot(years, auto_sales, marker='o', color='blue', label='Auto Sales')
plt.title("Automobile Sales Outside of Recession")
plt.xlabel("Year")
plt.ylabel("Sales Volume")
plt.grid(True)
plt.legend()
plt.savefig('/mnt/data/Auto_Sales_Yearly_Report.png')
plt.show()

# Plot 2: GDP Growth Outside of Recession
plt.figure(figsize=(8, 6))
plt.plot(years, gdp_growth, marker='s', color='green', label='GDP Growth (%)')
plt.title("GDP Growth Outside of Recession")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.grid(True)
plt.legend()
plt.savefig('/mnt/data/GDP_Growth_Yearly_Report.png')
plt.show()

# Plot 3: Unemployment Rate Outside of Recession
plt.figure(figsize=(8, 6))
plt.plot(years, unemployment_rate, marker='^', color='purple', label='Unemployment Rate')
plt.title("Unemployment Rate Outside of Recession")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.legend()
plt.savefig('/mnt/data/Unemployment_Rate_Yearly_Report.png')
plt.show()
