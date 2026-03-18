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


stdout.write("Hello World!")