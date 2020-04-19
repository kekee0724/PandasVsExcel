import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 777
homes = pd.read_excel('Temp/home_data.xlsx')  # , index_col='Field'
# import random
# for i in homes.index:
#     homes.at[i, 'id'] = random.randint(16000123, 8862768727)
#     homes.at[i, 'price'] = random.randint(180000, 2000000)
#     homes.at[i, 'bedrooms'] = random.randint(1, 6)
#     homes.at[i, 'bathrooms'] = random.randint(4, 18) / 4
#     homes.at[i, 'sqft_living'] = random.randint(50, 365) * 10
#     homes.at[i, 'sqft_basement'] = random.randint(0, 200) * 10
#     homes.at[i, 'sqft_lot'] = random.randint(1200, 101920)
#     homes.at[i, 'floors'] = random.randint(2, 6) / 2
#     homes.at[i, 'yr_built'] = random.randint(1910, 2019)
# homes.set_index('id', inplace=True)
# homes.to_excel('Temp/home_data.xlsx')

# print(homes.head())
# print(homes.columns)
print(homes.corr())  # 数据关联
# 散点图
# homes.plot.scatter(x='sqft_living',y='price')
# 直方图
# homes.sqft_living.plot.hist(bins=100)
# plt.xticks(range(0, max(homes.sqft_living), 200), fontsize=8, rotation=90)
# 密度图
# homes.sqft_living.plot.kde()
# plt.xticks(range(0, max(homes.sqft_living), 200), fontsize=8, rotation=90)
#
# plt.show()
