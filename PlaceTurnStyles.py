def set_errors(graph):
    for v in graph.vertices():
        print "Path to turn style from: "+v+" "+str(find_nearest_turn_style(v, graph))
        
"""Using BFS we will find the nearest turn style 
TODO: Need to make sure that we do not count edges that are not part of a branch...
"""
def find_nearest_turn_style(v, graph):
    q = [v]
    while q:
        path = q.pop(0)
        vertex = path[-1]
        if vertex in graph.get_turn_styles():
            return path #len(path) we will ultimately want the length of the path to determine error
        for neighbors in graph.get_neighbors(vertex):
            new_path = list(path)
            new_path.append(neighbors)
            q.append(new_path)
