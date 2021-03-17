import pandas as pd
index = pd.date_range("1/1/2019", periods=20, freq='D')
series = pd.Series(range(20), index=index)
# print(index)
# print(series)
#1. 將所有轉為周資料
week_seris = series.to_period('W')
week_seris
#2. 將周資料的值取平均
mean_week = week_seris.mean()
mean_week
#2. 將周資料的值取平均
mean_week = week_seris.resample('W').mean()
mean_week

print(week_seris.resample('W'))
print(week_seris)