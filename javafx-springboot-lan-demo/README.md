# Demo JavaFX Client + Spring Boot Server (Mạng LAN)

Dự án này minh họa cách một ứng dụng Desktop JavaFX giao tiếp với một API Server Spring Boot qua mạng nội bộ (LAN).

## Yêu cầu
- Java 17 trở lên
- Maven 3.6+

## Cấu trúc dự án
- `server/`: Ứng dụng Web Spring Boot
- `client/`: Ứng dụng Desktop JavaFX

## Hướng dẫn sử dụng

### 1. Khởi động Server (Máy chủ)
1. Mở terminal tại thư mục `server`.
2. Chạy lệnh: `mvn spring-boot:run`
3. Server sẽ khởi động tại cổng `8080`.
   - Nó được cấu hình bind tới `0.0.0.0`, nghĩa là có thể truy cập từ các máy khác trong cùng mạng.
   - **Quan trọng:** Đảm bảo tường lửa (firewall) của bạn cho phép kết nối đến cổng 8080.

### 2. Xác định IP của Server
1. Trên máy chạy server, mở terminal.
2. Chạy lệnh `ipconfig` (Windows) hoặc `ifconfig` (Linux/Mac).
3. Ghi lại địa chỉ IPv4 (ví dụ: `192.168.1.100`).

### 3. Khởi động Client (Máy trạm)
1. Mở terminal mới tại thư mục `client`.
2. Chạy lệnh: `mvn javafx:run`
3. Cửa sổ ứng dụng JavaFX sẽ hiện ra.

### 4. Kết nối
1. Trong giao diện JavaFX, nhập địa chỉ IP của Server (đã lấy ở Bước 2).
   - Ví dụ: `192.168.1.100`
2. Nhấn nút **"Ping Server"** (Kiểm tra kết nối).
3. Bạn sẽ thấy phản hồi "Pong từ Server!..." trong khung kết quả.

## Khắc phục sự cố
- **Connection Timeout/Refused (Kết nối bị từ chối/quá hạn)**:
    - Kiểm tra xem Server đã chạy chưa.
    - Kiểm tra xem Tường lửa (Firewall) trên máy Server có chặn cổng 8080 không.
    - Thử ping máy server từ máy client bằng dòng lệnh: `ping <IP>`.
- **JavaFX not found**: Đảm bảo bạn đang chạy với JDK có hỗ trợ JavaFX hoặc để Maven tự xử lý (như đã cấu hình trong `pom.xml`).

## Đóng gói file chạy (.EXE) cho Client

Để tạo file chạy độc lập (kèm sẵn Java Runtime) để mang sang máy khác:

1.  Tại thư mục `client`, chạy lệnh:
    ```bash
    mvn clean jlink:jlink
    ```
    *(Lưu ý: Nếu máy bạn có WiX Toolset, bạn có thể chạy `mvn jlink:jpackage` để tạo file cài đặt .msi/.exe chuẩn)*

2.  File chạy sẽ được tạo tại:
    `client/target/lan-ping-client/bin/lan-ping-client.bat` (Windows)

3.  **Cách dùng trên máy khác**:
    -   Copy toàn bộ thư mục `client/target/lan-ping-client` sang máy khác.
    -   Chạy file `bin/lan-ping-client.bat`.
    -   Không cần cài Java trên máy đó.
