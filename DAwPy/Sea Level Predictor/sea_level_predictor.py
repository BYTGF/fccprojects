import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    x = df['year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, label='Original Data')

    # First line of best fit (all data)
    res = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = res.intercept + res.slope * x_pred
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line 1880-2013')

    # Second line of best fit (from year 2000)
    recent_df = df[df['year'] >= 2000]
    x_recent = recent_df['year']
    y_recent = recent_df['CSIRO Adjusted Sea Level']
    res_recent = linregress(x_recent, y_recent)
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, 'green', label='Best Fit Line 2000-2013')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()