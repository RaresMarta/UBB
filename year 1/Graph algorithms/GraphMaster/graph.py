import random
from iter import *
from collections import deque


class Graph:
    def __init__(self, is_dir: bool = True, weighted: bool = False):
        # O(1)
        self.graph = []
        self.directed = is_dir
        self.weighted = weighted

    def random_weights(self, weight_range: [int, int]):
        self.weighted = True

        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if self.graph[i][j] != 0:
                    self.graph[i][j] = random.randint(weight_range[0], weight_range[1])

                    if self.directed == False:
                        self.graph[j][i] = self.graph[i][j]

    def create_from_file(self, filename):
        f = open(filename, "r")
        option = f.readline()

        self.graph = []
        params = option.split(' ')

        n, m = int(params[0]), int(params[1])

        for i in range(n):
            self.graph.append([])
            for j in range(n):
                self.graph[i].append(0)

        if params[2] == 'T':
            self.directed = True
        else:
            self.directed = False

        if params[3] == 'T':
            self.weighted = True
        else:
            self.weighted = False

        for line in f:
            l = line.split(' ')

            x, y, w = int(l[0]), int(l[1]), 1
            if self.weighted == True:
                w = int(l[2])

            self.graph[x][y] = w

            if self.directed == False:
                self.graph[y][x] = w

        f.close()

    def set_weight(self, i, j, weight):
        try:
            assert self.weighted == True

            self.graph[i][j] = weight

            if self.directed == False:
                self.graph[j][i] = weight
        except:
            raise Exception("Invalid data")

    def get_vertices(self):
        # O(1)
        return len(self.graph)

    def get_neighbours(self, vertex):
        neighbours = []

        for i in range(len(self.graph)):
            if self.graph[vertex][i] != 0:
                neighbours.append(i)

        return neighbours

    def get_graph(self):
        # O(1)
        return self.graph

    def valid_vertex(self, vertex):
        if vertex < len(self.graph):
            return True

        return False

    def add_vertex(self):
        self.graph.append([])

        for index in range(len(self.graph)):
            self.graph[index].append(0)
            self.graph[len(self.graph) - 1].append(0)

        self.graph[len(self.graph) - 1].pop()

    def add_edge(self, edge):
        if edge[0] < len(self.graph) and edge[1] < len(self.graph):
            if (self.graph[edge[0]][edge[1]] == 1):
                raise Exception("Edge already exists")

            self.graph[edge[0]][edge[1]] = 1

            if self.directed == False:
                self.graph[edge[1]][edge[0]] = 1
        else:
            raise Exception("Edge is invalid")

    def remove_edge(self, edge):
        try:
            # assert self.graph[edge[0]][edge[1]] != 0
            self.graph[edge[0]][edge[1]] = 0

            if self.directed == False:
                self.graph[edge[1]][edge[0]] = 0
        except:
            raise Exception("Edge is invalid")

    def remove_vertex(self, vertex):
        try:
            self.graph[vertex]

            for i in range(vertex, len(self.graph) - 1):
                self.graph[i] = self.graph[i + 1]

            self.graph.pop()

            for i in range(0, len(self.graph)):
                for j in range(vertex, len(self.graph) - 1):
                    self.graph[i][j] = self.graph[i][j + 1]

                self.graph[i].pop()
        except:
            raise Exception("Vertex is invalid")

    def assign_edge(self, m, i, j, weights_range=[0, 1]):
        self.graph[i][j] = random.choice(weights_range)

        if self.directed == False:
            self.graph[j][i] = self.graph[i][j]

        if self.graph[i][j] != 0:
            m -= 1

        return m

    def create_random(self, n, m, weights_range=[0, 1]):
        self.graph = []

        try:
            if self.directed == True:
                assert m <= n * (n - 1)
            else:
                assert m <= n * (n - 1) // 2

            for i in range(n):
                self.graph.append([])
                for j in range(n):
                    self.graph[i].append(0)

            for i in range(n):
                for j in range(n):
                    if i != j and self.graph[i][j] == 0 and m > 0:
                        m = self.assign_edge(m, i, j, weights_range)

            while m > 0:
                x = random.randint(0, len(self.graph) - 1)
                y = random.randint(0, len(self.graph) - 1)

                if x != y and self.graph[x][y] == 0:
                    self.assign_edge(m, x, y, weights_range)

                    if self.graph[x][y] != 0:
                        m -= 1

        except Exception as e:
            raise e

    def get_n(self):
        return len(self.graph)

    def get_m(self):
        sum = 0

        for edge in self.graph:
            for el in edge:
                sum += el

        return sum

    def deg(self, x, option=0):
        # option == 0 => inbound + outbound
        # option == 1 => inbound
        # option == 2 => outbound
        sum = 0
        if self.directed == False:
            option = 1

        if x >= len(self.graph):
            raise Exception("Vertex is invalid")

        if option == 0 or option == 1:
            for edge in self.graph:
                sum += edge[x]

        if option == 0 or option == 2:
            for el in self.graph[x]:
                sum += el

        return sum

    def is_edge(self, edge):
        try:
            assert self.graph[edge[0]][edge[1]] == 1
            return True
        except:
            raise Exception("Edge invalid")

    def outbound_edges(self, vertex):
        try:
            outbound = []

            for out_vertex in range(len(self.graph[vertex])):
                if (self.graph[vertex][out_vertex] == 1):
                    outbound.append([vertex, out_vertex])

            return outbound
        except:
            raise Exception("Vertex is invalid")

    def inbound_edges(self, vertex):
        try:
            inbound = []

            for in_vertex in range(len(self.graph)):
                if (self.graph[in_vertex][vertex] != 0):
                    inbound.append([in_vertex, vertex])

            return inbound
        except:
            raise Exception("Vertex is invalid")

    def iter_vertex(self, start):
        v = Iterator(self, start)

        visited = set()
        queue = deque()

        queue.append(start)

        while len(queue) != 0:
            curr = queue[0]
            queue.popleft()

            if curr not in visited:
                v = Iterator(self, curr)
                visited.add(curr)

                while v.validV():
                    queue.append(v.get_curr())
                    v.next()

    def __str__(self):
        vertex = []
        edges = []

        for i in range(len(self.graph)):
            vertex.append(i)

        for in_vert in range(len(self.graph)):
            for out_vert in range(len(self.graph[in_vert])):
                if self.graph[in_vert][out_vert] != 0:
                    edges.append([in_vert, out_vert])

        return str(self.graph)
