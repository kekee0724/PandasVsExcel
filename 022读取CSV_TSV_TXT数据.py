import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = 777
videos = pd.read_excel('Temp/Videos.xlsx', index_col='Month')  # , index_col='Field'
table = videos.transpose()
print(table)
