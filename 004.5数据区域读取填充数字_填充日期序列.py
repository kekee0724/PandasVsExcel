import pandas as pd
from datetime import date, timedelta

start = date(2018, 1, 1)


def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


#
#
# print(add_month(start, 200))

books = pd.read_excel('Temp/Books004.xlsx', skiprows=3, usecols='E:H', index_col=None,
                      dtype={'ID': str, 'InStore': str, 'Date': str})
# print(type(books['ID']))
# books['ID'].at[0] = 100
# print(books['ID'])

for i in books.index:
    # books['ID'].at[i] = i + 1
    books.at[i, 'ID'] = i + 1
    # books['InStore'].at[i] = 'Yes' if i % 2 == 0 else 'No'
    books.at[i, 'InStore'] = 'Yes' if i % 2 == 0 else 'No'
    # # books['Date'].at[i] = start + timedelta(days=i)
    books.at[i, 'Date'] = add_month(start, i)
books.set_index('ID', inplace=True)
print(books)
books.to_excel('Temp/output004.xlsx')
