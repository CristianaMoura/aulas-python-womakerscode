import numpy as np



# arrv = np.random.randint(10, size = (3,2))
# print(arrv)

# arr = np.array([1,2,3]).reshape(3,1)
# print(arr)


# # arrv2 = np.array([["Peras", "Morango"]])
# # print(arrv2)

# concatena = np.concatenate((arrv, arr), axis = 1)
# apagar = np.delete(concatena, 2, axis = 0)
# print(concatena)


# acidentes = np.array([[1,3,2],
#                      [0,1,0],
#                      [2,1,4],
#                      [0,0,0],
#                      [1,1,0]])
#metodo keepdims mantem a dimensão do array
# metodo axis = 0 é a media das colunas
# metodo axis = 1 é a media das linhas
# metodo cumsum é a soma acumulada
# metodo cumprod é o produto acumulado
# metodo sum é a soma
# metodo prod é o produto
# metodo mean é a media
#
#print(acidentes.mean(axis=0, keepdims=True))  
#print(acidentes.mean(axis=1, keepdims=True)) 


cartela_bingo = np.array([[16, 10,  3, 15],
                           [14, 23, 17, 27],
                           [ 6, 19,  3,  1],
                           [10,  4, 18, 19]])

cartela_bingo1 = cartela_bingo[0:3]
#print(cartela_bingo1)

print("------------------------------------")
cartela_bingo2 =cartela_bingo[-1:]
#print(cartela_bingo2) 

juntar = np.concatenate((cartela_bingo1, cartela_bingo2))
print(juntar)
