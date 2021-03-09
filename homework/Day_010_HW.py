
import pandas as pd
STOCK_DAY09 = 'STOCK_DAY_0050_202009.csv'
STOCK_DAY10 = 'STOCK_DAY_0050_202010.csv'
#讀取STOCK_DAY_0050_202009.csv、STOCK_DAY_0050_202010.csv

day9_data = pd.read_csv(STOCK_DAY09)
day10_data = pd.read_csv(STOCK_DAY10)
# 'date', 'open', 'high', 'low', 'close'
# day9_data.set_index('date')
#串聯
concat_days = pd.concat([day9_data, day10_data], join='inner')

#找出open小於close的資料
concat_days = concat_days.set_index('date')
concat_days[concat_days.close>concat_days.open]
