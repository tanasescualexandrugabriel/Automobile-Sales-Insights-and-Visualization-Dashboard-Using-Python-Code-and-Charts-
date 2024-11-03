# Sample data for automobile sales with seasonality impact
seasons = ['Winter', 'Spring', 'Summer', 'Fall']
sales = [500, 800, 950, 700]
bubble_size = [300, 500, 800, 400]

plt.scatter(seasons, sales, s=bubble_size, alpha=0.5, color='blue')
plt.title('Bubble Plot Showing Seasonality Impact on Automobile Sales')
plt.xlabel('Seasons')
plt.ylabel('Sales Volume')
plt.show()
