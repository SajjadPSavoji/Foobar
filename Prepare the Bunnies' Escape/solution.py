def solution(map):
    # solving with BFS
    # each node is represented wtih [i, j, w, d]
    # where i, j are map index and w determines
    # the number of walls we can break from that state
    # d is distance form source

    # some helper functions
    def in_bound(i, j, I, J):
      return (i>=0) and (i<I) and (j>=0) and (j<J)
    def is_empty(i, j, map):
      return not map[i][j]
    def is_wall(i, j, map):
      return map[i][j]
    def is_dest(i, j, I, J):
      return (i==I-1) and (j==J-1)
    def not_visited(i, j, w, visited):
      return (i,j,w) not in visited
    def can_break(w):
      return w > 0

    # moves are cardinal
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # get map dims
    I = len(map)
    J = len(map[0])

    # creat vis and que for BFS
    visited = {} # keeps tuple(i, j, w) using dict for o(1) access
    queue = [] # keeps list[i, j, w, d]

    # add source to queue
    queue.append([0, 0, 1, 1])
    visited[(0, 0, 1)] = True

    # while queue is not empty
    while queue:
      # Dequeue a vertex
      v = queue.pop(0)

      # check if reached destination
      if is_dest(v[0], v[1], I, J):
        return v[-1]

      # Get all adjacent vertices of the
      # dequeued vertex v.
      # we have only cardinal movemetns (i +-1 , j+-1)
      for im, jm in moves:
        i, j, w, d = v[0]+im, v[1]+jm, v[2], v[3]
        # check if [i,j] is in bound
        if in_bound(i, j, I, J):
          # if empty and not visited
          if is_empty(i, j, map) and not_visited(i, j, w, visited):
            queue.append([i, j, w, d+1])
            visited[(i, j, w)] = True
          # if wall and can break and not visited
          if is_wall(i, j, map) and can_break(w) and not_visited(i, j, w-1, visited):
            queue.append([i, j, w-1, d+1])
            visited[(i, j, w-1)] = True

    # dest could not be reached
    return -1