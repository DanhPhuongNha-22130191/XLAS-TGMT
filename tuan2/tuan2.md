# ĐỀ BÀI: BIẾN ĐỔI CƯỜNG ĐỘ SÁNG ẢNH VỚI OPENCV

## Mục tiêu
Thực hiện các phép biến đổi cường độ sáng ảnh bằng Python, sử dụng thư viện OpenCV và NumPy, bao gồm biến đổi tuyến tính, hiệu chỉnh gamma và kéo giãn độ tương phản.

## Nội dung yêu cầu

### 1. Đọc ảnh
- Đọc ảnh màu từ đường dẫn cho trước bằng OpenCV.
- Kiểm tra ảnh có được đọc thành công hay không.
- Nếu ảnh không đọc được, in ra thông báo `"Image is None"` và kết thúc hàm.

### 2. Biến đổi tuyến tính (Linear Transformation)
Thực hiện phép biến đổi ảnh theo công thức:


Yêu cầu:
- Chuyển ảnh sang kiểu `float32` trước khi xử lý.
- Giới hạn giá trị pixel trong khoảng `[0, 255]`.
- Chuyển ảnh kết quả về kiểu `uint8`.

### 3. Hiệu chỉnh Gamma (Gamma Correction)
Thực hiện hiệu chỉnh gamma theo công thức:


Yêu cầu:
- Chuẩn hóa ảnh về khoảng `[0,1]` trước khi xử lý.
- Giới hạn giá trị pixel trong `[0,255]`.
- Chuyển ảnh kết quả về kiểu `uint8`.

### 4. Kéo giãn độ tương phản (Contrast Stretching)
Thực hiện kéo giãn độ tương phản ảnh theo các bước:
- Dịch độ sáng ảnh với `beta = -100`.
- Tìm giá trị pixel nhỏ nhất (min) và lớn nhất (max).
- Áp dụng công thức:


- Giới hạn giá trị pixel trong `[0,255]`.
- In ra giá trị min và max của ảnh trước và sau khi kéo giãn.

### 5. Hiển thị kết quả
- Hiển thị ảnh gốc.
- Hiển thị ảnh sau khi biến đổi.
- Chờ người dùng nhấn phím bất kỳ để kết thúc chương trình.
- Đóng tất cả các cửa sổ hiển thị.

## Yêu cầu kỹ thuật
- Sử dụng Python 3.
- Sử dụng thư viện OpenCV (`cv2`) và NumPy (`numpy`).
- Code rõ ràng, dễ đọc, không làm thay đổi ảnh gốc.

## Kết quả mong đợi
- Quan sát được sự thay đổi độ sáng và độ tương phản của ảnh.
- Hiểu được tác dụng của các phép biến đổi tuyến tính, gamma và kéo giãn độ tương phản trong xử lý ảnh.
