# cores.py
import math
import copy
import time
import os
import shutil

class AlphaBetaSolver:
    """
    Thuật toán Minimax Alpha-Beta.
    """
    def __init__(self, depth, ai_val):
        self.depth = depth
        self.ai_val = ai_val
        self.user_val = -ai_val
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Nối vào folder images 
        self.base_dir = os.path.join(current_dir, "images")
        
        self.turn_counter = 0 # Đếm số lượt đi để tạo folder turn_1, turn_2...
        
        # Tạo thư mục gốc nếu chưa có
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def get_best_move(self, board):
        '''
        Tìm nước đi tốt nhất cho AI sử dụng Minimax với cắt tỉa Alpha-Beta.
        Args:
            board (CaroBoard): Trạng thái bàn cờ hiện tại
        Returns:
            (int, int): Tọa độ (row, col) của nước đi tốt nhất
        '''
        alpha, beta = -math.inf, math.inf
        best_val = -math.inf
        best_move = None
        
        # Lấy tất cả các nước đi có thể thực hiện
        moves = board.get_possible_moves()
        total_moves = len(moves)
        
        print(f"[AI] Depth: {self.depth} | Candidates: {total_moves}")
        start_time = time.time()
        
        self.turn_counter += 1
        current_turn_dir = os.path.join(self.base_dir, f"turn_{self.turn_counter}")
        
        # Xóa folder cũ nếu tồn tại 
        if os.path.exists(current_turn_dir):
            shutil.rmtree(current_turn_dir)
        os.makedirs(current_turn_dir)
        
        step_counter = 0 # Đếm bước trong lượt này
        print(f"Đang lưu ảnh quá trình vào: {current_turn_dir}")
        
        for i, move in enumerate(moves):
            print(f"\rDang tinh... {int((i/total_moves)*100)}%", end="")
            
            sim_board = copy.deepcopy(board)
            sim_board.make_move(move[0], move[1], self.ai_val)
            
            step_counter += 1
            img_filename = os.path.join(current_turn_dir, f"step_{step_counter}.png")
            img_title = f"Turn {self.turn_counter} - Step {step_counter}: AI check {move}"
            sim_board.save_image(img_filename, img_title)
            
            val = self.min_value(sim_board, self.depth - 1, alpha, beta)
            
            if val > best_val:
                best_val = val
                best_move = move
            
            alpha = max(alpha, best_val)
            
        print(f"\rXong! ({round(time.time() - start_time, 2)}s)      ")
        return best_move


    # alpha: giá trị tốt nhất mà Max có thể đảm bảo tại thời điểm này
    # beta: giá trị tốt nhất mà Min có thể đảm bảo tại thời điểm này

    def max_value(self, board, depth, alpha, beta):
        '''
        Hàm Max trong Minimax với cắt tỉa Alpha-Beta.
        Args:
            board (CaroBoard): Trạng thái bàn cờ hiện tại
            depth (int): Độ sâu còn lại
            alpha (float): Giá trị alpha
            beta (float): Giá trị beta
        Returns:
            float: Giá trị Max
        '''
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
        '''
        Hàm Min trong Minimax với cắt tỉa Alpha-Beta.
        Args:
            board (CaroBoard): Trạng thái bàn cờ hiện tại
            depth (int): Độ sâu còn lại
            alpha (float): Giá trị alpha
            beta (float): Giá trị beta
        Returns:
            float: Giá trị Min
        '''
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