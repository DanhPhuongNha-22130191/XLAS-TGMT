import numpy as np
import cv2

def hog(gray, row, col, ksize):
    bin_weight = 180 / 9
    bins = np.zeros(9)

    for i in range(row, row + ksize):
        for j in range(col, col + ksize):
            gx = gray[i, j+1] - gray[i, j-1]
            gy = gray[i+1, j] - gray[i-1, j]

            mag = np.sqrt(gx*gx + gy*gy)

            angle = np.arctan2(gy, gx) * 180 / np.pi
            if angle < 0:
                angle += 180

            bin_idx = angle / bin_weight
            left = int(bin_idx) % 9
            right = (left + 1) % 9

            r_weight = bin_idx - left
            l_weight = 1 - r_weight

            bins[left] += l_weight * mag
            bins[right] += r_weight * mag

    return bins


gray = np.array([[10,20,30,40,50,60,70],
                 [10,40,40,60,60,80,80],
                 [10,60,50,80,70,100,90],
                 [10,80,60,100,80,120,100],
                 [10,100,70,120,90,140,110],
                 [10,120,80,140,100,160,120]])
print(hog(gray, 1,2,3))
            