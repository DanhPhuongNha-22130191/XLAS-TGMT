import numpy as np
import cv2 

def harmonic(gray,ksize):
    M,N = gray.shape
    pad_count = ksize//2
    padded = np.pad(gray,pad_count,mode='edge')+10e-8
    out = np.zeros(gray.shape,dtype=np.float32)
    for row in range(M):
        for col in range(N):
            sub = padded[row:row+ksize,col:col+ksize]
            A = ksize*ksize
            B = np.sum(1/sub)
            out[row,col]=A/B
    return np.clip(out,0,255).astype(np.uint8)

def cotraharmonic(gray,ksize,Q):
    M,N = gray.shape
    pad_count = ksize//2
    padded = np.pad(gray,pad_count,mode='edge')+10e-8
    out = np.zeros(gray.shape,dtype=np.float32)
    for row in range(M):
        for col in range(N):
            sub = padded[row:row+ksize,col:col+ksize]
            A = np.sum(sub**(Q+1))
            B = np.sum(sub**Q)
            out[row,col]=A/B
    return np.clip(out,0,255).astype(np.uint8)