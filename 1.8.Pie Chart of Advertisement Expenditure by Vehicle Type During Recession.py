# Sample data for advertising expenditure by vehicle type during recession
labels = ['Sedan', 'SUV', 'Truck', 'Electric']
ad_expenditure_by_type = [200000, 250000, 150000, 100000]
colors = ['lightgreen', 'lightblue', 'lightcoral', 'gold']

# Create pie chart
plt.figure(figsize=(6,6))
plt.pie(ad_expenditure_by_type, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Ensure the pie is drawn as a circle.
plt.axis('equal')

# Add title
plt.title('Pie Chart of Advertisement Expenditure by Vehicle Type During Recession')

# Show the plot
plt.show()
