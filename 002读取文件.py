import pandas as pd

# header=0
# header = None
# people = pd.read_excel('Temp/16软工.xlsx', header=0)
people = pd.read_excel('Temp/16软工.xlsx', index_col='学号')
# people.columns = ['学院', '学号', '姓名', '学历', '专业', '生源地区', '班级', '联系方式',
#                   '就业动态', '已签约单位名称', '辅导员姓名', '辅导员联系方式', '备注']
# people.set_index('学号',inplace=True)
# people=people.set_index('学号')
print(people.shape)  # 打印行列
print(people.columns)  # 打印标题
print(people.head(3))  # 打印前仨排数据
print('=' * 20)
print(people.tail(3))  # 打印后仨排数据
# people.to_excel('Temp/16软工1.xlsx')
# print('Done')