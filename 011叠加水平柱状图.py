import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('Temp/Users.xlsx')  # , index_col='ID'
# import random
# for i in homes.index:
#     homes.at[i, 'Oct'] = random.randint(10, 20)
# homes.to_excel('Temp/Users.xlsx')
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True, ascending=False)
print(users)
# homes.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, color=['pink', '#303030', 'orange'],
#                title='User Behavior')
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, color=['pink', '#303030', 'orange'],
               title='User Behavior')
plt.tight_layout()
plt.show()
