import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/AmesHousing.csv")

# Display first few rows
print(df.head())

# Check missing values
print(df.isnull().sum().sort_values(ascending=False)[:20])

# Convert numeric columns and fill missing values
numeric_cols = df.select_dtypes(include=["number"]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=["number"])

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(numeric_df.corr(), cmap="coolwarm", annot=False)
plt.title("Feature Correlation Heatmap")
plt.show()
