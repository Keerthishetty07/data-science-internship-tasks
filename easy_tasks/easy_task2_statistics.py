# ==========================================
# EASY TASK 2: DATA SUMMARY AND STATISTICS
# ==========================================

# Step 1: Import Required Library
import pandas as pd

# Step 2: Load Dataset
# Replace "students.csv" with your actual file name

data = pd.read_csv("StudentsPerformance.csv")

# Display Success Message
print("Dataset Loaded Successfully!")
print("----------------------------------------")

# Step 3: Display Statistical Summary
print("Statistical Summary of Dataset")
print(data.describe())

print("\n----------------------------------------")

# Step 4: Calculate Mean Values
print("Mean Values of Numerical Columns")
mean_values = data.mean(numeric_only=True)
print(mean_values)

print("\n----------------------------------------")

# Step 5: Calculate Median Values
print("Median Values of Numerical Columns")
median_values = data.median(numeric_only=True)
print(median_values)

print("\n----------------------------------------")

# Step 6: Find Maximum Values
print("Maximum Values in Numerical Columns")
maximum_values = data.max(numeric_only=True)
print(maximum_values)

print("\n----------------------------------------")

# Step 7: Find Minimum Values
print("Minimum Values in Numerical Columns")
minimum_values = data.min(numeric_only=True)
print(minimum_values)

print("\n----------------------------------------")

# Step 8: Calculate Standard Deviation
print("Standard Deviation of Numerical Columns")
std_values = data.std(numeric_only=True)
print(std_values)

print("\n----------------------------------------")

# Step 9: Count Non-Null Values
print("Count of Non-Null Values")
print(data.count())

print("\n----------------------------------------")

# Step 10: Check Unique Values in Each Column
print("Number of Unique Values in Each Column")
print(data.nunique())

print("\n----------------------------------------")

# Step 11: Display Correlation Between Numerical Columns
print("Correlation Matrix")
print(data.corr(numeric_only=True))

print("\n----------------------------------------")

# Step 12: Print Completion Message
print("Data Summary and Statistics Completed Successfully!")
