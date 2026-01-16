import numpy as np
import cv2 

def read_img(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print('Image is None')
        return
    return img

def iterative_golabal_threshold(img, thres=0.5, max_iter=100):
    img = img.astype(np.float32)
    T0 = img.mean()
    for _ in range(max_iter):
        G1 = img[img > T0]
        G2 = img[img <= T0]
        if len(G1) == 0 or len(G2) == 0:
            break
        m1 = G1.mean()
        m2 = G2.mean()
        T_new = (m1 + m2)/2
        if abs(T_new - T0) < thres:
            break

        T0 = T_new
    print("T0:", T0)
    print("m1:", m1, "m2:", m2)
    return T0

def apply_global_threshold(img,T):
    bin = np.zeros_like(img, dtype=np.uint8)
    bin[img > T] = 255
    return bin

def histogram(gray,L):
    hist = np.zeros(L,dtype=np.float32)
    N,M = gray.shape
    for row in range(N):
        for col in range(M):
            g = gray[row,col]
            hist[g]+=1
    hist/=gray.size
    return hist
            
def otsu_threshold(img, L=256):
    img = img.astype(np.uint8)

    p = histogram(img, L)

    # μ_T
    mu_T = 0
    for i in range(L):
        mu_T += i * p[i]

    max_sigma = -1
    best_t = 0

    for t in range(L):
        w0 = 0
        for i in range(t + 1):
            w0 += p[i]

        if w0 == 0 or w0 == 1:
            continue

        mu0 = 0
        for i in range(t + 1):
            mu0 += i * p[i]
        mu0 /= w0

        w1 = 1 - w0
        mu1 = (mu_T - w0 * mu0) / w1

        sigma_b2 = w0 * w1 * (mu0 - mu1) ** 2

        if sigma_b2 > max_sigma:
            max_sigma = sigma_b2
            best_t = t

    return best_t
   
def main():
    path = r"LT_Bai08\\Untitled Diagram.drawio.png"
    img = read_img(path)
    gray = np.array([[4,5,7,3],[7,11,5,8],[4,9,10,6],[3,8,7,11]])

    threshold_otsu = otsu_threshold(gray, 256)
    print(threshold_otsu)
    # cv2.imshow("Gray Image", img)
    # cv2.imshow("Otsu Image", threshold_otsu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
  
main()