import numpy as np


def tabulation(s1, s2):
    table = np.zeros((len(s1)+1, len(s2)+1))
    result = 0
    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if i == 0 or j == 0:
                table[i+1][j+1] = 0
            elif s1[i] == s2[j]:
                table[i+1][j+1] = table[i][j] + 1
                result = max(result, table[i+1][j+1])
            else:
                table[i+1][j+1] = 0
    # Coversión a Int para evitar que devuelva un resultado.0
    return int(result)
