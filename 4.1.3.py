import pandas as pd

# Read the text file into a DataFrame
file = input()
data = pd.read_csv(file, sep="\s+", header=None, names=["Name", "Age", "Grade"])


# write your code here..

print("First five rows:")
print(data.head())
average_age=round(data['Age'].mean(),2)
print(f"Average age: {average_age}")
threshold_grade='B'
filtered_data=data[data['Grade']<=threshold_grade]
print(f"Students with a grade up to {threshold_grade}")
print(filtered_data)

 