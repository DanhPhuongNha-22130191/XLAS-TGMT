import numpy as np
import cv2

def convolution(gray,kernel):
   out = np.zeros_like(gray,float)
   ksize = kernel.shape[0]
   pad = ksize//2
   padded = np.pad(gray,pad)
   N,M = gray.shape
   for row in range(N):
    for col in range(M):
     sub = padded[row:row+ksize,col:col+ksize]
     out[row,col] = np.sum(sub*kernel)
   return np.clip(out,0,255).astype(np.uint8)

gray = np.array([
    [12,  4, 16,  8, 10, 14, 16, 10],
    [12,  4, 16,  8, 10, 14, 16, 10],
    [ 4, 16, 10,  8, 16, 14, 16, 10],
    [ 4, 10, 10,  4, 16, 14, 10,  4],
    [ 4, 10, 16,  4, 10, 10, 10,  4],
    [12,  4, 16,  4, 10, 10, 16, 16],
    [12,  4, 10,  8, 10,  4, 16, 12],
    [12,  4, 10,  8, 10,  4, 16, 12],
])
kernel = np.ones((3,3))
print(convolution(gray, kernel))