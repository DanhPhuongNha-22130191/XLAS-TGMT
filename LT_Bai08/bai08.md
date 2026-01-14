# THỰC HÀNH: TỰ CÀI ĐẶT THUẬT TOÁN CẮT NGƯỠNG TOÀN CỤC (ITERATIVE)

## 1. Mục tiêu bài học
- Hiểu cơ chế tìm ngưỡng tự động bằng phương pháp lặp.
- Thực hành xử lý mảng và tính giá trị trung bình trên ảnh mức xám.
- Xây dựng chương trình phân đoạn ảnh cơ bản.

---

## 2. Mô tả thuật toán
Thuật toán cắt ngưỡng toàn cục dựa trên việc chia ảnh thành hai vùng sáng và tối,
sau đó cập nhật ngưỡng cho đến khi hội tụ.

---

## 3. Nguyên lý hoạt động

### Bước 1: Khởi tạo
Tính giá trị trung bình mức xám của toàn bộ ảnh và chọn làm ngưỡng ban đầu:

$$
T_0 = mean(I)
$$

---

### Bước 2: Phân đoạn ảnh (lặp)
Chia ảnh thành hai nhóm pixel:
- G1: các pixel có giá trị mức xám lớn hơn T0
- G2: các pixel có giá trị mức xám nhỏ hơn hoặc bằng T0

Tính giá trị trung bình mức xám của từng nhóm:
- m1 là trung bình của G1
- m2 là trung bình của G2

---

### Bước 3: Cập nhật ngưỡng
Ngưỡng mới được tính theo công thức:

$$
T_{new} = (m_1 + m_2) / 2
$$

---

### Bước 4: Kiểm tra hội tụ
Tính độ chênh lệch giữa hai lần lặp:

$$
\Delta T = |T_{new} - T_0|
$$

- Nếu ΔT nhỏ hơn ngưỡng sai số cho trước (ví dụ 0.5) thì dừng thuật toán.
- Nếu không, gán T0 = Tnew và quay lại Bước 2.

---

## 4. Yêu cầu lập trình
- Ngôn ngữ: Python
- Thư viện: NumPy
- Không sử dụng các hàm tìm ngưỡng tự động của OpenCV.

---

## 5. Hướng tiếp cận cài đặt
- Ảnh đầu vào phải được chuyển về ảnh mức xám.
- Sử dụng vòng lặp while để thực hiện thuật toán.
- Xử lý trường hợp một nhóm không có pixel.
- Giới hạn số vòng lặp để tránh lặp vô hạn.

---

## 6. Kết quả mong đợi
- Tìm được ngưỡng toàn cục tối ưu.
- Ảnh đầu ra là ảnh nhị phân.
- Thuật toán hội tụ sau một số vòng lặp hữu hạn.

---

## 7. Ghi chú
- Thuật toán còn được gọi là Iterative Threshold Selection.
- Phù hợp với ảnh có sự phân tách rõ ràng giữa đối tượng và nền.

---
