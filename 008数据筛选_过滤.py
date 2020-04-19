import pandas as pd

# import random
# def age(a):
#     return 18 <= a < 30
# x = lambda a: 18 <= a < 30
# def level(a):
#     return 85 <= a <= 100
# y = lambda a: 85 <= a <= 100

students = pd.read_excel('Temp/Student.xlsx', index_col='ID')
# for i in homes.index:
#     homes.at[i, 'Age'] = random.randint(16, 30)
#     homes.at[i, 'Score'] = random.randint(50, 100)
# homes.sort_values(by='Age', inplace=True, ascending=False)
# homes.sort_values(by='Score', inplace=True, ascending=False)
# homes.sort_values(by=['Age', 'Score'], inplace=True, ascending=[True, False])
# homes = homes.loc[homes['Age'].apply(lambda a: 18 <= a < 30)]
# homes = homes.loc[homes['Score'].apply(lambda a: 85 <= a <= 100)]
students = students.loc[students.Age.apply(lambda a: 18 <= a < 24)]\
    .loc[students.Score.apply(lambda a: 90 <= a <= 100)]

print(students)
# homes.to_excel('Temp/Student.xlsx')
