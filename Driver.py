# This is a driver program to test the graph class and turn style placement
# Last modified 2016-02-13
# @author SAM MICKA  

import Graph
import PlaceTurnStyles
inf = 99999999
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
        "a" : inf,
        "b" : inf,
        "c" : inf,
        "d" : inf,
        "e" : inf,
        "f" : inf,
        "g" : inf
        }
    turn_styles_init = ["c"]

    g = Graph.Graph(graph_init, vertex_error_init, turn_styles_init)

    PlaceTurnStyles.set_errors(g)
    
    g.print_graph()

    graph_init2 = {
        "a": ["b", "c"],
        "b": ["c", "e"],
        "c": ["h"],
        "d": ["k"],
        "e": ["d"],
        "f": ["g"],
        "g": ["h", "j"],
        "h": ["i"],
        "i": ["j"],
        "j": [],
        "k": []
        }
    vertex_error_init2 = {
        "a" : inf,
        "b" : inf,
        "c" : inf,
        "d" : inf,
        "e" : inf,
        "f" : inf,
        "g" : inf,
        "h" : inf,
        "i" : inf,
        "j" : inf,
        "k" : inf
        }
    
    turn_styles_init2 = ["a", "j", "k"]

    g2 = Graph.Graph(graph_init2, vertex_error_init2, turn_styles_init2)

    PlaceTurnStyles.set_errors(g2)
    g2.print_graph()

    graph_init3 = {
        "a": ["b"],
        "b": ["a", "c"],
        "c": ["b", "d"],
        "d": ["c", "e"],
        "e": ["d"]
        }
    vertex_error_init3 = {
        "a" : inf,
        "b" : inf,
        "c" : inf,
        "d" : inf,
        "e" : inf
        }
    
    turnstiles_init3 = ["a"]

    g3 = Graph.Graph(graph_init3, vertex_error_init3, turnstiles_init3)

    PlaceTurnStyles.set_errors(g3)
    g3.print_graph()

if __name__ == '__main__':main()


