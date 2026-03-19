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

from heapq import heapify, heappop, heappush
n = FastIO.getInt()
candies = [FastIO.getInt() for _ in range(n)]
total = 0

heapify(candies)
while len(candies) > 1:
    bag1, bag2 = heappop(candies), heappop(candies)
    combine = bag1 + bag2
    total += combine * 2
    heappush(candies, combine)

print(total)
    

