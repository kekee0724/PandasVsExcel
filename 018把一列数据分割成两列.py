import pandas as pd
import matplotlib.pyplot as plt

employees = pd.read_excel('Temp/Employees.xlsx', index_col='ID')  # , index_col='Field'
df = employees['Full Name'].str.split('_', expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]  # .str.upper()
# print(df)
print(employees)
