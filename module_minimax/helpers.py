import numpy as np
import os
import time
from cores import AlphaBetaSolver

class CaroBoard:
    def __init__(self, n=10):
        self.n = n
        self.board = np.zeros((n, n), dtype=int) 
        self.win_len = 3 if n < 5 else 5
        self.symbols = {0: '.', 1: 'X', -1: 'O'}

    def make_move(self, r, c, player):
        if 0 <= r < self.n and 0 <= c < self.n and self.board[r][c] == 0:
            self.board[r][c] = player
            return True
        return False

    def get_possible_moves(self):
        '''
        Trả về danh sách các nước đi hợp lệ (ô trống kế cận ô đã đánh).
        Returns:
            list of tuple: Danh sách các nước đi dưới dạng (hàng, cột).
        '''
        if np.all(self.board == 0): return [(self.n // 2, self.n // 2)]
        rows, cols = np.where(self.board != 0)
        moves = set()
        for r, c in zip(rows, cols):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0: continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.n and 0 <= nc < self.n and self.board[nr][nc] == 0:
                        moves.add((nr, nc))
        center = self.n // 2
        return sorted(list(moves), key=lambda m: abs(m[0]-center) + abs(m[1]-center))

    def check_winner(self):
        '''
        Kiểm tra người thắng cuộc.
        Returns:
            int: 1 nếu X thắng, -1 nếu O thắng, 0 nếu chưa có người thắng.
        '''
        lines = self._get_all_lines()
        for line in lines:
            if len(line) < self.win_len: continue
            for i in range(len(line) - self.win_len + 1):
                window = line[i : i + self.win_len]
                if np.all(window == 1): return 1
                if np.all(window == -1): return -1
        return 0

    def evaluate(self, ai_player):
        '''
        Hàm đánh giá bàn cờ cho AI.
        Args:
            ai_player (int): Giá trị của AI (1 hoặc -1).
        Returns:
            int: Điểm số đánh giá.
        '''
        user = -ai_player
        ai_score, user_score = 0, 0
        lines = self._get_all_lines()
        for line in lines:
            if len(line) < self.win_len: continue
            for i in range(len(line) - self.win_len + 1):
                win = line[i : i + self.win_len]
                if user not in win: ai_score += 1
                if ai_player not in win: user_score += 1
        return ai_score - user_score

    def _get_all_lines(self):
        '''
        Lấy tất cả các hàng, cột, và đường chéo trên bàn cờ.
        '''
        lines = []
        for i in range(self.n):
            lines.append(self.board[i, :])
            lines.append(self.board[:, i])
        for k in range(-self.n + 1, self.n):
            lines.append(self.board.diagonal(k))
            lines.append(np.fliplr(self.board).diagonal(k))
        return lines

    def display(self):
        header = "   " + " ".join([f"{i:2}" for i in range(self.n)])
        print(header)
        print("   " + "-" * (len(header)-3))
        for r in range(self.n):
            row_str = f"{r:2}|"
            for c in range(self.n):
                val = self.board[r][c]
                char = self.symbols[val]
                if val == 1: char = f"\033[91m{char}\033[0m"
                elif val == -1: char = f"\033[94m{char}\033[0m"
                row_str += f" {char} "
            print(row_str)
        print()


class GameController:
    """
    Nhập liệu, vòng lặp game, và hiển thị.
    """
    def __init__(self):
        self.n = 10 
        self.depth = 3
        self.user_role = 'X'
        self.user_val = 1
        self.ai_val = -1
        self.game = None
        self.ai = None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def setup(self):
        self.clear_screen()
        print("=== CAU HINH GAME ===")
        try:
            n_in = input("1. Kich thuoc N (Mac dinh 10): ")
            self.n = 10 if not n_in.strip() else int(n_in)
            
            d_in = input("2. Do sau AI (3-5): ")
            self.depth = 3 if not d_in.strip() else max(3, min(5, int(d_in)))
            
            c_in = input("3. Chon phe (X di truoc, O di sau): ").upper().strip()
            self.user_role = 'X' if c_in != 'O' else 'O'
        except:
            print("Loi nhap. Dung mac dinh.")
            time.sleep(1)

        if self.user_role == 'X':
            self.user_val = 1
            self.ai_val = -1
            print("-Ban la X (Di truoc).")
        else:
            self.user_val = -1
            self.ai_val = 1
            print("-Ban la O (Di sau).")
        
        time.sleep(1)
        self.game = CaroBoard(self.n)
        self.ai = AlphaBetaSolver(self.depth, self.ai_val)

    def run(self):
        """Vòng lặp chính của game."""
        self.setup()
        
        current_turn = 1 # X luôn đi trước
        game_over = False
        
        while not game_over:
            self.clear_screen()
            print(f"--- CARO {self.n}x{self.n}")
            self.game.display()
            
            is_user = (current_turn == self.user_val)
            
            if is_user:
                # Lượt User
                print(f"LUOT CUA BAN ({self.user_role})")
                while True:
                    try:
                        s = input("Nhap 'Hang Cot' (vd: 5 5): ")
                        if s == 'exit': 
                            exit()

                        r, c = map(int, s.split())

                        if self.game.make_move(r, c, self.user_val): 
                            break
                        print("Loi: O khong hop le.")
                    except: print("Loi cu phap.")
            else:
                # Lượt AI
                print(f"AI ({'X' if self.ai_val==1 else 'O'}) dang suy nghi")
                move = self.ai.get_best_move(self.game)
                if move:
                    self.game.make_move(move[0], move[1], self.ai_val)
                    print(f"AI danh: {move}")
                    time.sleep(1.5)
                else:
                    print("AI dau hang!")
                    game_over = True

            # Kiểm tra thắng thua
            winner = self.game.check_winner()
            if winner != 0:
                self.clear_screen()
                self.game.display()
                msg = "BAN THANG!" if winner == self.user_val else "AI THANG!"
                print(f"\n{'='*20}\n{msg}\n{'='*20}")
                game_over = True
            elif not self.game.get_possible_moves():
                print("\nHOA CO!")
                game_over = True
            
            current_turn *= -1