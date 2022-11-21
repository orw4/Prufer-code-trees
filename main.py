# Converts tree graphs to Prufer codes and Prufer codes to trees
# 21/11/2022

class Tree:
    def __init__(self,vertices,edges):
        self.vertices = vertices
        self.edges = edges

    # the vertices are a list of vertices (represented by 0-n numbers)
    # the edges are a list of lists, each list has 2 vertices

    # creates a list of vertex degrees
    def degrees(self):
        listOfDegrees = [0] * (len(self.vertices) + 1)
        for e in self.edges:
            listOfDegrees[self.findVertex(e[0])] += 1
            listOfDegrees[self.findVertex(e[1])] += 1
        return listOfDegrees

    # finds the index of a given vertex
    def findVertex(self,vertex):
        for v in range(len(self.vertices)):
            if self.vertices[v] == vertex:
                return v
        return -1

    # finds the leaf of smallest index in the tree
    def smallestLeaf(self):
        degree = self.degrees()
        for v in range(len(degree)):
            if degree[v] == 1:
                return self.vertices[v]
        return -1

    # erases a given vertex from both the vertex set and the edge set
    def removeVertex(self, vertex):
        try:
            self.vertices.remove(vertex)
        except:
            i=1
        for e in self.edges:
            if vertex in e:
                self.edges.remove(e)

    # finds the neighbor of smallest index of a given vertex
    def smallestNeighbor(self, vertex):
        for e in self.edges:
            if vertex in e:
                if e[0] == vertex:
                    return e[1]
                else:
                    return e[0]
        return -1

# converts trees to prufer codes
def treeToPrufer(tree):
    prufer = []
    while len(tree.vertices) > 2:
        leaf = tree.smallestLeaf()
        prufer.append(tree.smallestNeighbor(leaf))
        tree.removeVertex(leaf)
    return prufer

#converts prufer codes to trees
def pruferToTree(prufer):
    vertices = []
    verticesForPrufer = []
    edges = []
    for v in range(len(prufer) + 2):
        vertices.append(v)
        verticesForPrufer.append(v)
    while prufer != []:
        possibleVertices = set(verticesForPrufer) - set(prufer)
        v = list(possibleVertices)[0]
        edges.append([v,prufer[0]])
        verticesForPrufer.remove(v)
        prufer = prufer[1:]
    edges.append([verticesForPrufer[0],verticesForPrufer[1]])
    tree = Tree(vertices,edges)
