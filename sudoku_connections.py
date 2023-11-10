from sudoku_graph import Graph

class SudokuConnections:
    def __init__(self):
        self.graph = Graph()
        self.rows = 9
        self.cols = 9
        self.total_blocks = 81
        self.create_graph()
        self.connect_edges()
        self.all_ids = self.graph.get_all_vertices_ids()

    def create_graph(self):
        for idx in range(1, self.total_blocks + 1):
            _ = self.graph.add_vertex(idx)

    def connect_edges(self):
        matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        count = 1
        for r in range(9):
            for c in range(9):
                matrix[r][c] = count
                count += 1

        head_connections = dict() 

        for r in range(9):
            for c in range(9):
                head = matrix[r][c]
                connections = self.determine_connections(matrix, r, c)
                head_connections[head] = connections

        self.connect_all(head_connections=head_connections)

    def connect_all(self, head_connections):
        for head in head_connections.keys():
            connections = head_connections[head]
            for key in connections:
                for v in connections[key]:
                    self.graph.add_edge(src=head, dest=v)

    def determine_connections(self, matrix, r, c):
        connections = dict()
        row = []
        col = []
        block = []

        for col_idx in range(c + 1, 9):
            row.append(matrix[r][col_idx])

        connections["rows"] = row

        for row_idx in range(r + 1, 9):
            col.append(matrix[row_idx][c])

        connections["cols"] = col

        block_start_r = (r // 3) * 3
        block_start_c = (c // 3) * 3

        for block_r in range(block_start_r, block_start_r + 3):
            for block_c in range(block_start_c, block_start_c + 3):
                if block_r != r or block_c != c:
                    block.append(matrix[block_r][block_c])

        connections["blocks"] = block
        return connections
