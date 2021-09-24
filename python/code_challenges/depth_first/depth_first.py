from collections import deque

class Vertex:

    def __init__(self,value):
        self.value = value



class Edge:

    def __init__(self,vertex,weight):
        self.vertex = vertex
        self.weight = weight


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Graph:
    def __init__(self):
        self._adjacency_list = {}


    def add_node(self, value):
        node = Vertex(value)
        self._adjacency_list[node] = []
        return node


    def size(self):
        return len(self._adjacency_list)

    def add_edge(self, start_node, end_node, weight=1):
        if start_node not in self.adjacency_list:
            raise KeyError('does not exist.')

        if end_node not in self.adjacency_list:
            raise KeyError('does not exist.')

        adjacencies = self.adjacency_list[start_node]
        adjacencies.append((end_node, weight))


    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list.get(vertex, [])

#############################################################


    def depthfirst(self,v,visited):
        visited = []
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.depthfirst(neighbour,visited)
    def DFS(self):
        visited=set()
        for vertex in self.graph:
            if vertex not in visited:
                self.depthfirst(vertex,visited)
 
