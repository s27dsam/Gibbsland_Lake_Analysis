import streamlit as st
import pandas as pd
from plots import plot_dissolved_oxygen_trends, plot_salinity_trends

st.set_page_config(page_title="Gibbsland Lakes Analysis", page_icon="🧮", layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            <h2 style='text-align: center;'Gibbsland Lakes Analysis</h2>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.title('Gibbsland Lakes Analysis')

tab1, tab2, tab3 = st.tabs(["Metrics", 'Plots','References'])

tab3.subheader('EPA Gippsland Lakes Water Quality Data 1990 - 2023')
tab3.write('Water quality data collected from EPA Victoria Marine Fixed Site Network within the Gippsland Lakes. Contains '
           'water sample data on a range of nutrients and physical parameters, pertaining to water quality. Data collected monthly, '
           'where possible, at known fixed locations (sites) in surface water')
tab3.write('https://discover.data.vic.gov.au/dataset/gippsland-lakes-water-quality-data-1990-2023')


tab1.write('Percentage of the Salinity in Gippsland Lakes Over the last 30 years')
col1, col2, col3, col4, col5 = tab1.columns(5)
col1.metric("Lake King North", "26.76", "11.27%")
col2.metric("Lake King North", "27.63", "4.23%")
col3.metric("Lake Victoria", "20.72", "16.20%")
col4.metric("Lake Wellington", "7.56", "21.95%")
col5.metric("Shaving Point", "27.87", "5.02%")


tab1.write('Percentage of Dissolved Oxygen in Gippsland Lakes Over the last 30 years')
col1, col2, col3, col4, col5 = tab1.columns(5)
col1.metric("Lake King North", "9.64", "27.24%")
col2.metric("Lake King North", "9.07", "4.01%")
col3.metric("Lake Victoria", "11.38", "-1.78%")
col4.metric("Lake Wellington", "7.56", "-5.93%")
col5.metric("Shaving Point", "8.99", "14.14%")


# Load the dataset
file_path = '/Users/sam/PycharmProjects/gibbslands_web_app/1990_01-2023_06_Gippsland_Lakes_Water_quality_data.xlsx'
data = pd.read_excel(file_path)

# Calculate the percentage of missing values for each column
missing_data_percentage = data.isnull().mean() * 100

# Set a threshold for missing data to decide whether to drop the column
threshold = 50  # percentage
columns_to_drop = missing_data_percentage[missing_data_percentage > threshold].index.tolist()

# Drop columns with missing data above the threshold
data_cleaned = data.drop(columns=columns_to_drop)

# Remove any duplicate rows in the dataset
data_cleaned = data_cleaned.drop_duplicates()

# Rename columns for clarity and consistency
renamed_data = data_cleaned.rename(columns=lambda x: x.strip().replace(" ", "_").lower())

# Isolate the columns for salinity and dissolved oxygen along with 'date' and 'site_name_short'
water_quality_data = renamed_data[['sal', 'do_mg', 'date', 'site_name_short']]

# Drop rows where 'sal' or 'do_mg' are missing
water_quality_comparison_data = water_quality_data.dropna(subset=['sal', 'do_mg'])

water_quality_comparison_data1 = water_quality_comparison_data[water_quality_comparison_data['site_name_short'] != 'Lake Reeve\xa0East']
# drop Lake_Reeve_East as its only has data from the last few years

water_quality_trends = water_quality_comparison_data1.groupby(['site_name_short', 'date']).mean().reset_index()


#Streamlit app
def main():
    pass
    fig = plot_dissolved_oxygen_trends(water_quality_trends)
    tab2.pyplot(fig)
    fig1 = plot_salinity_trends(water_quality_trends)
    tab2.pyplot(fig1)



if __name__ == "__main__":
    main()