# Module Minimax: AI Cờ Caro (Gomoku)

Module này cài đặt thuật toán **Minimax** kết hợp kỹ thuật cắt tỉa **Alpha-Beta Pruning** để xây dựng một AI chơi cờ Caro (Gomoku) trên giao diện Terminal (Console).

## 1\. Cấu trúc thư mục & File

Dự án được tổ chức theo mô hình **Core - Helper - Main** (OOP) để đảm bảo tính tách biệt và dễ bảo trì:

  * **`main.py`**:
      * Điểm bắt đầu của chương trình.
      * Khởi tạo `GameController` và kích hoạt vòng lặp trò chơi.
  * **`helpers.py`**:
      * **Class `CaroBoard`**: Quản lý trạng thái bàn cờ, luật chơi (thắng/thua/hòa) và tính toán hàm lượng giá (Heuristic).
      * **Class `GameController`**: Quản lý giao diện dòng lệnh, nhập liệu từ người dùng, và điều phối lượt đi giữa Người và AI.
  * **`cores.py`**:
      * **Class `AlphaBetaSolver`**: "Bộ não" của AI. Chứa thuật toán Minimax và logic cắt tỉa Alpha-Beta.

## 2\. Tính năng nổi bật

1.  **Tùy chỉnh linh hoạt**:
      * Kích thước bàn cờ $N \times N$ (Mặc định 10x10).
      * Độ sâu tìm kiếm (Depth) từ 3 đến 5.
      * Chọn phe đi trước (X) hoặc đi sau (O).
2.  **Luật chơi tự động**:
      * Nếu bàn cờ nhỏ ($N < 5$): Cần 3 quân liên tiếp để thắng.
      * Nếu bàn cờ lớn ($N \ge 5$): Cần 5 quân liên tiếp để thắng.

## 3\. Thuật toán & Hàm lượng giá

### 3.1. Thuật toán chính

Sử dụng **Minimax** với độ sâu giới hạn (Depth-limited search) kết hợp **Alpha-Beta Pruning** để loại bỏ các nhánh không cần thiết, giúp tăng tốc độ tính toán.

### 3.2. Hàm lượng giá (Heuristic)

Hàm đánh giá trạng thái bàn cờ dựa trên công thức:

$$E(n) = X(n) - O(n)$$

Trong đó:

  * **$X(n)$**: Tổng số "cửa sổ chiến thắng" (sliding window) mà quân AI (hoặc X) đang chiếm ưu thế (không bị đối thủ chặn).
  * **$O(n)$**: Tổng số "cửa sổ chiến thắng" mà Người chơi (hoặc O) đang chiếm ưu thế (không bị AI chặn).

## 4\. Yêu cầu cài đặt

Đảm bảo đã cài đặt thư viện `numpy` trong môi trường Python:

```bash
pip install numpy
```

## 5\. Hướng dẫn sử dụng

### Bước 1: Chạy chương trình

Mở terminal tại thư mục `module_minimax` và chạy lệnh:

```bash
python main.py
```

### Bước 2: Cấu hình

Nhập các thông số khi được hỏi:

1.  **Kích thước N**: Nhập số nguyên (ví dụ: `10` hoặc `5`).
2.  **Độ sâu**: Nhập từ `3` đến `5` (Khuyên dùng `3` để test nhanh, `5` để AI thông minh nhưng chậm hơn).
3.  **Chọn phe**: Nhập `X` (bạn đi trước) hoặc `O` (AI đi trước).

### Bước 3: Cách chơi

  * Nhập tọa độ theo cú pháp: `Hàng Cột` (cách nhau bởi dấu cách).
      * Ví dụ: `5 5` (đánh vào hàng 5, cột 5).
  * Khi đến lượt AI: Chương trình sẽ hiện bàn cờ thử nghiệm. Bạn chụp hình xong thì nhấn **Enter** để AI tính tiếp.

-----

**Lưu ý:** Để thoát game giữa chừng, nhập `exit` khi đến lượt của bạn.