# Sample data for advertising expenditure during recession vs non-recession
labels = ['Recession', 'Non-Recession']
ad_expenditure = [300000, 700000]
colors = ['lightcoral', 'lightblue']

# Create pie chart
plt.pie(ad_expenditure, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Add title
plt.title('Pie Chart of XYZAutomotives Advertising Expenditure in Recession vs Non-Recession')

# Show the plot
plt.show()
