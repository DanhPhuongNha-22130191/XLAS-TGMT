import numpy as np
import cv2

def read_img(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('Image is None')
        return
    return img

def erosion(img,kernel):
    row,col = img.shape
    out = np.zeros(img.shape,dtype=np.uint8)
    ksize = kernel.shape[0]
    pad = ksize//2
    padded = np.pad(img,pad)
    for i in range(row):
        for j in range(col):
            window = padded[i:i+ksize,j:j+ksize]
            if np.all(window==255):
                out[i,j]=255
            else:
                out[i,j]=0
    return out

def dilation(img,kernel):
    row,col = img.shape
    out = np.zeros(img.shape,dtype=np.uint8)
    ksize = kernel.shape[0]
    pad = ksize//2
    padded = np.pad(img,pad)
    for i in range(row):
        for j in range(col):
            window = padded[i:i+ksize,j:j+ksize]
            if np.any(window==255):
                out[i,j]=255
            else:
                out[i,j]=0
    return out

def main():
    kernel = np.ones((3,3),dtype=np.uint8)
    path = r'LT_Bai07\\salt.jpg'
    
    erosion(read_img(path),kernel)
    
    cv2.imshow('Original',read_img(path))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()