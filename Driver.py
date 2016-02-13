# This is a driver program to test the graph class and turn style placement
# Last modified 2016-02-13
# @author SAM MICKA  

import Graph
import PlaceTurnStyles
def main():
    graph_init = {
        "a": ["b", "g"],
        "b": ["a", "c"],
        "c": ["a", "b"],
        "d": ["c"],
        "e": ["d"],
        "f": ["e"],
        "g": ["b"]
        }
    vertex_error_init = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0
        }
    turn_styles_init = ["c"]

    g = Graph.Graph(graph_init, vertex_error_init, turn_styles_init)

    PlaceTurnStyles.set_errors(g)
    
    g.print_graph()

if __name__ == '__main__':main()


