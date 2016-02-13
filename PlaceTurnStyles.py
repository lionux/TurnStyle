def set_errors(graph):
    for v in graph.vertices():
        find_unbranching_paths(v, graph)

def find_unbranching_paths(v, graph):
    something = 0
