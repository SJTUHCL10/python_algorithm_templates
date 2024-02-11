from typing import Union, List, Tuple
import math
import heapq

inf = math.inf
Num = Union[int, float]

# n vertices, m edges

def dijkstra(graph: List[List[Num]], source: int = 0) -> List[Num]:
    """
    Vanilla dijkstra algorithm calculating the shortest distance from vertex <source>. 
    Complexity O(n ^ 2 + m).
    
    Args:
        graph: n * n adjacency matrix
        source: starting vertex

    Return:
        list of shortest distance from vertex <source>

    """
    n = len(graph)
    dist = [inf] * n
    dist[source] = 0
    st = [False] * n

    for i in range(n - 1):
        t = -1
        for j in range(n):
            if st[j]:
                continue
            if t == -1 or dist[t] > dist[j]:
                t = j
        
        for j in range(n):
            dist[j] = min(dist[j], dist[t] + graph[t][j])

        st[t] = True

    return dist


def dijkstra_with_heap(edges: List[Tuple[int, Num]], source: int = 0) -> List[Num]:
    """
    Dijkstra algorithm with heap. 
    Complexity O(m log n).

    Args:
        edges: adjacency list
        source: starting vertex

    Return:
        list of shortest distance from vertex <source>

    """
    n = len(edges)
    dist = [inf] * n
    dist[source] = 0
    st = [False] * n
    hp = [(0, source)]
    while hp:
        _, u = heapq.heappop(hp)
        if st[u]:
            continue
        for v, w in edges[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(hp, (dist[v], v))
        st[u] = True

    return dist


def main():
    graph = [
        [inf, 3, 2, inf, inf],
        [3, inf, 2, 1, inf],
        [2, 2, inf, inf, 10],
        [inf, 1, inf, inf, 5],
        [inf, inf, 10, 5, inf],
    ]
    edges = [
        [(1, 3), (2, 2)],
        [(0, 3), (2, 2), (3, 1)],
        [(0, 2), (1, 2), (4, 10)],
        [(1, 1), (4, 5)],
        [(2, 10), (3, 5)],
    ]
    print(dijkstra(graph=graph, source=0))     # [0, 3, 2, 4, 9]
    print(dijkstra_with_heap(edges=edges, source=2))   # [2, 2, 0, 3, 8]


if __name__ == '__main__':
    main()
