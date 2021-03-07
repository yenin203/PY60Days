import numpy as np
array1 = np.array([[10, 8], [3, 5]])

# 運用上列array計算反矩陣，乘上原矩陣，並觀察是否為單位矩陣?
inv_arr = np.linalg.inv(array1)
outer_arr = array1 @ inv_arr
isIdentity = len(outer_arr[0]) == np.trace(outer_arr)
isIdentity

# 運用上列array計算特徵值、特徵向量?
eigenvalues, eigenvectors = np.linalg.eig(array1)
eigenvalues
eigenvectors
# 運用上列array計算SVD?
u, s, vh = np.linalg.svd(array1)
u
s
vh