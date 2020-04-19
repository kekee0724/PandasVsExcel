import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 777
# students = pd.read_excel('Temp/Student_score.xlsx', sheet_name='Students', usecols='A:B')  # , index_col='Field'
# scores = pd.read_excel('Temp/Student_score.xlsx', sheet_name='Scores')
# table = students.merge(scores, on='ID', how='left').fillna(0)  # NaN填充0 on left_on right_on

students = pd.read_excel('Temp/Student_score.xlsx', sheet_name='Students', usecols='A:B',
                         index_col='ID')  # , index_col='Field'
scores = pd.read_excel('Temp/Student_score.xlsx', sheet_name='Scores', index_col='ID')
table = students.join(scores, how='left',on='ID').fillna(0)  # NaN填充0 on left_on right_on

table.Score = table.Score.astype(int)  # 成绩为整数
print(table)

