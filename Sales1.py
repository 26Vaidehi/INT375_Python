import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## LOADING THE DATASET
df = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Python_datasets\INT-375\global_superstore_sales_messy.csv')
print(df)  # Printing the dataset

# EXPLORING THE DATASET
print("Information of the Dataset:",df.info())
print("Description of the Dataset:", df.describe())

## HANDLING THE MISSING VALUES
print("Missing Values Before Cleaning:\n", df.isnull().sum())

df["Sales"] = df["Sales"].fillna(df["Sales"].mean())         # Fill Sales with mean
df["Profit"] = df["Profit"].fillna(df["Profit"].median())       # Fill Profit with median
df["Customer Name"] = df["Customer Name"].fillna(df["Customer Name"].mode()[0])     # Fill Name with mode

df.replace("", pd.NA, inplace=True)          # Convert empty strings to NaN
df.dropna(inplace=True)          # Remove remaining NaNs

print("Missing Values After Cleaning:\n", df.isnull().sum())

print(df)           ## Printing the cleaned dataset
