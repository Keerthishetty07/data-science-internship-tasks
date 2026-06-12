# ==========================================
# MEDIUM TASK 2: CORRELATION ANALYSIS
# ==========================================

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load Dataset
# Replace "students.csv" with your actual file name

data = pd.read_csv("StudentsPerformance.csv")

# Display Success Message
print("Dataset Loaded Successfully!")
print("----------------------------------------")

# ==========================================
# Step 3: Select Numerical Columns
# ==========================================

numerical_data = data.select_dtypes(include=['number'])

print("Numerical Columns Selected:")
print(numerical_data.columns)

print("\n----------------------------------------")

# ==========================================
# Step 4: Generate Correlation Matrix
# ==========================================

correlation_matrix = numerical_data.corr()

print("Correlation Matrix:")
print(correlation_matrix)

print("\n----------------------------------------")

# ==========================================
# Step 5: Visualize Correlation Matrix
# ==========================================

plt.figure(figsize=(8,6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Matrix of Student Scores")

plt.show()

print("Correlation Heatmap Displayed Successfully!")

print("\n----------------------------------------")

# ==========================================
# Step 6: Analyze Strong Correlations
# ==========================================

print("Analysis of Correlations:")

for column in correlation_matrix.columns:
    print(f"\nCorrelation of {column}:")
    print(correlation_matrix[column])

print("\n----------------------------------------")

# ==========================================
# Completion Message
# ==========================================

print("Correlation Analysis Completed Successfully!")