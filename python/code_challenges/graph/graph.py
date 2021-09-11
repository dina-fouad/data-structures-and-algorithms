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



    def breadth_first_search(self, start_vertex, action=(lambda x: None)):
        queue = Queue()
        visited = set()

        queue.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(queue):
            current_vertex = queue.dequeue()
            action(current_vertex)
            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor_vertex = edge.vertex

                if neighbor_vertex in visited:
                    continue
                else:
                    visited.add(neighbor_vertex)
                queue.enqueue(neighbor_vertex)
