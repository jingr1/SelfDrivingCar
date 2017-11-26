import math

def dist_between(start,end):
    return math.sqrt(pow((start[0]-end[0]),2)+pow((start[1]-end[1]),2))


def get_best_f_score(input_set,scoredict):
    idx = input_set.pop()
    input_set.add(idx)
    best = idx
    bv = scoredict[idx]
    for idx in input_set:
        if scoredict[idx] < bv:
            best = idx
            bv = scoredict[idx]
    return best  

def reconstruct_path(start_node,came_from, current_node):
    p = [current_node]

    while current_node != start_node:
        current_node = came_from[current_node]
        p.append(current_node)
    return p[::-1]
def shortest_path(M,start,goal):
    print("shortest path called")
    intersections = M.intersections
    roads = M.roads
    frontierset = set([start])
    explorededset = set()
    came_from = {}
    g_score = {}
    h_score = {}
    f_score = {}
    g_score[start] = 0
    h_score[start] = dist_between(intersections[start],intersections[goal])
    f_score[start] = g_score[start] + h_score[start]

    while frontierset:
        currentintersection = get_best_f_score(frontierset,f_score)
        frontierset.remove(currentintersection)
        explorededset.add(currentintersection)
        neighborsets = set(roads[currentintersection])
        if currentintersection == goal:
            return reconstruct_path(start,came_from, goal)
        else:
            for neighbor in neighborsets:
                if neighbor not in explorededset:
                    tentative_g_score = g_score[currentintersection] + dist_between(intersections[currentintersection],intersections[neighbor])
                    if neighbor not in frontierset:
                        frontierset.add(neighbor)
                        h_score[neighbor] = dist_between(intersections[neighbor],intersections[goal])
                        tentative_is_better = True
                    elif (tentative_g_score < g_score[neighbor]):
                        tentative_is_better = True
                    else:
                        tentative_is_better = False

                    if tentative_is_better == True:
                        came_from[neighbor] = currentintersection
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = g_score[neighbor] + h_score[neighbor]

    print('can not find the shortest path')