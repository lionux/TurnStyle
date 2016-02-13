import Graph
import PlaceTurnStyles
def main():
    graph_init = {
        "a": ["b", "c", "d"],
        "b": ["e", "a", "b"],
        "c": ["a"],
        "d": ["e", "a"],
        "e": []
        }
    vertex_error_init = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0
        }
    turn_styles_init = ["c"]

    g = Graph.Graph(graph_init, vertex_error_init, turn_styles_init)
    g.print_graph()

    PlaceTurnStyles.set_errors(g)

if __name__ == '__main__':main()


