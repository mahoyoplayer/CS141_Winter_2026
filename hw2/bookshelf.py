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

n, k = FastIO.getInts()
books = [FastIO.getInt() for _ in range(n)]

# Use binary search to find best width

def test(max_width):
    used, curr_width = 0, float("inf")
    for book in books:
        if curr_width + book > max_width:
            used += 1
            if used > k: return False
            curr_width = book
        else:
            curr_width += book
    return True

import math
r = sum(books)
l = max(max(books), math.ceil(r/k))

while l < r:
    mid = (l+r) // 2
    if test(mid) == True:
        r = mid
    else:
        l = mid + 1

print(l)
# Expect 13948