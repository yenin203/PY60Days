import numpy as np
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

mean = np.nanmean
npmax = np.nanmax
npmin = np.nanmin
std = np.nanstd
# print(np.vstack((english_score, math_score, chinese_score)))
#1. 請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?
# print('請計算各科成績平均、最大值、最小值、標準差，其中數學缺一筆資料可忽略?')
def scoreInfo():
    englishInfo = np.hstack((mean(english_score), npmax(english_score),npmin(english_score),std(english_score)))
    mathInfo = np.hstack((mean(math_score), npmax(math_score),npmin(math_score),std(math_score)))
    chineseInfo = np.hstack((mean(chinese_score), npmax(chinese_score),npmin(chinese_score), std(chinese_score)))
    print(englishInfo)
    print(mathInfo)
    print(chineseInfo)
scoreInfo()
#2. 第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?
# print('第五位同學補考數學後成績為55，請計算補考後數學成績平均、最大值、最小值、標準差?')
math_score[5 - 1] = 55
scoreInfo()
#3. 用補考後資料找出與國文成績相關係數最高的學科?
np.maximum(np.corrcoef(chinese_score, english_score, rowvar = True), np.corrcoef(chinese_score, math_score, rowvar = True))