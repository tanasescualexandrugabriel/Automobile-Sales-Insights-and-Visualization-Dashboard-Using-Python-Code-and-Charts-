import matplotlib.pyplot as plt
import numpy as np

# Sample data for recession periods (fictional data)
years = np.array([2007, 2008, 2009, 2010])
auto_sales = np.array([76000, 69000, 62000, 70000])
gdp_growth = np.array([-2.5, -3.0, -2.0, 1.2])
unemployment_rate = np.array([4.6, 5.8, 9.3, 9.5])

# Plot 1: Auto Sales During Recession
plt.figure(figsize=(8, 6))
plt.plot(years, auto_sales, marker='o', color='blue', label='Auto Sales')
plt.title("Automobile Sales During Recession")
plt.xlabel("Year")
plt.ylabel("Sales Volume")
plt.grid(True)
plt.legend()
plt.savefig('/mnt/data/Auto_Sales_Recession_Report.png')
plt.show()

# Plot 2: GDP Growth During Recession
plt.figure(figsize=(8, 6))
plt.plot(years, gdp_growth, marker='s', color='orange', label='GDP Growth (%)')
plt.title("GDP Growth During Recession")
plt.xlabel("Year")
plt.ylabel("GDP Growth (%)")
plt.grid(True)
plt.legend()
plt.savefig('/mnt/data/GDP_Growth_Recession_Report.png')
plt.show()

# Plot 3: Unemployment Rate During Recession
plt.figure(figsize=(8, 6))
plt.plot(years, unemployment_rate, marker='^', color='red', label='Unemployment Rate')
plt.title("Unemployment Rate During Recession")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.legend()
plt.savefig('/mnt/data/Unemployment_Rate_Recession_Report.png')
plt.show()
