# THỰC HÀNH: TỰ CÀI ĐẶT THUẬT TOÁN CẮT NGƯỠNG TOÀN CỤC (ITERATIVE)

## 1. Mục tiêu bài học
- Hiểu rõ cơ chế tìm ngưỡng tự động bằng **phương pháp lặp**.
- Làm quen với việc **xử lý mảng** và **tính toán thống kê (Mean)** trên ảnh mức xám.
- Xây dựng chương trình **phân đoạn ảnh (Image Segmentation)** cơ bản.

---

## 2. Mô tả thuật toán
Thuật toán tìm **ngưỡng toàn cục** cơ bản dựa trên nguyên tắc **giảm dần sai số giữa các vùng cường độ sáng**.

---

## 3. Nguyên lý hoạt động

### Bước 1: Khởi tạo
Tính giá trị trung bình mức xám của toàn bộ ảnh và chọn làm ngưỡng ban đầu:

$$
T_0 = \operatorname{mean}(I)
$$

---

### Bước 2: Phân đoạn ảnh (lặp)
Chia ảnh thành hai nhóm pixel:
- $G_1$: các pixel có giá trị mức xám **lớn hơn** $T_0$
- $G_2$: các pixel có giá trị mức xám **nhỏ hơn hoặc bằng** $T_0$

Tính giá trị trung bình mức xám của mỗi nhóm:
- $m_1 = \operatorname{mean}(G_1)$
- $m_2 = \operatorname{mean}(G_2)$

---

### Bước 3: Cập nhật ngưỡng
Ngưỡng mới được tính theo công thức:

$$
T_{new} = \frac{m_1 + m_2}{2}
$$

---

### Bước 4: Kiểm tra hội tụ
Tính độ chênh lệch giữa hai lần lặp:

$$
\Delta T = |T_{new} - T_0|
$$

- Nếu $\Delta T < \text{thres}$ (ví dụ: 0.5) thì **dừng thuật toán**
- Ngược lại, gán $T_0 = T_{new}$ và quay lại **Bước 2**

---

## 4. Yêu cầu lập trình
- Ngôn ngữ: **Python**
- Thư viện: **NumPy**
- **Không sử dụng** các hàm tìm ngưỡng tự động của OpenCV  
  (ví dụ: `cv2.threshold`, `cv2.THRESH_OTSU`)

---

## 5. Hướng tiếp cận cài đặt
- Ảnh đầu vào phải được chuyển sang **ảnh mức xám**
- Sử dụng vòng lặp `while` để thực hiện thuật toán
- Cần xử lý trường hợp một nhóm không có pixel
- Giới hạn số vòng lặp để tránh lặp vô hạn

---

## 6. Kết quả mong đợi
- Xác định được **ngưỡng toàn cục tối ưu**
- Ảnh đầu ra là **ảnh nhị phân**
- Thuật toán hội tụ sau một số vòng lặp hữu hạn

---

## 7. Ghi chú
- Thuật toán còn được gọi là **Iterative Threshold Selection**
- Phù hợp với ảnh có **độ tương phản rõ ràng** giữa nền và đối tượng

---
