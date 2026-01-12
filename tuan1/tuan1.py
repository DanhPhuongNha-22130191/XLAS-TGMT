import numpy as np
import cv2 

def read_img(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        print('Error to read image')
        return
    return img

def img_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def get_img_info(img):
    ndim = img.ndim
    size = img.size
    dtype  = img.dtype
    shape = img.shape
    
    print(f'Số chiều của ảnh: {ndim}')
    print(f'Tổng các phần tử của ảnh: {size}')
    print(f'Kiểu dữ liệu của ảnh: {dtype}')
    print(f'Kích thước của ảnh: {shape}')

def split_color_chanels(img):
    b, g, r = cv2.split(img)
    # cv2.imshow('Blue channel', b)
    # cv2.imshow('Green channel', g)
    # cv2.imshow('Red channel', r)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return b,g,r

def merge_color_chanels(b,g,r):
    img = cv2.merge([b,g,r])
    img_show('Imge merge',img)

def convert_bgr_to_hsv(img):
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img_show('HSV image',hsv_img)
    return img

def create_new_black_img(img):
    black_img = np.zeros((400,400,3), dtype=np.uint8)
    # img_show('Black image',black_img)
    return black_img

def create_circle(img,center,radius,color):
    new_img = cv2.circle(img,center,radius,color,thickness=2)
    img_show('New image',new_img)
    return new_img

def image_negative(img,L):
    return L-img

def covertToBin(img,threshold):
    return (img > threshold).astype(np.uint8)*255

path = r'tuan1\\model-surprise.png'
img = read_img(path)
# img_show(read_img(path))
# get_img_info(read_img(path))
# split_color_chanels(read_img(path))
# img = read_img(path)
# b, g, r = split_color_chanels(img)
# merge_color_chanels(b, g, r)
# hsv = convert_bgr_to_hsv(read_img(path))
# get_img_info(hsv)
# black = create_new_black_img(read_img(path))
# print(black.shape)
# create_circle(black,(200,200),50,(0,255,255))
# img_show('Original',img)
# img_show('Image negative', image_negative(img,255))
img_show('Thresholding', covertToBin(img,127))