import heapq
from typing import List, Tuple

class ShortestPath:
    """Class to compute shortest paths in an edge-weighted directed graph."""
    
    def __init__(self, vertices: int):
        self.V = vertices
        # Adjacency list for Dijkstra: adj[u] = [(v, weight), ...]
        self.adj: List[List[Tuple[int, int]]] = [[] for _ in range(vertices)]
        # Edge list for Bellman-Ford: [(u, v, weight), ...]
        self.edges: List[Tuple[int, int, int]] = []

    def add_edge(self, u: int, v: int, weight: int):
        """Adds a directed edge from u to v with a given weight."""
        self.adj[u].append((v, weight))
        self.edges.append((u, v, weight))

    def dijkstra(self, src: int) -> List[int]:
        """
        Dijkstra's algorithm for finding single-source shortest paths.
        Note: Does not work with negative edge weights.
        """
        # Initialize distances to infinity, and source distance to 0
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        # Priority queue stores tuples of (distance, vertex)
        pq = [(0, src)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            # Skip processing if a shorter path to u has already been found
            if current_dist > dist[u]:
                continue

            # Relax all outgoing edges
            for v, weight in self.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        # Convert infinity to -1 to signify unreachable nodes
        return [int(d) if d != float('inf') else -1 for d in dist]

    def bellman_ford(self, src: int) -> List[int]:
        """
        Bellman-Ford algorithm for finding single-source shortest paths.
        Works with negative edge weights and detects negative weight cycles.
        """
        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax all edges V - 1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles by attempting to relax one more time
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle.")

        # Convert infinity to -1 to signify unreachable nodes
        return [int(d) if d != float('inf') else -1 for d in dist]


# Example Usage:
if __name__ == "__main__":
    # Create a graph with 5 vertices
    sp = ShortestPath(5)
    
    sp.add_edge(0, 1, 9)
    sp.add_edge(0, 2, 6)
    sp.add_edge(0, 3, 5)
    sp.add_edge(0, 4, 3)
    sp.add_edge(2, 1, 2)
    sp.add_edge(2, 3, 4)
    
    print("Dijkstra Distances from source 0:")
    print(sp.dijkstra(0))
    
    print("\nBellman-Ford Distances from source 0:")
    print(sp.bellman_ford(0))

    # Example with a negative cycle for Bellman-Ford
    sp_neg = ShortestPath(3)
    sp_neg.add_edge(0, 1, 1)
    sp_neg.add_edge(1, 2, -1)
    sp_neg.add_edge(2, 0, -1)
    
    try:
        print("\nAttempting Bellman-Ford on graph with negative cycle:")
        sp_neg.bellman_ford(0)
    except ValueError as e:
        print(f"Error caught: {e}")