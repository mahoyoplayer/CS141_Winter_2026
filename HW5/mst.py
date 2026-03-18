import sys
import os

class FastIO:
    @staticmethod
    def getInt() -> int:
      return int(input())

    @staticmethod
    def getInts():
        return (list(map(int,input().split())))

    @staticmethod
    def getStr() -> str:
        return input().decode().strip()

    @staticmethod
    def getStrs() -> list[str]:
      return input().decode().split()

#region
base = os.path.splitext(__file__)[0]
input_file = base + ".txt"
if os.path.exists(input_file):
    sys.stdin = open(input_file, "r")
input = sys.stdin.buffer.readline
#endregion

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