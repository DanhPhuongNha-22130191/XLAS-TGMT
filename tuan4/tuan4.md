# BÀI TẬP THỰC HÀNH XỬ LÝ ẢNH

## Chủ đề

**Cài đặt Convolution, Mean Filter và Median Filter bằng Python (NumPy, OpenCV)**

---

## Mục tiêu

Sau khi hoàn thành bài tập này, sinh viên có thể:

* Hiểu và cài đặt phép **tích chập (convolution)** trên ảnh xám.
* Hiểu cơ chế **padding (zero-padding)** trong xử lý ảnh.
* Tự cài đặt **Mean filter** và **Median filter** mà không sử dụng hàm lọc có sẵn.
* So sánh hiệu quả của Mean filter và Median filter trong khử nhiễu.

---

## Yêu cầu môi trường

* Python 3.x
* Thư viện: `numpy`, `opencv-python`

---

## Nội dung bài tập

### Bài 1. Cài đặt hàm Convolution

Viết hàm `convolution(gray, kernel)` thỏa các yêu cầu:

* **Input**:

  * `gray`: ảnh xám 2 chiều (NumPy array)
  * `kernel`: ma trận kernel kích thước lẻ (k × k)
* Thực hiện **zero-padding** cho ảnh đầu vào.
* Duyệt từng pixel, lấy vùng lân cận và tính tổng tích chập.
* **Output**: ảnh sau khi tích chập (kiểu `float`).

---

### Bài 2. Mean Filter

Viết hàm `mean(gray, ksize)`:

* Tạo kernel Mean kích thước `ksize × ksize` với trọng số bằng nhau.
* Thực hiện lọc bằng cách **gọi lại hàm convolution** ở Bài 1.
* Chuẩn hóa giá trị ảnh về `[0, 255]` và ép kiểu `uint8`.

**Gợi ý:** Kernel Mean có dạng:

```
1/(k^2) * [ [1 1 ... 1]
            [1 1 ... 1]
            [...        ]
            [1 1 ... 1] ]
```

---

### Bài 3. Median Filter (có padding)

Viết hàm `median(gray, ksize)`:

* Thực hiện zero-padding cho ảnh.
* Với mỗi pixel:

  * Lấy vùng lân cận kích thước `ksize × ksize`.
  * Chuyển thành mảng 1 chiều, **sắp xếp tăng dần**.
  * Nếu số phần tử lẻ → lấy phần tử chính giữa.

---

### Bài 4. Median Filter (không padding)

Viết hàm `median2(gray, ksize)`:

* **Không padding ảnh**.
* Vùng lân cận được giới hạn trong biên ảnh.
* Nếu số phần tử:

  * Lẻ → lấy phần tử giữa.
  * Chẵn → lấy **trung bình của hai phần tử giữa**.

---

### Bài 5. Thực nghiệm

* Đọc một ảnh xám bất kỳ.
* Áp dụng:

  * Mean filter với `ksize = 3`.
  * Median filter với `ksize = 7`.
* Hiển thị:

  * Ảnh gốc
  * Ảnh sau Mean filter
  * Ảnh sau Median filter

---

## Câu hỏi thảo luận

1. Mean filter và Median filter khác nhau như thế nào về nguyên lý?
2. Trong trường hợp nhiễu muối tiêu (salt & pepper), bộ lọc nào hiệu quả hơn? Vì sao?
3. Ảnh hưởng của kích thước kernel đến chất lượng ảnh đầu ra?

---

## Yêu cầu nộp bài

* File mã nguồn Python (`.py`).
* Báo cáo ngắn (PDF/Markdown) gồm:

  * Mô tả thuật toán.
  * Ảnh kết quả.
  * Nhận xét và so sánh.

---

**Ghi chú:** *Không sử dụng các hàm lọc có sẵn như `cv.filter2D`, `cv.blur`, `cv.medianBlur`.*
