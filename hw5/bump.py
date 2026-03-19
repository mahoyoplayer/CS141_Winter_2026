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

n, m = FastIO.getInts()
 
adjacency = [[] for _ in range(n)]
 
for _ in range(m):
    loc1, loc2, b, d = FastIO.getInts()
    adjacency[loc1].append((loc2, b, d))
    adjacency[loc2].append((loc1, b, d))
    
bumps = [float("inf")] * n
distance = [float("inf")] * n
 
distance[0] = 0
bumps[0] = 0
 
from heapq import heappush, heappop
pq = [(0, 0, 0)]
while pq:
    b, d, loc = heappop(pq)
    
    # No longer worth considering
    if b != bumps[loc] or d != distance[loc]:
        continue
    
    for neighbor, road_bumps, road_dist in adjacency[loc]:
        newBump, newDist = b + road_bumps, d + road_dist
        if newBump < bumps[neighbor] or (newBump == bumps[neighbor] and newDist < distance[neighbor]):
            bumps[neighbor] = newBump
            distance[neighbor] = newDist
            heappush(pq, (newBump, newDist, neighbor))
 
print(bumps[-1], distance[-1])