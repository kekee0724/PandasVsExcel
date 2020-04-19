import pandas as pd

books = pd.read_excel('Temp/Books005.xlsx', index_col='ID')


# books.set_index('ID', inplace=True)
# for i in books.index:
#     books.at[i, 'Price'] = books.at[i, 'Listpride'] * books.at[i, 'Discount']
# def add_two(x):
#     return x + 2

# books['ListPrice'] = books['ListPrice'].apply(add_two)
books['ListPrice'] = books['ListPrice'].apply(lambda x:x+2)
# books['ListPrice'] += 2
books['Price'] = books['ListPrice'] * books['Discount']

print(books)
# books.to_excel('Temp/Output005.xlsx')
