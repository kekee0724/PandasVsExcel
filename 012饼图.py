import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('Temp/Students012.xlsx', index_col='From')  # , index_col='Field'
# import random
# for i in homes.index:
#     homes.at[i, '2017'] = random.randint(45 - 2 * i, 55 - 2 * i) * 876
# homes.to_excel('Temp/Students012.xlsx')
# homes['Total'] = homes['Oct'] + homes['Nov'] + homes['Dec']
# homes.sort_values(by='Total', inplace=True, ascending=False)
print(students)
# homes['2017'].sort_values(ascending=True).plot.pie(fontsize=8,startangle=-270)
students['2017'].plot.pie(fontsize=8, counterclock=False, startangle=-270)
plt.title('Source of International Students', fontsize=16, fontweight='bold')
# plt.xlabel('Field', fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.show()
