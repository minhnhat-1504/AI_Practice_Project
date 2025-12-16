import math
import copy
import time
import os

class AlphaBetaSolver:
    """
    Thuật toán Minimax Alpha-Beta.
    """
    def __init__(self, depth, ai_val):
        self.depth = depth
        self.ai_val = ai_val
        self.user_val = -ai_val

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_best_move(self, board):
        """
        Tìm nước đi tối ưu nhất cho AI.
        Args:
            board (CaroBoard): Bàn cờ hiện tại.
        Returns:
            tuple: Nước đi tốt nhất dưới dạng (hàng, cột).
        """
        alpha, beta = -math.inf, math.inf
        best_val = -math.inf
        best_move = None
        
        # Lấy danh sách các nước đi có thể
        moves = board.get_possible_moves()
        total_moves = len(moves)
        
        print(f"[AI Start] Depth: {self.depth} | Candidates: {total_moves}")
        
        # Duyệt qua từng nước đi ứng viên
        for i, move in enumerate(moves):
            # 1. Tạo bàn cờ giả lập
            sim_board = copy.deepcopy(board) # Sử dụng deepcopy() mà không phải copy() để tránh lỗi tham chiếu các đối tượng con 
            sim_board.make_move(move[0], move[1], self.ai_val)
            
            self.clear_screen()
            print("=" * 40)
            print(f"   AI ĐANG THỬ NƯỚC ĐI: {move} ({i+1}/{total_moves})")
            print("=" * 40)
            
            # Hiển thị bàn cờ giả lập
            sim_board.display()
            
            print(f"-> Giả sử AI đánh vào {move}.")
            print("-> Nhấn [ENTER] để AI tính toán tiếp...")
            input()

            # 2. Gọi đệ quy tìm giá trị Min 
            val = self.min_value(sim_board, self.depth - 1, alpha, beta)
            
            print(f"   => Điểm đánh giá cho nước {move} là: {val}")
            time.sleep(5) 

            if val > best_val:
                best_val = val
                best_move = move
            
            alpha = max(alpha, best_val)
            
        return best_move

    # alpha: Điểm số tốt nhất mà AI (Max) chắc chắn đạt được.
    # beta: Điểm số thấp nhất mà Đối thủ (Min) chắc chắn ép AI phải chịu

    def max_value(self, board, depth, alpha, beta):
        """
        Lượt AI (MAX).
        Args:
            board (CaroBoard): Bàn cờ hiện tại.
            depth (int): Độ sâu còn lại.
            alpha (float): Giá trị alpha.
            beta (float): Giá trị beta.
        Returns:
            float: Giá trị đánh giá tối đa.
        """
        winner = board.check_winner()
        if winner == self.ai_val: return 100000
        if winner == self.user_val: return -100000
        
        if depth == 0: 
            return board.evaluate(self.ai_val)

        v = -math.inf
        for move in board.get_possible_moves():
            sim_board = copy.deepcopy(board)
            sim_board.make_move(move[0], move[1], self.ai_val)
            
            v = max(v, self.min_value(sim_board, depth - 1, alpha, beta))
            
            if v >= beta: return v
            alpha = max(alpha, v)
        return v

    def min_value(self, board, depth, alpha, beta):
        """
        Lượt User (MIN).
        Args:
            board (CaroBoard): Bàn cờ hiện tại.
            depth (int): Độ sâu còn lại.
            alpha (float): Giá trị alpha.
            beta (float): Giá trị beta.
        Returns:
            float: Giá trị đánh giá tối thiểu.
        """
        winner = board.check_winner()
        if winner == self.ai_val: return 100000
        if winner == self.user_val: return -100000
        
        if depth == 0: 
            return board.evaluate(self.ai_val)

        v = math.inf
        for move in board.get_possible_moves():
            sim_board = copy.deepcopy(board)
            sim_board.make_move(move[0], move[1], self.user_val)
            
            v = min(v, self.max_value(sim_board, depth - 1, alpha, beta))
            
            if v <= alpha: return v
            beta = min(beta, v)
        return v