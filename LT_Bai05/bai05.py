import cv2 as cv
import numpy as np

def fft(gray):
    F = np.fft.fft2(gray)
    Fshift = np.fft.fftshift(F)
    


img = cv.imread(r'LT_Bai05\\moon.png', cv.IMREAD_GRAYSCALE)

