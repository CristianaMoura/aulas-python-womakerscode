import numpy as np

l = [ 4, 8, 2, 12, 5, 8, 0]

arr = np.array(l)
print(arr)


#1 zeros
arr1 = np.zeros((2,4)) # recebe uma tupla
print(arr1)
print('-1---------------------------------------------\n')

# #2 shape
arr4 = np.zeros((2,4)) # recebe uma tupla
print(arr4.shape)
print('-2---------------------------------------------\n')

# #3 flatten
arr2 = np.zeros((2,4)) # recebe uma tupla
print(arr2.flatten())
print('-3---------------------------------------------\n')

# #4 reshape
arr3 = np.array([[3,4,2],[8,11,5]]) # recebe uma tupla
arr3.reshape((3,2))
print(arr3)
print('-4---------------------------------------------\n')

# #5 range
l = list (range(0,3))
print(l)
print('-5---------------------------------------------\n')

# #6 arange
arr_ = np.arange(1,11)
print(arr_)
print('--6-------------------------------------------\n')

# #7 randint
arr_1 = np.random.randint(60, size =(6,10))
print(arr_1)
print('--7------------------------------------------------------------\n')

#8 #np.random.random()
arr_2 = np.random.random((3,5))
print(arr_2)
print('--8-------------------------------------------------------------\n')






