import pandas as pd
import matplotlib.pyplot as plt


def score_validation(row):
    # if not 0 <= row.Score <= 100: print(f'#{row.ID}\tstudent {row.Name} has an invalid score:{row.Score}')
    try:
        assert 0 <= row.Score <= 100
    except:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score:{row.Score}')


students = pd.read_excel('Temp/Student017.xlsx')  # , index_col='Field'

# print(students)
students.apply(score_validation, axis=1)

