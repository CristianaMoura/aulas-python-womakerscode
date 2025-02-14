import numpy as np

# vetorização

# arr = np.array([[1,2], [4,5]])

# for linha in range(0, arr.shape[0]):
#     for coluna in range(0, arr.shape[1]):
#         arr[linha][coluna]+= 1
#arr+=1
# arr +1
#print(arr)

# sintax numpy
# operacao booleana
# a = np.array([[1,2,3], [4,5,6]])
# aa = a > 3
# print(aa)

# vetorizando codigo python(np.vectorize)

# arra = np.array([["hello", "meninas", "coders"]])
# vec= len(arra) > 5
# print(vec)

# vetorizar_len = np.vectorize(len)
# vetorizar = vetorizar_len(arra) > 5
# print(vetorizar)

# def minha_funcao(x):
#     return x **2 +3*x + 1
# vetorizada_funcao = np.vectorize(minha_funcao)

# array_original = np.array([1,2,3,4,5])

# resultado = vetorizada_funcao(array_original)

# print([resultado])

# salvando
arr10 = np.arange(10).reshape(2,5)
print(arr10)
np.save('arr10.csv', arr10)

# carregando
arr10 = ([[0,1,2,3,4,], [5,6,7,8,9]])

arr = np.load('arr10.csv')
print(arr)


