from sys import stdout
import io, os

input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

class FastIO:
  @staticmethod
  def getInt() -> int:
      return int(input())

  @staticmethod
  def getInts() -> list[int]:
      return(list(map(int,input().split())))

  @staticmethod
  def getStr() -> str:
      return input().strip()

  @staticmethod
  def getStrs() -> list[str]:
      return input().strip().split()

# DELETE START
from sys import stdin
stdin = open("../input.txt", "r")
input = stdin.readline
# DELETE END

n, heights = FastIO.getInt(), FastIO.getInts()

if n == 1:
    stdout.write("0")
    raise SystemExit

# dp[i] = cost to get to i-th rock
dp = [0] * n
dp[1] = abs(heights[1] - heights[0])

for i in range(2, n):
    oneDiff = abs(heights[i] - heights[i-1])
    twoDiff = abs(heights[i] - heights[i-2])
    dp[i] = min(dp[i-1] + oneDiff, dp[i-2] + twoDiff)

stdout.write(str(dp[-1]))