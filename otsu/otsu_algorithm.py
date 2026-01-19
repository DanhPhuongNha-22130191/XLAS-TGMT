import numpy as np
import cv2

def histCalc(gray,L):
    hist = np.zeros((L,),dtype=np.uint8)
    N,M = gray.shape
    for row in range(N):
        for col in range(M):
            g = gray[row,col]
            hist[g]+=1
    return hist

def find_otsu(gray, L):
    hist = histCalc(gray,L)
    found_T = 0
    otsu = 0
    total = gray.size
    index = np.array(range(0,L),dtype=np.uint8)
    for T in range(L):
        w0 = sum(hist[:T+1])/total
        w1 = 1 - w0
        m0 = sum(index[:T+1]*hist[:T+1])/(sum(hist[:T+1])+10e-8)
        m1 = sum(index[T+1:]*hist[T+1:])/(sum(hist[T+1:])+10e-8)
        var = w0*w1*(m0-m1)*(m0-m1)
        if var > otsu:
            otsu = var
            found_T = T
    return found_T

def global_threshold(gray,T):
    out = gray.copy()
    out[gray>T]=1
    out[gray<=T]=0
    return out

# gray = np.array([[4,5,7,3],[7,11,5,8],[4,9,10,6],[3,8,7,11]])
gray = np.array([
    [5, 11,  6, 11, 4],
    [6,  4, 13,  7, 5],
    [7, 11,  4,  3, 9],
    [9, 13,  5, 11, 4],
    [3,  6,  9,  4, 7]
])
L=25
# # print("Global thresholding:", global_threshold(gray, 0.01))
print("Otsu thresholding:", find_otsu(gray, L)) # thay ra 6?
# # print(global_threshold(gray, findOtsu(gray, L)))
# print(impl_otsu(gray,L))