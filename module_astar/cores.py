import heapq

class AStarSolver:
    """
    Thực thi thuật toán tìm kiếm A*.
    """
    def __init__(self, maze_map):
        self.map = maze_map
        self.open_set = []
        self.closed_set = set()

    def heuristic(self, node_a, pos_b):
        """
        Khoảng cách Manhattan - Start(x1, y1), Goal(x2, y2)
        h(n) = |x1 - x2| + |y1 - y2|
        Args:
            node_a: Node hiện tại.
            pos_b: Tuple (x, y) của điểm đích.
        Returns: Khoảng cách Manhattan giữa node_a và pos_b.
        """
        return abs(node_a.x - pos_b[0]) + abs(node_a.y - pos_b[1])

    def get_neighbors(self, node):
        """
        Lấy các ô lân cận không phải vật cản.
        Args:
            node: Node hiện tại.
        Returns: Danh sách Node lân cận.
        """
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Lên, Xuống, Trái, Phải
        
        for dr, dc in directions:
            nr, nc = node.x + dr, node.y + dc
            if 0 <= nr < self.map.n and 0 <= nc < self.map.n:
                neighbor = self.map.grid[nr][nc]
                if not neighbor.is_obstacle:
                    neighbors.append(neighbor)
        return neighbors

    def solve(self):
        """
        Chạy thuật toán.
        Returns: (path, visited_history)
            - path: Danh sách tọa độ từ Start đến Goal nếu tìm thấy, else None.
            - visited_history: Danh sách các bước đã thăm với thông tin g, h
        """
        start_node = self.map.grid[self.map.start[0]][self.map.start[1]]
        goal_pos = self.map.goal
        
        start_node.g = 0
        start_node.h = self.heuristic(start_node, goal_pos)
        start_node.f = start_node.h
        
        heapq.heappush(self.open_set, start_node)
        
        visited_history = [] 

        while self.open_set:
            current = heapq.heappop(self.open_set)
            
            step_info = {
                'pos': current.get_pos(),
                'g': current.g,
                'h': current.h,
                'f': current.f
            }
            visited_history.append(step_info)

            if current.get_pos() == goal_pos:
                return self._reconstruct_path(current), visited_history

            self.closed_set.add(current.get_pos())

            for neighbor in self.get_neighbors(current):
                if neighbor.get_pos() in self.closed_set:
                    continue

                tentative_g = current.g + 1

                if tentative_g < neighbor.g:
                    neighbor.parent = current
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor, goal_pos)
                    neighbor.f = neighbor.g + neighbor.h
                    heapq.heappush(self.open_set, neighbor)
        
        return None, visited_history

    def _reconstruct_path(self, node):
        '''
        Tái tạo đường đi từ Start đến Goal.
        Args:
            node: Node đích (Goal).
        Returns: Danh sách tọa độ từ Start đến Goal.
        '''
        path = []
        while node:
            path.append(node.get_pos())
            node = node.parent
        return path[::-1]