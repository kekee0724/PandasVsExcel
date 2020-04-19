import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('Temp/Students_Duplicates.xlsx', index_col='ID')  # , index_col='Field'
# students.drop_duplicates(subset='Name',inplace=True,keep='last')

dupe = students.duplicated(subset='Name')
# print(dupe)
# print(dupe.any())
# print(type(dupe))

dupe = dupe[dupe]
print(dupe)
print(dupe.index)

print(students.iloc[dupe.index])
# print(students)
