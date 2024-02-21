# Python implementation of Dinic's Algorithm
class Edge:
	def __init__(self, v, flow, C, rev):
		self.v = v
		self.flow = flow
		self.C = C
		self.rev = rev

# Residual Graph
class Graph:
	def __init__(self, V):
		self.adj = [[] for i in range(V)]
		self.V = V
		self.level = [0 for i in range(V)]

	# add edge to the graph
	def addEdge(self, u, v, C):

		# Forward edge : 0 flow and C capacity
		a = Edge(v, 0, C, len(self.adj[v]))

		# Back edge : 0 flow and 0 capacity
		b = Edge(u, 0, 0, len(self.adj[u]))
		self.adj[u].append(a)
		self.adj[v].append(b)

	# Finds if more flow can be sent from s to t
	# Also assigns levels to nodes
	def BFS(self, s, t):
		for i in range(self.V):
			self.level[i] = -1

		# Level of source vertex
		self.level[s] = 0

		# Create a queue, enqueue source vertex
		# and mark source vertex as visited here
		# level[] array works as visited array also
		q = []
		q.append(s)
		while q:
			u = q.pop(0)
			for i in range(len(self.adj[u])):
				e = self.adj[u][i]
				if self.level[e.v] < 0 and e.flow < e.C:

					# Level of current vertex is
					# level of parent + 1
					self.level[e.v] = self.level[u]+1
					q.append(e.v)

		# If we can not reach to the sink we
		# return False else True
		return False if self.level[t] < 0 else True

# A DFS based function to send flow after BFS has
# figured out that there is a possible flow and
# constructed levels. This functions called multiple
# times for a single call of BFS.
# flow : Current flow send by parent function call
# start[] : To keep track of next edge to be explored
#		 start[i] stores count of edges explored
#		 from i
# u : Current vertex
# t : Sink
	def sendFlow(self, u, flow, t, start):
		# Sink reached
		if u == t:
			return flow

		# Traverse all adjacent edges one -by -one
		while start[u] < len(self.adj[u]):

			# Pick next edge from adjacency list of u
			e = self.adj[u][start[u]]
			if self.level[e.v] == self.level[u]+1 and e.flow < e.C:

				# find minimum flow from u to t
				curr_flow = min(flow, e.C-e.flow)
				temp_flow = self.sendFlow(e.v, curr_flow, t, start)

				# flow is greater than zero
				if temp_flow and temp_flow > 0:

					# add flow to current edge
					e.flow += temp_flow

					# subtract flow from reverse edge
					# of current edge
					self.adj[e.v][e.rev].flow -= temp_flow
					return temp_flow
			start[u] += 1

	# Returns maximum flow in graph
	def DinicMaxflow(self, s, t):

		# Corner case
		if s == t:
			return -1

		# Initialize result
		total = 0

		# Augument the flow while there is path
		# from source to sink
		while self.BFS(s, t) == True:

			# store how many edges are visited
			# from V { 0 to V }
			start = [0 for i in range(self.V+1)]
			while True:
				flow = self.sendFlow(s, float('inf'), t, start)
				if not flow:
					break

				# Add path flow to overall flow
				total += flow

		# return maximum flow
		return total

def solution(entrances, exits, path):
    # figure out cap for entry nodes
    # based on their first immidiate neighbors
    entrances_cap = []
    for ent in entrances:
        cap = 0
        for flow in path[ent]:
            cap += flow
        entrances_cap.append(cap)

    # figure out cap for exit nodes
    # based on their immediate neighbors
    exits_cap = [0 for ext in exits]
    for node in range(len(path)):
        for e, ext in enumerate(exits):
            exits_cap[e] += path[node][ext]

    # solving with max-flow
    # add single source and destination node
    # reserved node 0 for source
    # reserve last node for sinc
    g = Graph(len(path) + 2)
    for u in range(len(path)):
        for v in range(len(path)):
            g.addEdge(u+1, v+1, path[u][v])

    # connect node 0 (source) to entry nodes
    for v in range(len(entrances_cap)):
        g.addEdge(0, entrances[v]+1, entrances_cap[v])

    # conect last node (sinc) to exists
    for u in range(len(exits_cap)):
        g.addEdge(exits[u]+1, len(path) + 1, exits_cap[u])

    return g.DinicMaxflow(0, len(path) + 1)