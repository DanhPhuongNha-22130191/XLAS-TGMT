import numpy as np
import cv2

def histCalc(gray,L):
   hist = np.zeros(L,dtype=np.float32)
   N,M = gray.shape
   for row in range(N):
       for col in range(M):
           g = gray[row,col]
           if 0<=g<L:
            hist[g]+=1
   hist/=gray.size
   return hist

def histEqual(gray, L):
    hist = histCalc(gray,L)
    e_hist = np.zeros_like(hist)
    for g in range(L):
        e_hist[g] = hist[:g+1].sum()
    c_max = 1
    c_min = 0
    for g in range(L):
        if e_hist[g] > 0:
            c_min = e_hist[g]
            break
    if c_max - c_min == 0:
       return gray.copy()
    else:
        coef = (L-1)/(c_max-c_min)
    e_hist = np.round((e_hist-c_min)*coef)
    e_hist = e_hist.astype(np.uint8)
    out = np.zeros_like(gray,dtype=np.uint8)
    N,M = gray.shape
    for row in range(N):
        for col in range(M):
            g = int(gray[row,col])
            out[row,col] = e_hist[g]
    return out

img = np.array([
    [12,  4, 16,  8, 10, 14, 16, 10],
    [12,  4, 16,  8, 10, 14, 16, 10],
    [ 4, 16, 10,  8, 16, 14, 16, 10],
    [ 4, 10, 10,  4, 16, 14, 10,  4],
    [ 4, 10, 16,  4, 10, 10, 10,  4],
    [12,  4, 16,  4, 10, 10, 16, 16],
    [12,  4, 10,  8, 10,  4, 16, 12],
    [12,  4, 10,  8, 10,  4, 16, 12],
])
L=256
print(histCalc(img,L))
print(histEqual(img,L))
    


    