class Graph(object):
    def __init__(self, graph = {}, vertex_error = {}):
        self.graph = graph
        self.vertex_error = vertex_error

    def vertices(self):
        return list(self.graph.keys())

    def edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_vertex(self, vertex, error):
        if vertex not in self.graph:
            self.graph[vertex] = []
        if vertex not in self.vertex_error:
            self.vertex_error[vertex] = error

    def get_vertex_error(self, vertex):
        return self.vertex_err[vertex]
    
    def set_vertex_error(self, vertex, error):
        self.vertex_err[vertex] = error

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]
        if vertex2 not in self.graph:
            self.add_vertex(vertex2, 100)

    def print_graph(self):
        for vertex in self.graph.keys():
            print vertex + " error: "+ str(self.vertex_error[vertex]) + ": \n"
            for neighbor in self.graph[vertex]:
                print "  "+neighbor+"\n"


def main():
    graph_init = {
        "a": ["b", "c", "d"],
        "b": ["e", "a", "b"],
        "c": ["a"],
        "d": ["e", "a"]
        }
    vertex_error_init = {
        "a" : 100,
        "b" : 100,
        "c" : 35,
        "d" : 23,
        "e" : 74
        }

    g = Graph(graph_init, vertex_error_init)
    g.add_edge("c", "e")
    g.print_graph()

if __name__ == '__main__':main()
