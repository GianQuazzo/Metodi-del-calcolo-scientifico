import csv
import numpy as np
import math as m
from scipy.fftpack import fft, dct, idct
import mydct
import timeit

def dct2(X):
    return dct(dct(X, axis=0, norm='ortho'), axis=1, norm='ortho')

def write_csv(row_list, file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(row_list)

def log_time_mydct(X):
    start = timeit.default_timer()
    mydct.dct2(X)
    end = timeit.default_timer()
    time_passed = ((end - start) * 1000)
    return (time_passed)

def log_time_libdct2(X):
    start = timeit.default_timer()
    dct2(X)
    end = timeit.default_timer()
    time_passed = ((end - start) * 1000)
    return (time_passed)

if __name__ == "__main__":
    row_list = [["N", "Time_mydct.dct2(ms)", "Time_scipy.fft.dct(ms)"]]
    for N in range(10, 110, 10):
        X = np.random.randint(255, size=(N, N))
        time_mydct2 = log_time_mydct(X)
        time_libdct2 = log_time_libdct2(X)
        row_list.append([N, time_mydct2, time_libdct2])
    write_csv(row_list, './report.csv')