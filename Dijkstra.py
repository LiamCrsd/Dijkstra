import math
from collections import defaultdict
from queue import PriorityQueue

def dijkstra(graphe:dict, start_vertex) -> (dict, dict):
    graphe = {**graphe}
    D = {e: math.inf for e in graphe.keys()}
    V = {}

    D[start_vertex] = 0
    V[start_vertex] = None

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        dist, current_vertex = pq.get()
        try:
            liste = graphe[current_vertex].items()
            del graphe[current_vertex]
            for neighbor, distance in liste:

                old_cost : int = D[neighbor]
                new_cost : int = D[current_vertex] + distance

                if new_cost < old_cost:
                    pq.put((new_cost, neighbor))
                    V[neighbor] = current_vertex
                    D[neighbor] : int = new_cost
        except:
            pass
    return D, V
