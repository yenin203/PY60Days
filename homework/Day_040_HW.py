# pip install pingouin
# pip install researchpy 
# 在鐵達尼資料集中，今天我們專注觀察變數之間的相關性，以 Titanic_train.csv 中，首先將有遺失值的數值刪除，並回答下列問題。
# import library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import math
import statistics
import seaborn as sns
from IPython.display import display

import pingouin as pg
import researchpy   
df_train = pd.read_csv("Titanic_train.csv")
print(df_train.head(5))
## 這邊我們做一個調整，把 Survived 變成離散型變數 Survived_cate
df_train['Survived_cate'] = df_train['Survived'].astype('object')
print("在一定區間內可以任意取值的變數叫連續變數,其數值是連續不斷的,相鄰兩個數值可作無限分割,即可取無限個數值.例如,生產零件的規格尺寸,人體測量的身高,體重,胸圍等為連續變數,其數值只能用測量或計量的方法取得.")
print("反之,其數值只能用自然數或整數單位計算的則為離散變數例如,企業個數,職工人數,設備台數等,只能按計量單位數計數,這種變數的數值一般用計數方法取得")
## 寫一個副程式判斷相關性的強度
def judgment_CramerV(df,V):
    if df == 1:
        if V < 0.10:
            qual = 'Negligible 微乎其微'
        elif V < 0.30:
            qual = 'Small 小有關聯'
        elif V < 0.50:
            qual = 'Medium 有關係但影響不大'
        else:
            qual = 'Large 非常相關'
    elif df == 2:
        if V < 0.07:
            qual = 'Negligible 微乎其微'
        elif V < 0.21:
            qual = 'Small 小有關聯'
        elif V < 0.35:
            qual = 'Medium 有關係但影響不大'
        else:
            qual = 'Large 非常相關'
    elif df == 3:
        if V < 0.06:
            qual = 'Negligible 微乎其微'
        elif V < 0.17:
            qual = 'Small 小有關聯'
        elif V < 0.29:
            qual = 'Medium 有關係但影響不大'
        else:
            qual = 'Large 非常相關'
    elif df == 4:
        if V < 0.05:
            qual = 'Negligible 微乎其微'
        elif V < 0.15:
            qual = 'Small 小有關聯'
        elif V < 0.25:
            qual = 'Medium 有關係但影響不大'
        else:
            qual = 'Large 非常相關'
    else:
        if V < 0.05:
            qual = 'Negligible 微乎其微'
        elif V < 0.13:
            qual = 'Small 小有關聯'
        elif V < 0.22:
            qual = 'Medium 有關係但影響不大'
        else:
            qual = 'Large 非常相關'
    return(qual)

def valiate_etaSq(etaSq):
    if etaSq < .01:
        qual = 'Negligible 微乎其微'
    elif etaSq <.06:
        qual = 'Small 小有關聯'
    elif etaSq <.14:
        qual = 'Medium 有關係但影響不大'
    else:
        qual = 'Large 非常相關'
    return qual
    
dv = "Age"
between = "Survived_cate"
aov = pg.anova(dv=dv,  between=between, data=df_train, detailed=True)
etaSq = aov.SS[0] / (aov.SS[0]+aov.SS[1])
print("Q1: 透過數值法計算 Age 和 Survived 是否有相關性? A:連續與離散")
print("Eta Squared (η2)結果：%.3f 相關性 %s" % (etaSq, valiate_etaSq(etaSq)))
# print("Cramer's Values 結果 ", res.loc[2, 'results'], valiate_etaSq(res.loc[2, 'results']))
dt = 'Survived_cate'
between = 'Sex'
# step1: 用交叉列連表(contingency table)，來整理兩個類別型的資料
contTable = pd.crosstab(df_train[between], df_train[dt])
df = min(contTable.shape[0], contTable.shape[1]) - 1
crosstab, res = researchpy.crosstab(df_train[between], df_train[dt], test='chi-square')
print()
print("Q2:透過數值法計算 Sex 和 Survived 是否有相關性? A:離散與離散")
print("Cramer's 相關性%.3f 結果 %s" % (res.loc[2,'results'], judgment_CramerV(df,res.loc[2,'results'])))
print()
# 連續與連續 Pearson
def judgment_PearsonV(corr):
    if corr < .1:
        qual = "無線性相關"
    elif corr <.4:
        qual = "低度線性相關"
    elif corr <.7:
        qual = "中度線性相關"
    elif corr < 1:
        qual = "高度線性相關"
    else:
        qual = "完全線性相關"
    return qual
dt = "Age"
between = "Fare"
# print(df_train.isnull().any()) # 檢測
df_not_age_null = df_train.loc[df_train[dt].notnull(), (dt,between)]
corr, _ = stats.pearsonr(df_not_age_null[dt],df_not_age_null[between])
print("Q3: 透過數值法計算 Age 和 Fare 是否有相關性? A:連續與連續")
print("Pearson 相關性%.3f 結果 %s" % (corr, judgment_PearsonV(corr)))