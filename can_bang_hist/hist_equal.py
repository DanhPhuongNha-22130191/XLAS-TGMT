import numpy as np
import cv2

def calc_hist(gray,L):
    hist = np.zeros((L,),dtype=np.float32)
    M,N = gray.shape
    for i in range(M):
        for j in range(N):
            g = gray[i,j]
            hist[g]+=1
    hist/=gray.size
    return hist

def calc_cdf(gray,L):
    hist = calc_hist(gray,L)
    cdf = np.zeros((L,),dtype=np.float32)
    cdf[0] = hist[0]
    for k in range(1,L):
        cdf[k] = cdf[k-1]+hist[k]
    return cdf

def hist_equal(gray,L):
    hist = calc_hist(gray,L)
    M,N = gray.shape
    c_k = calc_cdf(gray,L)
    c_min = np.min(c_k[c_k>0])
    new = np.zeros_like(gray,dtype=np.uint8)
    for row in range(M):
        for col in range(N):
            r = gray[row,col]
            s_k = np.round(((c_k[r]-c_min)/(1-c_min))*(L-1))
            new[row,col]= np.uint8(s_k)
    return new

gray = np.array([
    [12,  4, 16,  8, 10, 14, 16, 10],
    [12,  4, 16,  8, 10, 14, 16, 10],
    [ 4, 16, 10,  8, 16, 14, 16, 10],
    [ 4, 10, 10,  4, 16, 14, 10,  4],
    [ 4, 10, 16,  4, 10, 10, 10,  4],
    [12,  4, 16,  4, 10, 10, 16, 16],
    [12,  4, 10,  8, 10,  4, 16, 12],
    [12,  4, 10,  8, 10,  4, 16, 12]
])

L= 256

print(hist_equal(gray,L))