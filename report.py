# importing required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# dataset URL
url = "https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv"

# Impoort dataset
df = pd.read_csv(url)

# # first 5 columns of the dataset
print(df.head())

# ======== HIGH LEVEL DATA UNDERSTANDING =========

# Number of rows and columns in the dataset

print("Shape : ", df.shape)

# Data types of columns

print("Data types of columns :\n", df.dtypes)

# Info and describe of dataset

print("Info : \n")
df.info()
print("Statistical Summary : \n")
print(df.describe(include='all'))


# ======== LOW LEVEL DATA UNDERSTANDING =========

# Count of unique values in location column.

print("Number of Unique locations : ", df['location'].nunique())

# Continent that has maximum frequency using values counts.

print("Maximum frequency continent : ", df['continent'].value_counts().idxmax())

# Maximum & mean value in 'total_cases'

print("Maximum value of 'total cases: ", df['total_cases'].max())
print("Mean value of 'total cases: ", df['total_cases'].mean())

# 25%,50% & 75% quartile value in 'total_deaths'

print("Percentiles of total deaths: ")
print("\n25 perrcentile : ", df['total_deaths'].quantile(0.25))
print("\n50 perrcentile : ", df['total_deaths'].quantile(0.50))
print("\n75 perrcentile : ", df['total_deaths'].quantile(0.75))

# Continent has maximum 'human_development_index'.

print("Continent with maximum human_development_index:", df.groupby('continent')['human_development_index'].max().idxmax())

# Continent has minimum 'gdp_per_capita'.

print("Continent with minimum gdp_per_capita:", df.groupby('continent')['gdp_per_capita'].min().idxmin())

#  ======== Filtering Dataset =========

df1 = df[['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']]

print("Filtered data : \n")
print(df1.head())

#  ======== Data Cleaning =========

# Remove all duplicates observations

df1 = df1.drop_duplicates()

#  Find missing values in all columns

print("Count of missing values in all columns..... ")
print(df1.isnull().sum())

# Remove all observations where continent column value is missing

df1 = df1.dropna(subset=['continent'])

# Fill all missing values with 0

df1 = df1.fillna(0)

print("\nAfter cleaning:")
print(df1.isnull().sum())

# ======== DATE TIME FORMAT =========

# convert data column to datetime format
df1['date'] = pd.to_datetime(df1['date'])

# create new column "Month"
df1['month'] = df1['date'].dt.month

print("Data after adding month column :\n")
print(df1.head())

# ======== DATA AGGREAGTION =========

# Max value in all columns using groupby function on 'continent'

df_groupby = df1.groupby('continent').max().reset_index()

print("Grouped dataframe......")
print(df_groupby)

# ======== FEATURE ENGINEERING =========

# a. Create a new feature 'total_deaths_to_total_cases' by ratio of  'total_deaths' column to 'total_cases'

df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']

print(df_groupby.head())


# ======== DATA VISUALIZATION =========

# Univariate analysis on 'gdp_per_capita' column by plotting {Histogram of gdp_per_capita}

sns.histplot(df_groupby['gdp_per_capita'], kde=True)
plt.title("Distribution of GDP per capita")
plt.show()

# Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
sns.scatterplot(x = 'gdp_per_capita', y = 'total_cases', data = df_groupby)
plt.title("Total Cases vs GDP per capita")
plt.show()

# Pairplot on df_groupby

sns.pairplot(df_groupby)
plt.show()

# Bar Plot of continent with total_cases

sns.catplot(x='continent', y='total_cases', data = df_groupby, kind = 'bar')
plt.title("Total Cases by Continent")
plt.show()

# ======== SAVE DATAFRAME =========

df_groupby.to_csv("covid_analysis_output.csv", index=False)
df_groupby.to_excel("covid_analysis_output.xlsx", index=False)

print("File saved sucessfully")