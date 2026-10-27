import heapq
from typing import List

class Edge:
    """Class to represent a weighted edge in the graph."""
    def __init__(self, u: int, v: int, weight: int):
        self.u = u
        self.v = v
        self.weight = weight

    def __repr__(self):
        return f"Edge({self.u}-{self.v}, w={self.weight})"


class DisjointSet:
    """Helper class for Kruskal's Algorithm to detect cycles (Union-Find)."""
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        # Path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int):
        # Union by rank
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1


class Graph:
    """Class representing an edge-weighted undirected graph."""
    def __init__(self, vertices: int):
        self.V = vertices
        self.edges: List[Edge] = []
        # Adjacency list for Prim's algorithm: adj[u] = [(v, weight), ...]
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append(Edge(u, v, weight))
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def kruskal_mst(self) -> List[Edge]:
        """
        Kruskal's algorithm to find the Minimum Spanning Tree (MST).
        Greedily picks the smallest edge that does not form a cycle.
        """
        mst_edges: List[Edge] = []
        # Sort all edges in non-decreasing order of their weight
        sorted_edges = sorted(self.edges, key=lambda e: e.weight)
        ds = DisjointSet(self.V)

        for edge in sorted_edges:
            # Check if including this edge forms a cycle
            if ds.find(edge.u) != ds.find(edge.v):
                ds.union(edge.u, edge.v)
                mst_edges.append(edge)
                
            # Early stopping if MST is complete (V-1 edges)
            if len(mst_edges) == self.V - 1:
                break

        return mst_edges

    def prim_mst(self) -> List[Edge]:
        """
        Prim's algorithm to find the Minimum Spanning Tree (MST).
        Greedily grows the MST from a starting node by picking the smallest connected edge.
        """
        if self.V == 0:
            return []

        mst_edges: List[Edge] = []
        visited = [False] * self.V
        
        # Priority queue stores tuples of (weight, current_vertex, parent_vertex)
        # Start from vertex 0 with no parent (-1)
        pq = [(0, 0, -1)]

        while pq:
            weight, u, parent = heapq.heappop(pq)

            if visited[u]:
                continue

            # Mark current node as visited
            visited[u] = True

            # If it's not the starting node, add the edge to MST
            if parent != -1:
                mst_edges.append(Edge(parent, u, weight))

            # Push all unvisited adjacent vertices into the priority queue
            for v, w in self.adj[u]:
                if not visited[v]:
                    heapq.heappush(pq, (w, v, u))

        return mst_edges


# Example Usage:
if __name__ == "__main__":
    # Create a graph with 4 vertices (0 to 3)
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    print("Kruskal's MST:")
    print(g.kruskal_mst())
    
    print("\nPrim's MST:")
    print(g.prim_mst())