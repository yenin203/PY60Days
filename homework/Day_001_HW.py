# -*- coding: utf-8
import numpy as np
sNum = 0
eNum = 20
multi = 3
#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
answer1 = np.arange(sNum, eNum - sNum + 1) #整數等差1
#2.呈上題，將以上數列取出偶數。
answer2 = answer1[sNum:eNum - sNum + 1:2]
#3.呈1題，將數列取出3的倍數。
answer3 = answer1[multi:eNum - sNum + 1:multi]

print(answer1)
print(answer2)
print(answer3)