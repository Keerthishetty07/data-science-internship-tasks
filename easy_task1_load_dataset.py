# ==========================================
# EASY TASK 1: LOAD AND EXPLORE A DATASET
# ==========================================

# Step 1: Import Required Library
import pandas as pd

# Step 2: Load the Dataset
# Replace "students.csv" with your actual file name

data = pd.read_csv("StudentsPerformance.csv")

# Step 3: Display Dataset Successfully Loaded Message
print("Dataset Loaded Successfully!")
print("-----------------------------------")

# Step 4: Display First 5 Rows
print("First 5 Rows of Dataset")
print(data.head())

print("\n-----------------------------------")

# Step 5: Display Last 5 Rows
print("Last 5 Rows of Dataset")
print(data.tail())

print("\n-----------------------------------")

# Step 6: Display Number of Rows and Columns
print("Shape of Dataset")
print("Number of Rows and Columns:")
print(data.shape)

print("\n-----------------------------------")

# Step 7: Display Column Names
print("Column Names in Dataset")
print(data.columns)

print("\n-----------------------------------")

# Step 8: Display Dataset Information
print("Dataset Information")
print(data.info())

print("\n-----------------------------------")

# Step 9: Display Data Types
print("Data Types of Each Column")
print(data.dtypes)

print("\n-----------------------------------")

# Step 10: Display Random Sample Rows
print("Random Sample Rows")
print(data.sample(5))

print("\n-----------------------------------")

# Step 11: Check Missing Values
print("Missing Values in Dataset")
print(data.isnull().sum())

print("\n-----------------------------------")

# Step 12: Display Total Number of Elements
print("Total Number of Elements in Dataset")
print(data.size)

print("\n-----------------------------------")

# Step 13: Display Statistical Overview
print("Basic Statistical Summary")
print(data.describe())

print("\n-----------------------------------")

# Step 14: Print Completion Message
print("Dataset Exploration Completed Successfully!")