import numpy as np
import cv2


# =========================
# Histogram calculation
# =========================
def histCalc(gray, L):
    """
    Tính histogram ảnh xám
    """
    hist = np.zeros(L, dtype=np.int32)
    N, M = gray.shape

    for i in range(N):
        for j in range(M):
            g = gray[i, j]
            hist[g] += 1

    return hist


# =========================
# Global thresholding
# =========================
def global_threshold(gray, T):
    """
    Nhị phân hóa ảnh theo ngưỡng T
    """
    out = np.zeros_like(gray, dtype=np.uint8)
    out[gray > T] = 1
    return out


# =========================
# Otsu threshold
# =========================
def find_otsu(gray, L=256):
    """
    Tìm ngưỡng Otsu
    """
    hist = histCalc(gray, L)
    total = gray.size

    index = np.arange(L, dtype=np.int32)

    max_var = -1.0
    best_T = 0

    for T in range(1, L - 1):
        g0 = hist[:T + 1].sum()
        g1 = hist[T + 1:].sum()

        if g0 == 0 or g1 == 0:
            continue

        w0 = g0 / total
        w1 = g1 / total

        m0 = (index[:T + 1] * hist[:T + 1]).sum() / g0
        m1 = (index[T + 1:] * hist[T + 1:]).sum() / g1

        var_between = w0 * w1 * (m1 - m0) ** 2

        if var_between > max_var:
            max_var = var_between
            best_T = T

    return best_T


# =========================
# Read image
# =========================
def read_img(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError("Cannot read image")
    return img


# =========================
# Run Otsu
# =========================
def impl_otsu(gray):
    T = find_otsu(gray, 256)
    print("Otsu threshold:", T)

    result = global_threshold(gray, T)

    cv2.imshow("Original", gray)
    cv2.imshow("Otsu Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# =========================
# TEST
# =========================
if __name__ == "__main__":

    # Test với ma trận nhỏ
    gray_test = np.array([
        [4, 5, 7, 3],
        [7, 11, 5, 8],
        [4, 9, 10, 6],
        [3, 8, 7, 11]
    ], dtype=np.uint8)

    T_test = find_otsu(gray_test, 16)
    print("Otsu threshold (test matrix):", T_test)
    print(global_threshold(gray_test, T_test))

    # Test với ảnh thật
    path = r"otsu/Untitled Diagram.drawio (1).png"
    img = read_img(path)
    impl_otsu(img)
