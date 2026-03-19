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
print(bestProfit)

