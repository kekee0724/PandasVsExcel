import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('Temp/Student019.xlsx', index_col='ID')  # , index_col='Field'
# import random
# for i in students.index:
#     students.at[i, 'Test_1'] = random.randint(50, 100)
#     students.at[i, 'Test_2'] = random.randint(45, 95)
#     students.at[i, 'Test_3'] = random.randint(56, 89)

# students.to_excel('Temp/Student019.xlsx')
temp = students[['Test_1', 'Test_2', 'Test_3']]
students['Total'] = temp.sum(axis=1)
students['Average'] = temp.mean(axis=1)

col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
col_mean['Name'] = 'Summary'
students = students.append(col_mean, ignore_index=True)

students.Test_1 = students.Test_1.astype(int)  # 成绩为整数
students.Test_2 = students.Test_2.astype(int)  # 成绩为整数
students.Test_3 = students.Test_3.astype(int)  # 成绩为整数

print(students)
