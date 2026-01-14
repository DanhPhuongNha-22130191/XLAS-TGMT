# ĐỀ BÀI THỰC HÀNH: TỰ CÀI ĐẶT THUẬT TOÁN HÌNH THÁI HỌC (MORPHOLOGY)

## 1. Thông tin chung
* **Môn học:** Xử lý ảnh (Image Processing)
* **Chủ đề:** Biến đổi hình thái học (Morphological Transforms)
* **Yêu cầu kỹ thuật:** * Ngôn ngữ: Python (Sử dụng thư viện Numpy).
    * **Không** sử dụng các hàm có sẵn của OpenCV như `cv2.erode`, `cv2.dilate`, `cv2.morphologyEx`.
    * Áp dụng trực tiếp trên ảnh gốc (không chuyển sang ảnh nhị phân bằng hàm `cv2.threshold`).

---

## 2. Yêu cầu bài tập
Cho một ma trận ảnh xám hoặc ảnh thực tế, hãy xây dựng chương trình thực hiện các nhiệm vụ sau:

### Nhiệm vụ 1: Xây dựng hàm Phép Co (Erosion)
* **Nguyên lý:** Sử dụng một cửa sổ trượt (Kernel) kích thước $k \times k$. Tại mỗi vị trí $(x, y)$, giá trị của pixel đích sẽ là giá trị **Nhỏ nhất (MIN)** của tất cả các pixel trong vùng mà Kernel bao phủ.
* **Mục đích:** Thu hẹp các vùng sáng, mở rộng các vùng tối.



### Nhiệm vụ 2: Xây dựng hàm Phép Giãn (Dilation)
* **Nguyên lý:** Sử dụng một cửa sổ trượt (Kernel) kích thước $k \times k$. Tại mỗi vị trí $(x, y)$, giá trị của pixel đích sẽ là giá trị **Lớn nhất (MAX)** của tất cả các pixel trong vùng mà Kernel bao phủ.
* **Mục đích:** Mở rộng các vùng sáng, lấp đầy các lỗ hổng tối.



### Nhiệm vụ 3: Ứng dụng xử lý ảnh
1.  Đọc một ảnh xám từ máy tính.
2.  Tự định nghĩa kích thước Kernel (ví dụ $3 \times 3$ hoặc $5 \times 5$).
3.  Thực hiện lần lượt các phép toán đã xây dựng để khử nhiễu cho ảnh.

---


