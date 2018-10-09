#Uses python3

import sys

def explore(adj,x,v):
  v[x-1]=1
  for y in adj[x]:
    if v[y-1]==0: explore(adj,y,v)
  return

def reach(adj, x, y):
    #write your code here
#    print(adj)
    visited = [0 for x in range(len(adj))]
    explore(adj,x,visited)
#    print(visited)
    return visited[y-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
