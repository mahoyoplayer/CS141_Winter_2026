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

house_map = {
    "Gryffindor": 0,
    "Hufflepuff": 1,
    "Ravenclaw": 2,
    "Slytherin": 3
}

houses = [[] for _ in range(4)]
n = FastIO.getInt()
for _ in range(n):
    name, house = FastIO.getStrs()
    houses[house_map[house]].append(name)

# Sort names in each house
for i in range(4):
    houses[i].sort()

for house in house_map:
    print(house)
    print("\n".join(houses[house_map[house]]))

