import sys

class FastIO:
    import os
    # Try to use local input file if exists
    if os.path.exists(input_file := os.path.splitext(__file__)[0] + ".txt"):
        sys.stdin = open(input_file, "r")
    input = sys.stdin.buffer.readline

    @staticmethod
    def getInt() -> int:
        return int(FastIO.input())

    @staticmethod
    def getInts():
        return list(map(int, FastIO.input().split()))

    @staticmethod
    def getFloat() -> float:
        return float(FastIO.input())

    @staticmethod
    def getFloats() -> list[float]:
        return list(map(float, FastIO.input().split()))

    @staticmethod
    def getStr() -> str:
        return FastIO.input().decode().strip()

    @staticmethod
    def getStrs() -> list[str]:
        return FastIO.input().decode().split()

# Simple Implementation of Kruskal Algorithm
n, m = FastIO.getInts()
edges = [FastIO.getInts() for _ in range(m)]
# Sort by costs
edges.sort(key = lambda x: x[2]) 

# labels[i] = parent of vertex i
labels = list(range(n))
total = 0

for u, v, cost in edges:
    # Check if u and v are already connected
    if labels[u] == labels[v]: 
        continue
        
    # Include this edge
    for i in range(n):
        if i == v: continue
        # Update all vertexes with same parent as u
        if labels[i] == labels[v]: 
            labels[i] = labels[u]
    labels[v] = labels[u]
    total += cost
 
print(total)