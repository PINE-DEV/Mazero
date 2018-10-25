import random
import numpy

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class MazeGraph:
    def __init__(self, width, height):
        # Using an Adjacency matrix implementation to store the graph:
        # https://en.wikipedia.org/wiki/Adjacency_matrix
        self.width = width
        self.height = height
        self.adjList = numpy.zeros([self.width*self.height, self.width*self.height], dtype=bool)
        self.edgesList = []
        self.generateMaze()

    def getEdges(self):
        return self.edgesList

    def generateMaze(self):
        # Simplest algorithm. Just for testing the rest of the interface first
        for x1 in range(self.width - 1):
            self.addEdge(Cell(x1, 0), Cell(x1 + 1, 0))
            self.addEdge(Cell(x1, self.height - 1), Cell(x1 + 1, self.height - 1))

        for y1 in range(self.height - 1):
            self.addEdge(Cell(0, y1), Cell(0, y1 + 1))
            self.addEdge(Cell(self.width - 1, y1), Cell(self.width - 1, y1 + 1))

        for y1 in range(1, self.height - 1):
            for x1 in range(1, self.width - 1):
                x2, y2 = x1, y1
                cellA = Cell(x1, y1)
                if bool(random.getrandbits(1)):
                    y2 += 1
                else:
                    x2 += 1
                cellB = Cell(x2, y2)
                self.addEdge(cellA, cellB)

    def addEdge(self, cellA, cellB):
        self.edgesList.append([cellA, cellB])
        vertexNumberA = (cellA.x % self.width) + (cellA.y * self.width)
        vertexNumberB = (cellB.x % self.width) + (cellB.y * self.width)
        self.adjList[vertexNumberA][vertexNumberB] = True
        self.adjList[vertexNumberB][vertexNumberA] = True

    def adjacent(self, cellA, cellB):
        pass
    def neighbors(self, cell):
        pass
    def add_vertex(self, cell):
        pass
    def remove_vertex(self, cell):
        pass
    def add_edge(self, cellA, cellB):
        pass
    def remove_edge(self, cellA, cellB):
        pass
    def get_vertex_value(self, cell):
        pass
    def set_vertex_value(self, cell):
        pass
