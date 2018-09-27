#Uses python3

import sys

def explore(adj,x,v,c):
  v[x]=1
  c[x]=1
  for y in adj[x]:
    if v[y]==0:
        if explore(adj,y,v,c) == 1:
            return 1
    elif c[y] == 1: return 1
  c[x]=0
  return 0

def acyclic(adj):
    visited = [0 for x in range(len(adj))]
    cyc = [0 for x in range(len(adj))]

    # iterate thru nodes
    for x in range(len(adj)):
        if visited[x] == 0:
            if explore(adj, x, visited, cyc) == 1:
                return 1
                # reset list of current path's vertices
        #reset list of current path's vertices
        cyc = [0 for x in range(len(adj))]
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
