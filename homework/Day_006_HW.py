import numpy as np
#. 將下兩列array存成npz檔
array1 = np.array(range(30))
array2 = np.array([2,3,5])
filename = 'multi_array.npz'

with open(filename, 'wb') as f:
    np.savez(f, array1, array2)

# #2. 讀取剛剛的npz檔，加入下列array一起存成新的npz檔
array3 = np.array([[4,5,6], [1,2,3]])
reshapearr3 = array3.reshape((1, array3.size))
npzFile = np.load(filename)
data = [npzFile[key] for key in npzFile]
data.append(reshapearr3)
with open(filename, 'wb') as f:
    np.savez(f, *data)

npzFile = np.load(filename)
print(npzFile['arr_2'])