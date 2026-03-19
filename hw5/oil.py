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

n, m = FastIO.getInts()
 
if n == 0:
    sys.stdout.write("0")
    sys.exit()
 
edges = [0] * m
for i in range(m):
    edges[i] = FastIO.getInts()
# Sort edges by cost
edges.sort(key = lambda x: x[2])
 
labels = list(range(n))

# Number of edges to get to parent
rank = [0] * n

def findParent(v):
    if labels[v] == v:
        return v
    labels[v] = findParent(labels[v])
    return labels[v]
   
def union(u_p, v_p):
    # Always move lesser into greater
    if rank[u_p] < rank[v_p]:
        labels[u_p] = v_p
    elif rank[v_p] < rank[u_p]:
        labels[v_p] = u_p
    else:
        labels[u_p] = v_p
        rank[v_p] += 1
        

used = 0
for u, v, cost in edges:
    u_p, v_p = findParent(u), findParent(v)
    if u_p == v_p: continue
    union(u_p, v_p)
    used += 1
    if used == n - 1:
        print(cost)
        sys.exit()
 
raise RuntimeError("Should never reach this point")