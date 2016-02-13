class Graph(object):
    def __init__(self, graph = {}):
        self.graph = graph

    def vertices(self):
        return list(self.graph.keys())

    def edges(self):
        edges = []
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

    def print_graph(self):
        for vertex in self.graph.keys():
            print vertex + ": \n"
            for neighbor in self.graph[vertex]:
                print "  "+neighbor+"\n"


def main():
    graph_init = {
        "a": ["b", "c", "d"],
        "b": ["e", "a", "b"],
        "c": ["a"],
        "d": ["e", "a"]
        }

    g = Graph(graph_init)
    g.print_graph()

if __name__ == '__main__':main()
