# ======== HIGH LEVEL DATA UNDERSTANDING =========

# Number of rows and columns in the dataset

print("Shape : ", df.shape)

# Data types of columns

print("Data types of columns :\n", df.dtypes)

# Info and describe of dataset

print("Info : \n")
df.info()
print("Statistical Summary : \n", df.describe())