import pandas as pd

# import random

# def ran(l = ['Yes', 'No']):
#     return l[random.randint(0, 1)]
#
# lambda l = ['Yes', 'No']:l[random.randint(0, 1)]


products = pd.read_excel('Temp/List.xlsx', index_col='ID')
# for i in products.index:
#     products.at[i, 'Price'] = round(random.uniform(5, 20), 2)
#     products.at[i, 'Worthy'] = ran()
# products.sort_values(by='Price', inplace=True, ascending=False)
# products.sort_values(by='Worthy', inplace=True, ascending=False)
products.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=[True, False])
print(products)
# products.to_excel('Temp/List.xlsx')
