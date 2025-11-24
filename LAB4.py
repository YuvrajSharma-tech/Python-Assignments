import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Create output folder if not exists
os.makedirs("output", exist_ok=True)

# -------------------------------
# TASK 1: DATA LOADING
# -------------------------------
df = pd.read_csv("weather_data.csv")   # change file name if needed

print("\n--- HEAD ---")
print(df.head())

print("\n--- INFO ---")
print(df.info())

print("\n--- DESCRIBE ---")
print(df.describe())

# -------------------------------
# TASK 2: CLEANING + PROCESSING
# -------------------------------

df = df.dropna()   # Or df.fillna(method='ffill')

df['Date'] = pd.to_datetime(df['Date'])

df = df[['Date', 'Temperature', 'Rainfall', 'Humidity']]

# -------------------------------
# TASK 3: STATISTICS USING NUMPY
# -------------------------------

daily_mean = np.mean(df['Temperature'])
daily_min = np.min(df['Temperature'])
daily_max = np.max(df['Temperature'])
daily_std = np.std(df['Temperature'])

df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

monthly_stats = df.groupby('Month')['Temperature'].agg(['mean', 'min', 'max', 'std'])
yearly_stats  = df.groupby('Year')['Temperature'].agg(['mean', 'min', 'max', 'std'])

print("\n--- Monthly Stats ---")
print(monthly_stats)

print("\n--- Yearly Stats ---")
print(yearly_stats)

# -------------------------------
# TASK 4: VISUALIZATIONS
# -------------------------------

# 1. Line Chart – Daily Temperature
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Temperature'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("output/daily_temperature.png")
plt.close()

# 2. Bar Chart – Monthly Rainfall
monthly_rainfall = df.groupby('Month')['Rainfall'].sum()

plt.figure(figsize=(10,5))
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("output/monthly_rainfall.png")
plt.close()

# 3. Scatter – Humidity vs Temperature
plt.figure(figsize=(7,5))
plt.scatter(df['Temperature'], df['Humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("output/humidity_vs_temperature.png")
plt.close()

# 4. Combined plot
fig, ax = plt.subplots(2, 1, figsize=(10,10))

ax[0].plot(df['Date'], df['Temperature'])
ax[0].set_title("Daily Temperature Trend")

ax[1].bar(monthly_rainfall.index, monthly_rainfall.values)
ax[1].set_title("Monthly Rainfall")

plt.tight_layout()
plt.savefig("output/combined_plots.png")
plt.close()

# -------------------------------
# TASK 5: GROUP & AGGREGATION
# -------------------------------

def get_season(month):
    if month in [12,1,2]: return "Winter"
    if month in [3,4,5]: return "Summer"
    if month in [6,7,8]: return "Monsoon"
    return "Autumn"

df['Season'] = df['Month'].apply(get_season)

seasonal_agg = df.groupby('Season').agg({
    'Temperature':'mean',
    'Rainfall':'sum',
    'Humidity':'mean'
})

print("\n--- Seasonal Aggregation ---")
print(seasonal_agg)

# -------------------------------
# TASK 6: EXPORT CLEANED FILE
# -------------------------------

df.to_csv("output/cleaned_weather_data.csv", index=False)

print("\nAll plots and cleaned CSV saved in /output folder 👌")