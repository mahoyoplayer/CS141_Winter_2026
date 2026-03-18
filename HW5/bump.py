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