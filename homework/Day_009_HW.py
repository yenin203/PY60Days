
import pandas as pd

#讀取資料夾中boston.csv讀取其欄位CHAS、NOX、RM，輸出成.xlsx檔案
prefix = 'boston'
csv_extension = '.csv'
excel_extension = '.xlsx'
csv_data = pd.read_csv(prefix + csv_extension, usecols =['CHAS','NOX','RM'])
csv_data.to_excel(prefix + excel_extension, sheet_name = prefix)
csv_data