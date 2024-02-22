
def isCyclic(x, y):
    cnt = 0
    while True:
        if x == y:
            return False
        if (x + y) % 2 == 1:
            return True
        if x > y:
            (x,y) = ((x - y)//2, y)
        else:
            (x,y) = (x, (y - x)//2)

def countMatch(G):
    n = len(G)
    M = [-1 for x in range(n)]
    for i in range(n):
        p = None if M[i] != -1 else findPath(G, M, i)        
        if p != None: #Path exists
            lp = len(p)//2
            for j in range(lp):#set Matching
                s = p[2 * j]
                v = p[2 * j + 1]
                M[s] = v
                M[v] = s
    return n - M.count(-1)

def findPath(G, M, src):
    #Graph G
    #Matching M
    
    n = len(G)
    #bfs from i
    q = [src]
    reachBy = [[]] * n
    reachBy[src] = [src]
    while q != []:
        nq = []
        for i in range(len(q)):
            x  = q[i]#current vertex
            p  = reachBy[x]
            for j in range(n):
                if G[x][j]:#e -> j
                    if M[j] == -1:
                        if j != src:
                            return p + [j]
                    else:
                        if reachBy[j] == []:
                            nq.append(M[j])
                            reachBy[j] = p + [j]
                            reachBy[M[j]] = p + [j, M[j]]
                        else:
                            cp = reachBy[j]
                            if len(cp) % 2 == 1:#cycle detected
                                for k in range(len(cp) - 1, - 1, -2):
                                    if cp[k] in p:#cycle closed
                                        break
                                    y, yn = cp[k], cp[k - 1] # new goThrough
                                    ##  x -> j -> M[j] -> y -> yn -> yp
                                    for yp in range(n):
                                        if G[yn][yp]:
                                            if M[yp] == -1:
                                                if yp != src:
                                                    return p + [j, M[j], y, yn, yp]
                                            elif reachBy[yp] == []:
                                                reachBy[j] = p + [j]
                                                reachBy[M[j]] = p + [j, M[j]]
                                                nq.append(M[yp])
                                                reachBy[yp]    = p + [j, M[j], y, yn, yp]
                                                reachBy[M[yp]] = p + [j, M[j], y, yn, yp, M[yp]]                                                
        q = nq
    return None
                
def solution(banana_list):
    n = len(banana_list)
    cyclic = [[False for x in range(n)] for y in range(n)]
    for y in range(n):
        for x in range(y + 1, n):
            isCycle = isCyclic(banana_list[x], banana_list[y])
            cyclic[y][x] = isCycle
            cyclic[x][y] = isCycle
    return n - countMatch(cyclic)