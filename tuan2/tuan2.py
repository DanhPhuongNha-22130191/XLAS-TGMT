import numpy as np
import cv2

def read_img(path):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('Image is None')
        return
    return img

def linear_transformation(img,alpha,beta):
    img_float = img.astype(np.float32)
    new_img= alpha*img_float+beta
    new_img = np.clip(new_img,0,255).astype(np.uint8)
    return new_img

def gamma_transformation(img,gamma):
    gimg = img.astype(np.float32)/255
    gimg = np.pow(gimg,float(gamma))*255
    gimg = np.clip(gimg,0,255).astype(np.uint8)
    return gimg
    
def contrast_stretching(img):
   img_f = img.astype(np.float32)
   img_max = np.max(img_f)
   img_min = np.min(img_f)
   if img_max == img_min:
    return img
   new_img = (256-1)*((img_f-img_min)/(img_max-img_min))
   return new_img.astype(np.uint8)

def main():
    path = r'tuan2\\black-white.png'
    img = read_img(path)
    new_img= linear_transformation(img,1.05,-2)
    cv2.imshow('Original image',img)
    cv2.imshow('New image',new_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()