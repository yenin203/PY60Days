import pandas as pd
import numpy as np
CSV_FILE = 'boston_day12.csv'
#1.畫出箱型圖，並判斷哪個欄位的中位數在300~400之間?
csv_data = pd.read_csv(CSV_FILE)
df = pd.DataFrame(csv_data)
df.boxplot()
#TAX 與 B
#2. 畫出散佈圖 x='NOX', y='DIS' ，並說明這兩欄位有什麼關係?
df.plot.scatter(x='NOX', y='DIS')
#反比