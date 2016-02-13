import Graph
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

    g = Graph.Graph(graph_init, vertex_error_init)
    g.add_edge("c", "e")
    g.print_graph()

if __name__ == '__main__':main()


