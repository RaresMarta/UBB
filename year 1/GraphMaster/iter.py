class Iterator:
    def __init__(self, graph,vertex):
        self.graph = graph
        self.initial = vertex
        self.curr = vertex

        self.reachable = self.graph.get_neighbours(vertex)
        self.index = 0
        self.valid = True

    def first(self):
        self.curr = self.initial
        self.reachable = self.graph.get_neighbours(self.curr)

    def get_curr(self):
        return self.curr

    def validV(self):
        return self.valid

    def next(self):
        try:
            self.curr = self.reachable[self.index]
            self.index += 1
        except Exception:
            self.valid = False


