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

def global_threshold(gray,T):
    out = gray.copy()
    out[gray>T]=1
    out[gray<=T]=0
    return out

def find_otsu(gray,L):
    hist = histCalc(gray,L)
    total = gray.size
    index = np.array(range(0,L),dtype=np.uint8())
    found_T = 0
    otsu = 0
    for T in range(L):
        g0 = sum(hist[:T+1])
        g1 = sum(hist[T+1:])
        w0 = g0/total
        w1 = 1-w0        
        m0 = sum(index[:T+1]*hist[:T+1])/(g0+10e-8)
        m1 = sum(index[T+1:]*hist[T+1:])/(g1+10e-8)
        res = w0*w1*(m1-m0)*(m1-m0)
        if res > otsu:
            otsu = res
            found_T = T
    return found_T

gray = np.array([[4,5,7,3],
                 [7,11,5,8],
                 [4,9,10,6],
                 [3,8,7,11]])
L=16   
print(find_otsu(gray,L))
    

# # print("Global thresholding:", global_threshold(gray, 0.01))
# otsu = find_otsu(gray, L)
# print("Otsu thresholding:", otsu) # thay ra 6?
# print(global_threshold(gray, otsu))