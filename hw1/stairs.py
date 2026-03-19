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

n = FastIO.getInt()
steps = [FastIO.getInt() for _ in range(n)]

first_diff, second_diff = steps[1] - steps[0], steps[2] - steps[1]
if first_diff == second_diff:
    # Fourth or later step is wrong
    correct_diff = first_diff
    for i in range(3, n):
        if steps[i] - steps[i-1] != correct_diff:
            print(i + 1)
            sys.exit()
    raise RuntimeError("Should neve reach here.")
else:
    # First, second, or third step is wrong
    third_diff = steps[3] - steps[2]
    if third_diff == second_diff:
        print(1)
    else:
        correct_diff = (steps[3] - steps[0]) /3
        if steps[0] + correct_diff != steps[1]:
            print(2)
        else:
            print(3)
