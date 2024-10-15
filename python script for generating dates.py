import random
import pandas as pd

# Define the date range
start_date = pd.to_datetime('2018-01-01')
end_date = pd.to_datetime('2024-09-01')

# Generate 1000 random dates
random_dates = pd.to_datetime(pd.Series(random.randint(start_date.value, end_date.value) for _ in range(8600)))

# Format the dates
formatted_dates = random_dates.dt.strftime('%d-%b-%Y')

# Print the dates
for date in formatted_dates:
    print(date)
