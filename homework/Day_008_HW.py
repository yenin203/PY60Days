import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]
dataNum = np.count_nonzero(name_list)
#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
dt = np.dtype([('Name', '<U5'), ('Sex', '<U5'), ('Weight', '<f2'), ('Rank', '<i2'), ('Myopia', '?')])

# name_list, sex_list, weight_list, rank_list, myopia_list

c = np.zeros(dataNum, dtype=dt)
c['Name'] = name_list
c['Sex'] = sex_list
c['Weight'] = weight_list
c['Rank'] = rank_list
c['Myopia'] = myopia_list
c
# print(c)
#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重
avg_w = np.average(weight_list)
avg_w
print(avg_w)
#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重

result3 = np.mean(c['Weight'][np.argwhere(c['Sex'] == 'boy')])
result3
print(result3)
#3. 呈上題，進一步算出女生(sex欄位是girl)平均體重
result3_2 = np.mean(c['Weight'][np.argwhere(c['Sex'] == 'girl')])
result3_2
print(result3_2)