class Solution:
    def __init__(self):
        self.startNodes = []  # An array to store the starting nodes (nodes with no incoming edges).
        self.graph = []  # An adjacency list representation of the course prerequisites graph.
        self.time = []  # An array to store the time required to complete each course.
        self.visited = []  # An array to track visited nodes during DFS.
        self.ans = []  # An array to store the maximum time needed for each course.

    def minimumTime(self, n, relations, time):
        self.toGraph(relations, n)  # Convert the input relations into a graph.
        self.time = time
        self.ans = [0] * n  # Initialize the ans array to store maximum times.
        self.visited = [False] * n  # Initialize the visited array for DFS.
        longest = 0

        # For each starting node (no incoming edges), find the maximum time needed.
        for node in self.startNodes:
            longest = max(longest, self.calculate(node))
        return longest

    # Convert the input relations into an adjacency list graph.
    def toGraph(self, edges, n):
        incoming = [0] * n
        outgoing = [0] * n

        # Count incoming and outgoing edges for each node.
        for e in edges:
            outgoing[e[0] - 1] += 1
            incoming[e[1] - 1] += 1

        startCnt = 0

        # Count the number of starting nodes (nodes with no incoming edges).
        for i in incoming:
            if i == 0:
                startCnt += 1

        self.startNodes = [0] * startCnt

        # Populate the starting nodes array.
        sni = 0
        for i in range(n):
            if incoming[i] == 0:
                self.startNodes[sni] = i
                sni += 1

        # Create the adjacency list graph.
        self.graph = [[] for _ in range(n)]

        # Populate the graph with edges.
        for e in edges:
            self.graph[e[0] - 1].append(e[1] - 1)

    # Recursively calculate the maximum time needed for a course using DFS.
    def calculate(self, node):
        if self.ans[node] > 0:
            return self.ans[node]

        worstPrereq = 0
        self.visited[node] = True

        # Visit each child (prerequisite) and find the maximum time.
        for child in self.graph[node]:
            if not self.visited[child]:
                worstPrereq = max(self.calculate(child), worstPrereq)

        self.visited[node] = False

        # Store the maximum time needed for the current course.
        self.ans[node] = worstPrereq + self.time[node]
        return self.ans[node]