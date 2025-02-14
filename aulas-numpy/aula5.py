import numpy as np


##FANCY INDEXING E NP.WHERE()

#pessoas_id_idade = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])

#print(pessoas_id_idade)


# quais dos valores são divisiveis por 2
# maskk = np.where(pessoas_id_idade[:,1] % 2 == 0)
# print(pessoas_id_idade[maskk])


# arr1 = np.array([1, 2, 3, 4, 5])
# mask = arr1 % 2 == 0
# print(mask)
# print(arr1[mask])

# cartela_bingo = np.array([[16, 10,  3, 15],
#        [14, 23, 17, 27],
#        [ 6, 19,  3,  1],
#        [10,  4, 18, 19]])

# maska = np.where(cartela_bingo % 3 == 0)
# print(maska)

##BUSCAR E SUBSTITUIR 

# cartela_bingo = np.array([[16, 10,  3, 15],
#        [14, 23, 17, 27],
#        [ 6, 19,  3,  1],
#        [10,  4, 18, 19]])


# maskara = np.where(cartela_bingo % 3 == 0, "", cartela_bingo )
# print(maskara.dtype)

#pessoas_id_idade = np.array([[1, 22], [2, 21], [3, 27], [4, 26]])
#print(pessoas_id_idade)
#mascara = pessoas_id_idade[:, 1] > 21
#print(pessoas_id_idade[mascara])

#print(np.where(mascara))

# mascara = np.where(pessoas_id_idade % 3 == 0, "div3", pessoas_id_idade )
# mascara = np.where(pessoas_id_idade >= 21  , "maior ", pessoas_id_idade )
# print(mascara)

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


#maior_especie = especies[:, 3] == 22
#print(especies[maior_especie])



# mask_297 = especies[:, 0] ==297
# print(especies[mask_297])
# print("-------------------------------------------------")

# especie105 = np.where(especies[:,1] == 105 )
# print([especie105])

especies_profunda = np.where(especies[:,2] > 60, "profundo", especies [:, 2])
print([especies_profunda])





    