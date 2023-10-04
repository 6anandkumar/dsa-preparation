# Bellman Ford Algorithm works where Dijkstra's Fails - In Directed graph with negative weights
# Bellman Ford is Just Dijkstra's Algo's 'if' condition in a V-1 loop
# This takes edges array instead of adjacency list

import math
def shortestPath(edges,V,source):
    cost = [math.inf for _ in range(V)]
    cost[source] = 0
    for _ in range(V-1):
        for j in range(len(edges)):     #This is also called edge relaxation
            frm = edges[j][0]
            to = edges[j][1]
            price = edges[j][2]
            if cost[frm]+price < cost[to]:
                cost[to] = cost[frm] + price
                
    # return cost[dest] #Return if only this is needed

    #Optional: To find if there is a negative cycle - run edge relaxation one more time
    # if there is any reduction in cost that means there is a negative cycle in graph
    
    for j in range(len(edges)):     #This is also called edge relaxation
            frm = edges[j][0]
            to = edges[j][1]
            price = edges[j][2]
            if cost[frm]+price < cost[to]:
                return -1
    
    return cost
    
    
    
    
    
    