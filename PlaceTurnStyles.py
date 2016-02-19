# This program places the turn styles on the graph
# Last modified 2016-02-13
# @author SAM MICKA

#Reset the errors of each node based on how far they are from a turn style
def set_errors(graph):
    for v in graph.vertices():
        #print "Path to turn style from: "+v+" "+str(find_nearest_turn_style(v, graph))
        graph.set_vertex_error(v, find_nearest_turn_style(v, graph))
    #graph.print_graph()
    place_turn_styles(graph)


#Using a modified BFS that ignores unbranching paths we will find the nearest turn style 
def find_nearest_turn_style(v, graph):
    q = [v]
    while q:
        path = list(q.pop(0))
        vertex = path[-1]
        #CASE 1: our vertex is already a turn style
        if vertex in graph.get_turn_styles():
            return len(path)-1 
        #CASE 2: one of the neighbors is a turn style
        if len(set(graph.get_turn_styles()).intersection(set(graph.get_neighbors(vertex)))) != 0:
            #turn_style = list(set(graph.get_turn_styles()).intersection(set(graph.get_neighbors(vertex))))[0]
            #path.append(turn_style)
            #del path[0] #get rid of the first element because we don't need it in our path
            return len(path)-1
        #CASE 3: no turn styles in neighbor list and there is a branch
        if len(graph.get_neighbors(vertex)) > 1:
            for neighbor in graph.get_neighbors(vertex):
                new_path = list(path)
                new_path.append(neighbor)
                q.append(new_path)
        #CASE 4: only one neighbor, not a turn style (collaps path, it is unbranching)
        else:
            new_path = list(graph.get_neighbors(vertex))
            q.append(new_path)

#With the errors reset this function places a turn style at the node with the highest error
def place_turn_styles(graph):
    turn_style_candidate = ""
    max_error = 0
    for v in graph.vertices():
        if graph.get_vertex_error(v) > max_error:
            max_error = graph.get_vertex_error(v)
            turn_style_candidate = v

    if max_error > 0:
        print "adding turn style at: "+turn_style_candidate
        graph.add_turn_style(turn_style_candidate)
        set_errors(graph)
    else:
        print "\n\nFinished setting turn styles.\n\n"
