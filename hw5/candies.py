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

from heapq import heappop, heappush

n, m = FastIO.getInts()
sell = [FastIO.getInt() for _ in range(n)]

# Set up adjacency array
adjacency = [[] for _ in range(n)]
for _ in range(m):
    x, y, cost = FastIO.getInts()
    adjacency[x].append((y, cost))
    adjacency[y].append((x, cost))

# Basic implemenation of Dijisktra
distance = [float("inf")] * n
distance[0] = 0
heap = [(0, 0)]
while heap:
    curr_dist, city = heappop(heap)
    
    # Better path was found earlier. Skip.
    if curr_dist > distance[city]: 
        continue
    
    # Explore adjacenct cities
    for neighbor, cost in adjacency[city]:
        new_dist = curr_dist + cost
        if new_dist < distance[neighbor]:
            distance[neighbor] = new_dist
            heappush(heap, (new_dist, neighbor))
                    
bestProfit = 0
for i in range(n):
    # Must subtract cost to reach and return from city
    profit = sell[i] - distance[i] * 2
    bestProfit = max(bestProfit, profit)
sys.stdout.write(str(bestProfit))

