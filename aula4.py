import numpy as np


# a1 = np.array([16,10,3,15])
# a2 = np.array([14,23,17,27])
# a3 = np.array([6,19, 3,1])
# a4 = np.array([10,4,18,19])

# cartela_bingo = np.array([a1, a2,a3,a4])            
#print(cartela_bingo)

#print(cartela_bingo[1:3, 0:2])

#print(np.sort(cartela_bingo,axis=1))

#print(cartela_bingo[:,1].reshape(4,1))

#print(cartela_bingo[0])

especies = np.array([[747,  89,  33,   5],
                    [623, 123,  32,  13],
                    [501,  22,  49,   2],
                    [116, 101,  42,  10],
                    [297,  56,  69,  22],
                    [613,  64,  27,   7],
                    [295,  84,  29,  14],
                    [692, 105,  72,  16],
                    [229, 103,  35,   5],
                    [374, 124,  70,   1]])
# qtd_especies = especies[:,1]
# #print(qtd_especies.reshape(10,1))
# print(qtd_especies[0:3])

# print(especies.shape)
# print(qtd_especies[-5:])


tam_especies= np.sort(especies[:, 3])[::-1]
print(tam_especies)