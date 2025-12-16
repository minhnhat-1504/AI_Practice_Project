class OptimalColoringSolver:
    """
    Thực thi thuật toán tô màu tối ưu trên đồ thị.
    Chiến lược: Ưu tiên tô màu các đỉnh có bậc cao nhất trước (High Degree First).
    """
    def __init__(self, graph_map):
        self.graph = graph_map
        self.result_colors = {}

    def solve(self):
        """
        Chạy thuật toán tô màu.
        Returns: history (list of dicts) - Lịch sử các bước tô màu.
        """
        history = []
        self.result_colors = {}

        # --- BƯỚC 1: TÍNH BẬC CỦA CÁC ĐỈNH ---
        # Tạo danh sách (node_id, degree)
        nodes_degree = []
        for i in range(self.graph.n):
            degree = len(self.graph.adj_list[i])
            nodes_degree.append((i, degree))

        # --- BƯỚC 2: SẮP XẾP ĐỈNH THEO BẬC GIẢM DẦN ---
        # Đỉnh có nhiều kết nối nhất sẽ được xử lý trước để tối ưu màu
        nodes_degree.sort(key=lambda x: x[1], reverse=True)

        # Lấy ra danh sách các đỉnh đã sắp xếp
        sorted_nodes = [item[0] for item in nodes_degree]

        # In ra thứ tự ưu tiên tô màu
        print(f"Thu tu uu tien to mau (bac giam dan): {sorted_nodes}")

        # --- BƯỚC 3: TIẾN HÀNH TÔ MÀU (GREEDY) ---
        for node in sorted_nodes:
            # 1. Tìm tập hợp màu của các hàng xóm đã được tô trước đó
            neighbor_colors = set()
            for neighbor in self.graph.adj_list[node]:
                if neighbor in self.result_colors:
                    neighbor_colors.add(self.result_colors[neighbor])

            # 2. Chọn màu có chỉ số nhỏ nhất KHÔNG trùng với hàng xóm
            # Màu được đánh số 0, 1, 2...
            color_id = 0
            while color_id in neighbor_colors:
                color_id += 1

            # 3. Gán màu cho đỉnh hiện tại
            self.result_colors[node] = color_id

            # 4. Lưu lại trạng thái vào lịch sử
            history.append(self.result_colors.copy())

        return history