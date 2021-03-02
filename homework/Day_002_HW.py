import numpy as np
#1.將下列清單(list1)，轉成維度為(5X6)的array，順序按列填充。(hint:order="F")
array1 = np.array(range(30))
answer1 = array1.reshape((5,6), order = 'F')
answer2 = np.where(answer1 % 6 == 1)
print(answer1)
print(answer2)