import numpy as np
import time
import mydct
from scipy.fftpack import fft, dct, idct

def prof_test():
    input = [[231, 32, 233, 161, 24, 71, 140, 245],
             [247, 40, 248, 245, 124, 204, 36, 107],
             [234, 202, 245, 167, 9, 217, 239, 173],
             [193, 190, 100, 167, 43, 180, 8, 70],
             [11, 24, 210, 177, 81, 243, 8, 112],
             [97, 195, 203, 47, 125, 114, 165, 181],
             [193, 70, 174, 167, 41, 30, 127, 245],
             [87, 149, 57, 192, 65, 129, 178, 228]]

    C = mydct.dct2(input)
    print(C)
    #C_lib = dct(dct(input, axis=0, norm='ortho'), axis=1, norm='ortho')
    #print(C_lib)

def prof_test_row():
    input = [231, 32, 233, 161, 24, 71, 140, 245]

    c = dct(input, norm='ortho')
    print(c)

def big_random_comparison(n, m):
    big_input = np.random.randint(255, size=(n, m))
    start = time.time()
    C_my = mydct.dct2(big_input)
    end = time.time()
    #print(C_my)
    print(f"Tempo di esecuzione per mydct.dct2: {end-start}")
    start = time.time()
    C_lib = dct(dct(big_input, axis=0, norm='ortho'), axis=1, norm='ortho')
    end = time.time()
    #rint(C_lib)
    print(f"Tempo di esecuzione per scipy.fft.dct: {end-start}")


print("========================================================")
print("=============big_random_comparison (100x100)============")
big_random_comparison(100, 100)
print("========================================================")
print("========================prof_test=======================")
prof_test()
#prof_test_row()