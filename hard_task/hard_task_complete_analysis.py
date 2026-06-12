# ==========================================
# HARD TASK: COMPLETE DATA ANALYSIS PROJECT
# ==========================================

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Step 2: Load Dataset
# ==========================================

data = pd.read_csv("StudentsPerformance.csv")

print("Dataset Loaded Successfully!")
print("----------------------------------------")

# ==========================================
# Step 3: Explore Dataset
# ==========================================

print("First 5 Rows of Dataset:")
print(data.head())

print("\n----------------------------------------")

print("Dataset Shape:")
print(data.shape)

print("\n----------------------------------------")

print("Dataset Information:")
print(data.info())

print("\n----------------------------------------")

# ==========================================
# Step 4: Check Missing Values
# ==========================================

print("Missing Values:")
print(data.isnull().sum())

print("\n----------------------------------------")

# ==========================================
# Step 5: Remove Duplicate Rows
# ==========================================

duplicates = data.duplicated().sum()

print("Number of Duplicate Rows:", duplicates)

data = data.drop_duplicates()

print("Duplicates Removed Successfully!")

print("\n----------------------------------------")

# ==========================================
# Step 6: Fill Missing Values
# ==========================================

# Fill Numerical Columns with Mean
numeric_columns = data.select_dtypes(include=['number']).columns

for column in numeric_columns:
    data[column] = data[column].fillna(data[column].mean())

# Fill Text Columns with Mode
text_columns = data.select_dtypes(include=['object']).columns

for column in text_columns:
    data[column] = data[column].fillna(data[column].mode()[0])

print("Missing Values Handled Successfully!")

print("\n----------------------------------------")

# ==========================================
# Step 7: Statistical Analysis
# ==========================================

print("Statistical Summary:")
print(data.describe())

print("\n----------------------------------------")

print("Mean Values:")
print(data.mean(numeric_only=True))

print("\n----------------------------------------")

print("Median Values:")
print(data.median(numeric_only=True))

print("\n----------------------------------------")

print("Maximum Values:")
print(data.max(numeric_only=True))

print("\n----------------------------------------")

print("Minimum Values:")
print(data.min(numeric_only=True))

print("\n----------------------------------------")

# ==========================================
# Step 8: Correlation Analysis
# ==========================================

correlation = data.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation)

print("\n----------------------------------------")

# ==========================================
# Step 9: Visualization 1
# Bar Chart
# ==========================================

average_scores = data[
    ['math score', 'reading score', 'writing score']
].mean()

plt.figure(figsize=(8,5))

plt.bar(
    average_scores.index,
    average_scores
)

plt.title("Average Scores of Subjects")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

# ==========================================
# Step 10: Visualization 2
# Histogram
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(data['math score'], bins=10)

plt.title("Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Frequency")

plt.show()

# ==========================================
# Step 11: Visualization 3
# Pie Chart
# ==========================================

gender_count = data['gender'].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct='%1.1f%%'
)

plt.title("Gender Distribution")

plt.show()

# ==========================================
# Step 12: Visualization 4
# Scatter Plot
# ==========================================

plt.figure(figsize=(8,5))

plt.scatter(
    data['math score'],
    data['reading score']
)

plt.title("Math Score vs Reading Score")
plt.xlabel("Math Score")
plt.ylabel("Reading Score")

plt.show()

# ==========================================
# Step 13: Findings / Conclusion
# ==========================================

print("PROJECT FINDINGS")
print("----------------------------------------")

print("1. Student performance differs across subjects.")

print("2. Reading and Writing scores are strongly related.")

print("3. Data visualization helped understand score patterns.")

print("4. Data cleaning improved dataset quality.")

print("5. Correlation analysis helped identify relationships.")

print("\n----------------------------------------")

# ==========================================
# Step 14: Save Cleaned Dataset
# ==========================================

data.to_csv("final_cleaned_students.csv", index=False)

print("Final Cleaned Dataset Saved Successfully!")

print("\n----------------------------------------")

print("COMPLETE DATA ANALYSIS PROJECT FINISHED!")
