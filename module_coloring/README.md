# Module Graph Coloring: Tô Màu Đồ Thị

Dự án triển khai giải thuật cho bài toán **Tô màu đồ thị** - một bài toán thuộc nhóm bài toán thỏa mãn ràng buộc - CSP.

Chương trình được viết dưới dạng **Jupyter Notebook**, sử dụng chiến lược tham lam (Greedy) dựa trên bậc của đỉnh để tối ưu hóa số lượng màu sử dụng, kèm theo mô phỏng đồ họa trực quan.

## 1\. Cấu trúc Dự án

```
.
├── module_coloring/
│   ├── coloring_demo.ipynb  # File chính chứa mã nguồn và giao diện chạy
│   ├── input.txt            # File dữ liệu đầu vào (tùy chọn)
│   └── README.md            # Tài liệu hướng dẫn
```

### Chi tiết file `coloring_demo.ipynb`

Notebook được chia thành 3 Cell chính theo mô hình OOP:

1.  **Cell 1 - Helper (GraphMap):**
      * Quản lý cấu trúc dữ liệu đồ thị (Danh sách kề, Danh sách cạnh).
      * Hỗ trợ sinh đồ thị ngẫu nhiên hoặc đọc từ file ma trận kề.
2.  **Cell 2 - Core (OptimalColoringSolver):**
      * Chứa thuật toán tô màu chính.
      * Sử dụng chiến lược **High-Degree First** (Ưu tiên đỉnh bậc cao) để giảm thiểu số màu.
3.  **Cell 3 - Main & Visualizer:**
      * Hàm `visualize_coloring_history`: Vẽ đồ thị minh họa từng bước bằng thư viện `networkx`.
      * Hàm `run_coloring_interactive`: Giao diện dòng lệnh tương tác với người dùng.

## 2\. Tính năng 

  * **Đa dạng chế độ nhập liệu**:
      * **Random Mode [R]**: Tự động sinh đồ thị ngẫu nhiên (chỉ định số đỉnh $N$ và xác suất nối cạnh).
      * **File Mode [F]**: Đọc cấu trúc đồ thị từ file văn bản .txt bên ngoài.
  * **Trực quan hóa (Visualization)**:
      * Hiển thị quá trình tô màu qua từng bước.
      * Sử dụng bố cục lưới để dễ dàng quan sát lịch sử thuật toán.
  * **Tùy chỉnh giao diện**:
      * Cho phép người dùng tự định nghĩa bảng màu (nhập tên màu tiếng Anh hoặc mã Hex).
      * Tự động xử lý nếu số lượng màu người dùng nhập không đủ.

## 3\. Thuật toán sử dụng

Chương trình giải quyết bài toán: *Gán màu cho các đỉnh sao cho không có hai đỉnh kề nhau cùng màu, dùng ít màu nhất có thể.*

**Chiến lược Greedy High-Degree First:**

1.  **Tính bậc (Degree):** Đếm số lượng cạnh nối của mỗi đỉnh.
2.  **Sắp xếp:** Xếp các đỉnh theo thứ tự bậc giảm dần (Đỉnh có nhiều kết nối nhất sẽ khó tô nhất $\rightarrow$ Xử lý trước).
3.  **Gán màu tham lam:**
      * Duyệt qua danh sách đỉnh đã sắp xếp.
      * Với mỗi đỉnh, chọn màu có chỉ số nhỏ nhất ($0, 1, 2...$) mà **chưa bị hàng xóm sử dụng**.

## 4\. Yêu cầu cài đặt

Bạn cần cài đặt các thư viện Python sau để chạy Notebook:

```bash
pip install networkx matplotlib
```

## 5\. Hướng dẫn sử dụng

### Bước 1: Khởi động

Mở file `coloring_demo.ipynb` bằng Jupyter Notebook hoặc VS Code.

### Bước 2: Chạy chương trình

1.  Chạy lần lượt **Cell 1** và **Cell 2** để nạp các lớp `GraphMap` và `OptimalColoringSolver`.
2.  Chạy **Cell 3**. Chương trình sẽ hiện khung nhập liệu bên dưới.

### Bước 3: Tương tác

  * **Chọn chế độ:** Nhập `R` (Ngẫu nhiên) hoặc `F` (File).
  * **Cấu hình (Nếu chọn R):** Nhập số đỉnh (VD: 10) và xác suất (VD: 0.4).
  * **Chọn màu:**
      * Nhập danh sách màu bạn thích (VD: `red blue green yellow`).
      * Hoặc nhấn **Enter** để dùng bảng màu mặc định.

### Định dạng file `input.txt` (Dành cho chế độ File)

Nếu bạn muốn tự nhập đồ thị, hãy tạo file `input.txt` cùng thư mục với nội dung:

  * Dòng 1: Số nguyên $N$ (Số lượng đỉnh).
  * $N$ dòng tiếp theo: Ma trận kề ($N \times N$) gồm các số 0 và 1.

**Ví dụ input.txt:**

```text
4
0 1 1 0
1 0 1 0
1 1 0 1
0 0 1 0
```