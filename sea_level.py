import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

