import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
import seaborn as sns  # For a nice palette of colors

def plot_dissolved_oxygen_trends(water_quality_trends):
    fig, ax = plt.subplots(figsize=(15, 7))

    # Define a color palette
    palette = sns.color_palette('husl', n_colors=water_quality_trends['site_name_short'].nunique())

    # Plot the regression line for dissolved oxygen data for each lake
    for idx, (lake, color) in enumerate(zip(water_quality_trends['site_name_short'].unique(), palette)):
        # Select data for the current lake
        lake_data = water_quality_trends[water_quality_trends['site_name_short'] == lake].copy()

        # Convert dates to ordinal numbers for regression
        lake_data['date_ordinal'] = pd.to_datetime(lake_data['date']).apply(lambda x: x.toordinal())

        # Calculate the linear regression
        slope, intercept, r_value, p_value, std_err = linregress(lake_data['date_ordinal'], lake_data['do_mg'])

        # Create the regression line
        reg_line = slope * lake_data['date_ordinal'] + intercept

        # Plot the regression line with a unique color and label
        ax.plot(lake_data['date'], reg_line, label=lake, color=color, linewidth=2)

    # Title and labels for dissolved oxygen plot
    ax.set_title('Linear Regression of Dissolved Oxygen Trends in Gippsland Lakes Over Time', fontsize=16)
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Dissolved Oxygen (mg/L)', fontsize=14)

    # Legend
    ax.legend(title='Lakes', loc='upper left', bbox_to_anchor=(1, 1))

    # Formatting the date ticks
    plt.xticks(rotation=45)
    plt.tight_layout()

    return fig


def plot_salinity_trends(water_quality_trends):
    fig, ax = plt.subplots(figsize=(15, 7))

    # Define a color palette
    palette = sns.color_palette('husl', n_colors=water_quality_trends['site_name_short'].nunique())

    # Plot the regression line for dissolved oxygen data for each lake
    for idx, (lake, color) in enumerate(zip(water_quality_trends['site_name_short'].unique(), palette)):
        # Select data for the current lake
        lake_data = water_quality_trends[water_quality_trends['site_name_short'] == lake].copy()

        # Convert dates to ordinal numbers for regression and store them in the 'date_ordinal' column
        lake_data['date_ordinal'] = pd.to_datetime(lake_data['date']).apply(lambda x: x.toordinal())

        # Calculate the linear regression
        slope, intercept, r_value, p_value, std_err = linregress(lake_data['date_ordinal'], lake_data['sal'])

        # Create the regression line
        reg_line = slope * lake_data['date_ordinal'] + intercept

        # Plot the regression line with a unique color and label
        ax.plot(lake_data['date'], reg_line, label=lake, color=color, linewidth=2)

    # Title and labels for dissolved oxygen plot
    ax.set_title('Linear Regression of Salinity Trends in Gippsland Lakes Over Time (Excluding Lake Reeve East)', fontsize=16)
    ax.set_xlabel('Year', fontsize=14)
    ax.set_ylabel('Salinity (ppt)', fontsize=14)

    # Legend
    ax.legend(title='Lakes', loc='upper left', bbox_to_anchor=(1, 1))

    # Formatting the date ticks
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()