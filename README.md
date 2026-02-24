# COVID-19 Data Analysis Project using Python

## Project Overview
This project performs a comprehensive analysis of COVID-19 data using Python and pandas. It covers high-level and low-level data understanding, data cleaning, feature engineering, aggregation, and visualization to gain insights into COVID-19 trends across continents.  

**Dataset URL:** [covid-data.csv](https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv)

Step 1: Import Dataset
import pandas as pd

url = "https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv"
df = pd.read_csv(url)
print(df.head())

Step 2: High-Level Data Understanding
Checked dataset shape (rows and columns).
Checked data types of each column.
Used df.info() to inspect missing values.
Generated statistical summary with df.describe().

Step 3: Low-Level Data Understanding
Counted unique locations.
Identified continent with maximum frequency.
Found maximum and mean of total_cases.
Calculated 25%, 50%, and 75% quartiles of total_deaths.
Identified continent with maximum human_development_index.
Identified continent with minimum gdp_per_capita.

Step 4: Filter Relevant Columns
Kept only necessary columns: ['continent','location','date','total_cases','total_deaths','gdp_per_ca
pita','human_development_index'] 

Step 5: Data Cleaning
Removed duplicate rows.
Checked for missing values.
Dropped rows where continent was missing.
Filled remaining missing values with 0

Step 6: Date Conversion
Converted date column to datetime format.
Created a new column month extracted from date.

Step 7: Data Aggregation
Grouped by continent to find maximum values per continent.
Stored results in df_groupby.

Step 8: Feature Engineering
Created a new feature total_deaths_to_total_cases to calculate death ratio per continent.

Step 9: Data Visualization
Histogram of gdp_per_capita:
Scatter Plot of total_cases vs gdp_per_capita.
Pairplot of all numerical columns.
Bar Plot of continent vs total_cases

Step 10: Save Processed Data
Saved the final processed and aggregated dataset

## Outcome
Cleaned and aggregated dataset ready for analysis.
Visualizations provide insights into COVID-19 cases and GDP trends across continents.
Created a new feature total_deaths_to_total_cases for understanding the death rate per continent.


---

✅ **How to use:**  
1. Open a text editor or VSCode.  
2. Create a new file called `README.md`.  
3. Paste everything above.  
4. Save and upload to your GitHub repo.  

---

If you want, I can also **add GitHub badges, a small description for each visualization, and make it look like a “professional project repo README”** that looks very polished on GitHub.  

Do you want me to do that next?
