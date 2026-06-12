# ==========================================
# MEDIUM TASK 1: DATA CLEANING
# ==========================================

# Step 1: Import Required Library
import pandas as pd

# Step 2: Load Dataset

data = pd.read_csv("StudentsPerformance.csv")

# Display Success Message
print("Dataset Loaded Successfully!")
print("----------------------------------------")

# ==========================================
# Step 3: Display Original Dataset Shape
# ==========================================

print("Original Dataset Shape:")
print(data.shape)

print("\n----------------------------------------")

# ==========================================
# Step 4: Check Missing Values
# ==========================================

print("Missing Values in Dataset:")
print(data.isnull().sum())

print("\n----------------------------------------")

# ==========================================
# Step 5: Check Duplicate Rows
# ==========================================

duplicate_rows = data.duplicated().sum()

print("Number of Duplicate Rows:")
print(duplicate_rows)

print("\n----------------------------------------")

# ==========================================
# Step 6: Remove Duplicate Rows
# ==========================================

data = data.drop_duplicates()

print("Duplicate Rows Removed Successfully!")

print("Dataset Shape After Removing Duplicates:")
print(data.shape)

print("\n----------------------------------------")

# ==========================================
# Step 7: Handle Missing Values
# Replace Missing Numerical Values with Mean
# ==========================================

numeric_columns = data.select_dtypes(include=['number']).columns

for column in numeric_columns:
    data[column] = data[column].fillna(data[column].mean())

print("Missing Numerical Values Filled Successfully!")

print("\n----------------------------------------")

# ==========================================
# Step 8: Handle Missing Text Values
# Replace Missing Text Values with Mode
# ==========================================

text_columns = data.select_dtypes(include=['object']).columns

for column in text_columns:
    data[column] = data[column].fillna(data[column].mode()[0])

print("Missing Text Values Filled Successfully!")

print("\n----------------------------------------")

# ==========================================
# Step 9: Verify Missing Values Again
# ==========================================

print("Missing Values After Cleaning:")
print(data.isnull().sum())

print("\n----------------------------------------")

# ==========================================
# Step 10: Check Data Types
# ==========================================

print("Updated Data Types:")
print(data.dtypes)

print("\n----------------------------------------")

# ==========================================
# Step 11: Display Cleaned Dataset Sample
# ==========================================

print("First 5 Rows of Cleaned Dataset:")
print(data.head())

print("\n----------------------------------------")

# ==========================================
# Step 12: Save Cleaned Dataset
# ==========================================

data.to_csv("cleaned_students.csv", index=False)

print("Cleaned Dataset Saved Successfully!")
print("File Name: cleaned_students.csv")

print("\n----------------------------------------")

# ==========================================
# Completion Message
# ==========================================

print("Data Cleaning Completed Successfully!")
