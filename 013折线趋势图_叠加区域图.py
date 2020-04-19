import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('Temp/Weeks.xlsx', index_col='Week')  # , index_col='Field'
# import random
# for i in homes.index:
#     homes.at[i, 'Accessories'] = random.randint(5000, 8000)
# homes['Grand Total'] = homes['Accessories'] + homes['Bikes'] + homes['Clothing'] + homes['Component']
# homes.to_excel('Temp/Weeks.xlsx')

print(weeks)
print(weeks.columns)
# homes.plot(y=['Accessories', 'Bikes', 'Clothing', 'Component']) # 折线趋势图
# homes.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Component'])  # 叠加区域图
weeks.plot.bar(y=['Accessories', 'Bikes', 'Clothing', 'Component'], stacked=True)  # 叠加柱状图
plt.title('Sales Weekly Trend', fontsize=16, fontweight='bold')
plt.ylabel('Total', fontsize=12, fontweight='bold')
plt.xticks(weeks.index, fontsize=5)
plt.show()
