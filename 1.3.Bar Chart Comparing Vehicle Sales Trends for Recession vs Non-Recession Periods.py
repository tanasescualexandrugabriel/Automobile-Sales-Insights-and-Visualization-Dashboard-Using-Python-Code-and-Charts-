import seaborn as sns

# Sample data for vehicle sales trends during recession and non-recession periods
data = {
    'Vehicle_Type': ['SUV', 'Sedan', 'Truck'],
    'Recession': [900, 720, 400],
    'Non_Recession': [1000, 830, 600]
}

# Create DataFrame
df = pd.DataFrame(data)

# Melt the DataFrame to long format for seaborn
df_melted = pd.melt(df, id_vars='Vehicle_Type', var_name='Period', value_name='Sales')

# Create bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x='Vehicle_Type', y='Sales', hue='Period', data=df_melted)

# Add title and labels
plt.title('Bar Chart Comparing Vehicle Sales Trends for Recession vs Non-Recession Periods', fontsize=14)
plt.xlabel('Vehicle Type', fontsize=12)
plt.ylabel('Sales Volume', fontsize=12)

# Show the plot
plt.show()
