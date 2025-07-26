import xarray as xr
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime

# Load the NetCDF rainfall data
file_path = 'probability_statistics/Rainfall_estimation/imdlib_rain_2025-03-25_to_2025-07-22_polygon.nc'
ds = xr.open_dataset(file_path)

# Extract rainfall and time
rainfall = ds['rain'].values  # shape: (time, lat, lon)
time = ds['time'].values      # time array

# Convert to datetime and average over area
dates = pd.to_datetime(time)
rainfall_avg = rainfall.mean(axis=(1, 2))  # average over lat/lon

# Create a DataFrame
df = pd.DataFrame({'date': dates, 'rainfall': rainfall_avg})
df['day_number'] = (df['date'] - df['date'].min()).dt.days

# Train linear regression model
X = df[['day_number']]
y = df['rainfall']
model = LinearRegression()
model.fit(X, y)

# Function to predict rainfall and probability
def predict_rainfall_probability(future_date_str):
    future_date = pd.to_datetime(future_date_str)
    day_num = (future_date - df['date'].min()).days
    predicted_rainfall = model.predict([[day_num]])[0]

    # Estimate probability based on past data
    rainy_days = (df['rainfall'] >= predicted_rainfall).sum()
    total_days = len(df)
    probability = (rainy_days / total_days) * 100

    print(f"📅 Date: {future_date_str}")
    print(f"🌧 Predicted Rainfall: {predicted_rainfall:.2f} mm")
    print(f"🔢 Estimated Probability of Rain: {probability:.2f}%")

# Example usage
date_input = input("Enter a future date (YYYY-MM-DD): ")
predict_rainfall_probability(date_input)