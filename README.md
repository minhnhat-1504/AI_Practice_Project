# AI Practice Project

## Giới thiệu

Dự án **AI Practice Project** là một bộ sưu tập các module thực hành thuật toán trí tuệ nhân tạo cơ bản. Dự án được thiết kế để học và thử nghiệm các thuật toán AI thông qua các bài toán thực tế như tìm đường đi, tô màu đồ thị và chơi cờ Caro.

Dự án bao gồm 3 module chính:
- **Module A***: Thuật toán tìm đường đi ngắn nhất trên lưới 2D.
- **Module Tô màu Đồ thị**: Giải quyết bài toán tô màu đồ thị sử dụng phương pháp tham lam.
- **Module Minimax**: AI chơi cờ Caro sử dụng thuật toán Minimax với Alpha-Beta Pruning.

## Cấu trúc dự án

```
ai_practice_project/
├── README.md              # Tài liệu tổng quan dự án
├── requirements.txt       # Danh sách thư viện cần thiết
├── module_astar/          # Module tìm đường đi A*
│   ├── README.md
│   ├── main.py
│   ├── cores.py
│   ├── helpers.py
│   ├── astar_demo.ipynb
│   └── images/
├── module_coloring/       # Module tô màu đồ thị
│   ├── README.md
│   ├── main.py
│   ├── cores.py
│   ├── helpers.py
│   ├── input.txt
│   ├── coloring_demo.ipynb
│   └── images/
└── module_minimax/        # Module AI cờ Caro
    ├── README.md
    ├── main.py
    ├── cores.py
    ├── helpers.py
    └── images/
```

## Yêu cầu hệ thống

- Python 3.6 hoặc cao hơn
- Các thư viện Python: numpy, matplotlib, networkx

## Cài đặt

1. **Clone hoặc tải dự án**:
   ```bash
   git clone https://github.com/minhnhat-1504/AI_Practice_Project
   cd ai_practice_project
   ```

2. **Cài đặt các thư viện cần thiết**:
   ```bash
   pip install -r requirements.txt
   ```

   Hoặc cài đặt thủ công:
   ```bash
   pip install numpy matplotlib networkx
   ```

## Cách sử dụng

### Chạy từng module

1. **Module A***:
   ```bash
   cd module_astar
   python main.py
   ```

2. **Module Tô màu Đồ thị**:
   ```bash
   cd module_coloring
   python main.py
   ```

3. **Module Minimax (Cờ Caro)**:
   ```bash
   cd module_minimax
   python main.py
   ```

### Chạy demo với Jupyter Notebook

Mỗi module có file notebook demo:
- `module_astar/astar_demo.ipynb`
- `module_coloring/coloring_demo.ipynb`

Để chạy notebook:
```bash
pip install jupyter
jupyter notebook
```

Sau đó mở file `.ipynb` tương ứng.

## Mô tả các module

### 1. Module A* (Tìm đường đi)

Triển khai thuật toán A* để tìm đường đi ngắn nhất từ điểm bắt đầu đến điểm đích trên lưới 2D có vật cản.

**Tính năng chính**:
- Tùy chỉnh kích thước lưới và mật độ vật cản
- Trực quan hóa quá trình tìm kiếm
- Xuất kết quả dưới dạng hình ảnh

**Thuật toán**: A* với hàm heuristic Manhattan distance.

### 2. Module Tô màu Đồ thị

Giải quyết bài toán tô màu đồ thị sử dụng thuật toán tham lam với heuristic bậc đỉnh.

**Tính năng chính**:
- Sinh đồ thị ngẫu nhiên hoặc đọc từ file
- Trực quan hóa đồ thị và kết quả tô màu
- Hiển thị thứ tự tô màu

**Thuật toán**: Greedy coloring với sắp xếp theo bậc đỉnh giảm dần.

### 3. Module Minimax (AI Cờ Caro)

Xây dựng AI chơi cờ Caro sử dụng thuật toán Minimax kết hợp Alpha-Beta Pruning.

**Tính năng chính**:
- Tùy chỉnh kích thước bàn cờ và độ sâu tìm kiếm
- Chơi với AI trên terminal
- Lưu ảnh từng lượt đi

**Thuật toán**: Minimax với Alpha-Beta Pruning và hàm đánh giá dựa trên "cửa sổ chiến thắng".


