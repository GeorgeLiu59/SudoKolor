class Vertex:
    def __init__(self, identifier, data=0):
        self.id = identifier
        self.data = data
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        if neighbor.id not in self.neighbors:
            self.neighbors[neighbor.id] = weight

    def set_data(self, data):
        self.data = data

    def get_connections(self):
        return list(self.neighbors.keys())

    def get_id(self):
        return self.id

    def get_data(self):
        return self.data

    def get_weight(self, neighbor):
        return self.neighbors[neighbor.id]

    def __str__(self):
        return f"{self.data} Connected to: { [neighbor.data for neighbor in self.neighbors] }"


class Graph:
    total_vertices = 0

    def __init__(self):
        self.all_vertices = {}

    def add_vertex(self, identifier):
        if identifier in self.all_vertices:
            return None

        Graph.total_vertices += 1
        vertex = Vertex(identifier)
        self.all_vertices[identifier] = vertex
        return vertex

    def add_vertex_data(self, identifier, data):
        if identifier in self.all_vertices:
            vertex = self.all_vertices[identifier]
            vertex.set_data(data)
        else:
            print("No ID to add the data.")

    def add_edge(self, src, dest, weight=0):
        self.all_vertices[src].add_neighbor(self.all_vertices[dest], weight)
        self.all_vertices[dest].add_neighbor(self.all_vertices[src], weight)

    def is_neighbor(self, u, v):
        if 1 <= u <= 81 and 1 <= v <= 81 and u != v:
            if v in self.all_vertices[u].get_connections():
                return True
        return False

    def print_edges(self):
        for identifier in self.all_vertices:
            vertex = self.all_vertices[identifier]
            for connection in vertex.get_connections():
                print(f"{vertex.get_id()} --> {self.all_vertices[connection].get_id()}")

    def get_vertex(self, identifier):
        if identifier in self.all_vertices:
            return self.all_vertices[identifier]
        return None

    def get_all_vertices_ids(self):
        return list(self.all_vertices.keys())
