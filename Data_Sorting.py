import pandas as pd
import numpy as np
import matplotlib
import math

# importing Data from CSV, droping out the NA values and creating the Data Series called salary,
# then sorting values 2 times and presenting the first 15 values.
# Finally -> creating other series to find 100 the biggest salaries and 100 the smallest salaries

salary = pd.read_csv("C:/Users/demes/Downloads/data/course-files/StackOverflowDeveloperSurvey.csv", usecols = ["Salary"]).dropna().squeeze()

print(salary.sort_values)
print(salary.sort_values(ascending = False))
salarySorted = salary.sort_values()
print(salarySorted.head(15))

salary.sort_index(ascending = False)

maxSalaries = salary.sort_values(ascending = False).head(100)
maxSalaries

minSalaries = salary.sort_values().head(100)
minSalaries

print("The average of the biggest 100 salaries is: ", maxSalaries.mean())
print("The average of the smallest 100 salaries is: ", minSalaries.mean())