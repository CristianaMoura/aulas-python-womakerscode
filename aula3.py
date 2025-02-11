import numpy as np

## Conversão e Coerção

# dtype como argumento

# tipo float - mesmo que a maioria seja int tendo um float ele sempre será float
arr = np.array([2.0, 3.6, 8.9 ]).dtype
print(arr)

# tipo inteiro
arr_1 = np.array([3, 4, 7, 9, ]).dtype
print(arr_1)

# tipo string- sempre conta a string maior
arr_2 = np.array(["helo", "dia", "morango"]).dtype
print(arr_2)


arr_3 = np.array([2.56, 3.6, 8.9 ], dtype=np.float32).dtype
print(arr_3)

arr_4 = np.array([[True, False], [True, True]])
arr_4 = arr_4.astype(str)
print(arr_4)
arr_4 = np.char.mod('%s', arr_4)
print(arr_4)
print(arr_4.dtype)


