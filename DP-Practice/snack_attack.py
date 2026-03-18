from sys import stdout
import io, os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

class FastIO:
    @staticmethod
    def getInt() -> int:
      return int(input())

    @staticmethod
    def getInts():
        return map(int, input().split())

    @staticmethod
    def getStr() -> str:
        return input().decode().strip()

    @staticmethod
    def getStrs() -> list[str]:
      return input().decode().split()

# DELETE START
from sys import stdin
stdin = open("../input.txt", "r")
input = stdin.readline
# DELETE END

n, p, b = FastIO.getInts()
start_y, start_x = FastIO.getInts()

# There can be multiple popcorns spawning on same tile
popcorns = {}
for _ in range(p):
    r, c, t = FastIO.getInts()
    popcorns[(r, c, t)] = popcorns.get((r, c, t), 0) + 1

boulders = set()
for _ in range(b):
    r, c, t = FastIO.getInts()
    boulders.add((r, c, t))
    
max_time = 100

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0), (0, 0))

def three_d_dp():
    valid = lambda x: 0 <= x < n
    dp = [[[-1] * n for _ in range(n)] for _ in range(max_time+1)]
    dp[0][start_y][start_x] = 0
   
    for t in range(1, max_time + 1):
        for r in range(n):
            for c in range(n):
                bestPrev = -1
                for deltaX, deltaY in dirs:
                    newX, newY = c + deltaX, r + deltaY
                    if valid(newX) and valid(newY):
                        bestPrev = max(bestPrev, dp[t-1][newY][newX])
                if bestPrev == -1: 
                    dp[t][r][c] = -1
                    continue
                    
                if (r, c, t) in popcorns:
                    bestPrev += popcorns[(r, c, t)]
                elif (r, c, t) in boulders:
                    bestPrev >>= 1
                    
                dp[t][r][c] = bestPrev
     
    best = 0
    for r in range(n):
        for c in range(n):
            best = max(best, dp[max_time][r][c])
    stdout.write(str(best))
    
three_d_dp()

