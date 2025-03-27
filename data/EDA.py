# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud

# Load datasets
sephora_df = pd.read_csv("sephora_dataset.csv")  # American skincare
yesstyle_df = pd.read_csv("yesstyle_dataset.csv")  # Korean skincare

# Display first few rows
print("Sephora (American) Skincare Data:")
display(sephora_df.head())

print("\nYesStyle (Korean) Skincare Data:")
display(yesstyle_df.head())

# Check dataset info
print("\nSephora Dataset Info:")
sephora_df.info()

print("\nYesStyle Dataset Info:")
yesstyle_df.info()

# Check missing values
print("\nMissing Values in Sephora Dataset:")
print(sephora_df.isnull().sum())

print("\nMissing Values in YesStyle Dataset:")
print(yesstyle_df.isnull().sum())

# Drop duplicates if needed
sephora_df = sephora_df.drop_duplicates()
yesstyle_df = yesstyle_df.drop_duplicates()

# Convert price to numeric
sephora_df["price_usd"] = sephora_df["price_usd"].astype(float)
yesstyle_df["price_usd"] = yesstyle_df["price_usd"].astype(float)

# Check cleaned data
print("\nPrice Column After Cleaning:")
print(sephora_df["price_usd"].head())
