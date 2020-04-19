import pandas as pd
import matplotlib.pyplot as plt
import random

students = pd.read_excel('Temp/Field.xlsx')  # , index_col='Field'
students.sort_values(by='Number', inplace=True, ascending=False)
# for i in homes.index:
#     homes.at[i, 'Number'] = random.randint(100, 2000) * 100
print(students)
# homes.to_excel('Temp/Field.xlsx')
# homes.plot.bar(x='Field', y='Number',color='pink',title='International Students by Field')
plt.bar(students.Field,students.Number,color='pink')
plt.xticks(students.Field,rotation='90')
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Students by Field',fontsize=16)
plt.tight_layout()
plt.show()
