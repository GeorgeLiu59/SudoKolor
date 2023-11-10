from sudoku_connections import SudokuConnections
import time

class SudokuBoard:
    def __init__(self, board):
        self.board = board
        self.sudoku_graph = SudokuConnections()
        self.mapped_grid = self.__get_mapped_matrix()
        self.solve_time = 0

    def __get_mapped_matrix(self):
        matrix = [[0 for _ in range(9)] for _ in range(9)]
        count = 1
        for r in range(9):
            for c in range(9):
                matrix[r][c] = count
                count += 1
        return matrix

    def is_blank(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def graph_coloring_initialize_color(self):
        color = [0] * (self.sudoku_graph.graph.total_vertices + 1)
        given = []  # list of all the ids whose value is already given. Thus cannot be changed
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] != 0:
                    idx = self.mapped_grid[row][col]
                    color[idx] = self.board[row][col]
                    given.append(idx)
        return color, given

    def solve_graph_coloring(self, m=9):
        start = time.time()
        color, given = self.graph_coloring_initialize_color()
        if self.__graph_color_utility(m=m, color=color, v=1, given=given) is None:
            print(":(")
            return False
        count = 1
        for row in range(9):
            for col in range(9):
                self.board[row][col] = color[count]
                count += 1

        end = time.time()
        self.solve_time = end - start
        return color

    def __graph_color_utility(self, m, color, v, given):
        if v == self.sudoku_graph.graph.total_vertices + 1:
            return True
        for c in range(1, m + 1):
            if self.can_color(v, color, c, given):
                color[v] = c
                if self.__graph_color_utility(m, color, v + 1, given):
                    return True
            if v not in given:
                color[v] = 0

    def can_color(self, v, color, c, given):
        if v in given and color[v] == c:
            return True
        elif v in given:
            return False

        for i in range(1, self.sudoku_graph.graph.total_vertices + 1):
            if color[i] == c and self.sudoku_graph.graph.is_neighbor(v, i):
                return False
        return True
