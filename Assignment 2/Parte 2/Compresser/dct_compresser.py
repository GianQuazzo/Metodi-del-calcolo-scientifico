import numpy as np
from scipy.fftpack import fft, dct, idct

"""
dct2 calcolata applicando la dct prima per righe poi per colonne
"""
def dct2(M):
    return dct(dct(M, axis=0, norm='ortho'), axis=1, norm='ortho')

"""
idct2 calcolata applicando la idct prima per righe poi per colonne
"""
def idct2(M):
    return idct(idct(M, axis=0, norm='ortho'), axis=1, norm='ortho')

"""
Fixa i valori che eccedono dal range [0, 255]
x < 0 : x = 0
x > 255 : x = 255
"""
def cut_excesses(X):
    X_shape = np.shape(X)
    for i in range(X_shape[0]):
        for j in range(X_shape[1]):
            if X[i][j] < 0:
                X[i][j] = 0
            elif X[i][j] > 255:
                X[i][j] = 255
    return X

"""
Ritaglia la matrice rendendo le dimesnioni multiple di k
"""
def resize_matrix(X, k):
    X_shape = np.shape(X)
    n = X_shape[0] - (X_shape[0] % k)
    m = X_shape[1] - (X_shape[1] % k)
    resized_X = np.zeros((n,m))
    resized_X = X[:n,:m]
    return resized_X

"""
Salva solo gli elementi della matrice X che si trovano al di sopra dell' antidiagonale
identificata da d; i restanti elementi sono posti a zero
"""
def cut_freq(X, d):
    X_shape = np.shape(X)
    tmp = np.zeros(np.shape(X))
    for i in range(X_shape[0]):
        for j in range(X_shape[1]):
            if i + j < d:
                tmp[i][j] = X[i][j]
    return tmp

"""
Esegue l'algoritmo di compressione lavorando su blocchi fxf dell'immagine, scartando
gli avanzi

Input: 
    - M: matrice dell'immagine da comprimere
    - f: dimensione finestra di lavoro (o dei macroblocchi)
    - d: soglia di taglio delle frequenze
"""
def compress(M, f, d):
    M = resize_matrix(M, f)
    M_shape = np.shape(M)
    C = np.zeros(M_shape)
    C_t = np.zeros(M_shape)
    M_t = np.zeros(M_shape)

    # Calcolo della dct2 a blocchi fxf
    for i in range(0, M_shape[0], f):
        for j in range(0, M_shape[1], f):
            C[i:i+f, j:j+f] = dct2(M[i:i+f, j:j+f])
            C_t[i:i+f, j:j+f] = cut_freq(C[i:i+f, j:j+f], d)
            M_t[i:i+f, j:j+f] = idct2(C_t[i:i+f, j:j+f]).astype(int)
    
    M_t = cut_excesses(M_t)

    return M_t