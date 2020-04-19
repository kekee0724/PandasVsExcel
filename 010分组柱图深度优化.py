import pandas as pd
import matplotlib.pyplot as plt
import random

students = pd.read_excel('Temp/Field009.xlsx')  # , index_col='Field'
students.sort_values(by=2017, inplace=True, ascending=False)
# for i in homes.index:
#     homes.at[i, 2016] = random.randint(100, 2000) * 100
print(students)
# homes.to_excel('Temp/Field009.xlsx')
students.plot.bar(x='Field', y=[2016, 2017], color=['pink', '#303030'], title='International Students by Field')
# plt.bar(homes.Field,homes.Number,color='pink')
# plt.xticks(homes.Field,rotation='90')
plt.title('International Students by Field', fontsize=16, fontweight='bold')
plt.xlabel('Field', fontweight='bold')
plt.ylabel('Years', fontweight='bold')
ax = plt.gca()
ax.set_xticklabels(students['Field'], rotation=45, ha='right')  # 旋转45度 对齐文字
f = plt.gcf()
f.subplots_adjust(left=0.2, bottom=0.42)
# plt.tight_layout()
plt.show()
