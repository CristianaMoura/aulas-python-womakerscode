import numpy as np



# Array 3d - bidimensional e multidimensional

arr1_2d = np.array([[1, 2], [3, 4]])
print(arr1_2d)
print("----------------------------------")
arr2_2d = np.array([[5, 6], [7, 8]])
print(arr2_2d)
print("----------------------------------")
arr3_2d = np.array([[9, 2], [3, 4]])
print(arr3_2d)

print("----------------------------------")

print("----------------------------------")

arr_3d = np.array([arr1_2d, arr2_2d, arr3_2d])
print(arr_3d)

print('-----soma de arrays----------------------------------------------------------\n')

#exercicio 1
a57 = np.random.random((5,7))
a57 = a57.flatten()
print(a57)
print("---ex1---------------------------------------------------")

#exercicio 2
bingo = np.random.randint(1, 31, size =(10, 4, 3))
print(bingo)
('--ex2-------------------------------------------------------------\n')
#exercicio3
bingo1 = bingo.reshape((5,4,6))
print(bingo1)
print('--ex3-------------------------------------------------------------\n')
