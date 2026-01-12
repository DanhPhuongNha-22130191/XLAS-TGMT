# YÊU CẦU CHI TIẾT – CÂN BẰNG HISTOGRAM ẢNH XÁM

## Yêu cầu

1. Sử dụng thư viện **NumPy** và **OpenCV (cv2)** để thực hiện xử lý ảnh số.

2. Đọc một ảnh từ file và chuyển ảnh sang dạng **ảnh xám**.

3. Xây dựng hàm `histCalc(gray, L)` với các yêu cầu sau:
   - Khởi tạo một mảng histogram gồm `L` phần tử, kiểu `float`, ban đầu có giá trị bằng 0.
   - Lấy kích thước ảnh xám `gray` là `N × M`.
   - Duyệt qua từng pixel của ảnh bằng hai vòng lặp `for`.
   - Với mỗi pixel, xác định mức xám `g` và tăng giá trị histogram tại vị trí `g` lên 1.
   - Chuẩn hóa histogram bằng cách chia cho tổng số pixel của ảnh (`N × M`).
   - Trả về histogram chuẩn hóa.

4. Xây dựng hàm `histEqual(gray, L)` để thực hiện cân bằng histogram:
   - Gọi hàm `histCalc(gray, L)` để tính histogram chuẩn hóa.
   - Khởi tạo mảng histogram tích lũy `e_hist` có cùng kích thước với histogram.
   - Tính histogram tích lũy bằng cách cộng dồn các giá trị histogram từ mức xám 0 đến mức xám `g`.
   - Xác định mức xám nhỏ nhất xuất hiện trong ảnh (`g_min`).
   - Lấy giá trị histogram tích lũy tương ứng với `g_min` làm `C_min`.
   - Thiết lập hệ số biến đổi:
     
     ```
     coef = (L - 1) / (1 - C_min)
     ```

   - Chuẩn hóa và làm tròn histogram tích lũy theo công thức cân bằng histogram.
   - Chuyển histogram sau cân bằng sang kiểu `uint8`.

5. Tạo ảnh đầu ra sau cân bằng histogram:
   - Khởi tạo ảnh kết quả có cùng kích thước với ảnh gốc.
   - Duyệt qua từng pixel của ảnh gốc.
   - Ánh xạ mức xám cũ sang mức xám mới thông qua histogram đã cân bằng.
   - Gán giá trị mới cho ảnh kết quả.

6. Thực hiện cân bằng histogram trực tiếp trên ảnh xám và hiển thị kết quả.

7. (Nâng cao) Chuyển ảnh sang không gian màu **HSV** và:
   - Chỉ áp dụng cân bằng histogram cho kênh **V (Value)**.
   - Giữ nguyên các kênh **H** và **S**.

8. Hiển thị ảnh sau khi cân bằng histogram bằng OpenCV.

9. Giải phóng tài nguyên và đóng tất cả cửa sổ hiển thị sau khi kết thúc chương trình.
