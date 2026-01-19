import numpy as np
import cv2

def global_threshold(gray,T):
    out = gray.copy()
    out[gray>T] = 1
    out[gray<=T] = 0
    return out

def calc_hist(gray,L):
    hist = np.zeros((L,),dtype=np.uint8)
    M,N = gray.shape
    for i in range(M):
        for j in range(N):
            hist[gray[i,j]]+=1
    return hist

def find_otsu(gray,L):
    hist = calc_hist(gray,L)
    otsu = 0
    found_T = 0
    total = gray.size
    index = np.array(range(0,L),dtype = np.uint8)
    for T in range(L):
        g0 = sum(hist[:T+1])
        g1 = sum(hist[T+1:])
        w0 = g0 / total
        w1 = 1 - w0
        m0 = sum((index[:T+1]*hist[:T+1]))/(g0+10e-8)
        m1 = sum((index[T+1:]*hist[T+1:]))/(g1+10e-8)
        var = w0*w1*(m0-m1)*(m0-m1)
        print(f"T = {T:2d} | var = {var:.6f}")

        if var > otsu:
            otsu = var
            found_T = T
    return found_T

gray = np.array([
    [5, 11,  6, 11, 4],
    [6,  4, 13,  7, 5],
    [7, 11,  4,  3, 9],
    [9, 13,  5, 11, 4],
    [3,  6,  9,  4, 7]
])
L=25
print("Otsu thresholding:", find_otsu(gray, L))