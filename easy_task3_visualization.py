# ==========================================
# EASY TASK 3: DATA VISUALIZATION
# ==========================================

# Step 1: Import Required Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load Dataset
# Replace "students.csv" with your actual file name

data = pd.read_csv("StudentsPerformance.csv")

# Display Success Message
print("Dataset Loaded Successfully!")
print("----------------------------------------")

# ==========================================
# GRAPH 1: BAR CHART
# Average Scores of Subjects
# ==========================================

average_scores = data[['math score', 'reading score', 'writing score']].mean()

plt.figure(figsize=(8,5))
plt.bar(average_scores.index, average_scores)

plt.title("Average Scores of Subjects")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

print("Bar Chart Displayed Successfully!")

# ==========================================
# GRAPH 2: HISTOGRAM
# Math Score Distribution
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(data['math score'], bins=10)

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Frequency")

plt.show()

print("Histogram Displayed Successfully!")

# ==========================================
# GRAPH 3: PIE CHART
# Gender Distribution
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

print("Pie Chart Displayed Successfully!")

# ==========================================
# GRAPH 4: LINE CHART
# Subject Scores Trend
# ==========================================

subject_average = data[['math score', 'reading score', 'writing score']].mean()

plt.figure(figsize=(8,5))

plt.plot(subject_average.index, subject_average)

plt.title("Average Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

print("Line Chart Displayed Successfully!")

# ==========================================
# GRAPH 5: SCATTER PLOT
# Math Score vs Reading Score
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

print("Scatter Plot Displayed Successfully!")

print("----------------------------------------")
print("Data Visualization Completed Successfully!")