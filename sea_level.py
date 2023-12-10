import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create first line of best fit
res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_pred = pd.Series([i for i in range(1880, 2051)])
y_pred = res.intercept + res.slope * x_pred
plt.plot(x_pred, y_pred, 'r')

# Create second line of best fit from 2000
new_df = df[df['Year'] >= 2000]
res_new = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
x_pred_new = pd.Series([i for i in range(2000, 2051)])
y_pred_new = res_new.intercept + res_new.slope * x_pred_new
plt.plot(x_pred_new, y_pred_new, 'green')

