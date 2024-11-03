# Sample data for GDP variations during recession and non-recession periods
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
gdp_recession = [15, 14.5, 14.2, 14.1, 14.3, 14.4, 14.6, 14.7]
gdp_non_recession = [16, 16.2, 16.4, 16.6, 16.8, 17, 17.2, 17.4]

# Create subplots
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Recession subplot
ax[0].plot(years, gdp_recession, marker='o', color='r')
ax[0].set_title('Recession Period')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('GDP')

# Non-recession subplot
ax[1].plot(years, gdp_non_recession, marker='o', color='g')
ax[1].set_title('Non-Recession Period')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('GDP')

# Show the plot
plt.suptitle('Subplots of GDP Variations During Recession and Non-Recession Periods', fontsize=16)
plt.tight_layout()
plt.show()
