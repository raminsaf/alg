class Vert():
  def __init__(self, label):
    self.adjacents = {}
    self.weights = {}
    self.label = label

  def printVert(self):
    #for key in self.adjacents.keys():
    print " %s => %s" % (str(self.label), str(self.adjacents.keys()))

  def addAdjacent(self, vert, weight = 0):
    self.adjacents[vert.label] = vert
    self.weights[vert.label] = weight

class Edge():
  def __init__(self, vlabel, ulabel, weight = 0):
    self.vlabel = vlabel
    self.ulabel = ulabel
    self.weight = weight

class Graph():
  def __init__(self, edges):
    self.verts = {}
    for edge in edges:
      #pull inside a function
      #maybe use sets here instead of dict
      v = self.getVert(edge.vlabel)
      u = self.getVert(edge.ulabel)
      v.addAdjacent(u, edge.weight)
  
  def getVert(self, label):
    if self.verts.has_key(label):
      v = self.verts[label]
    else:
      v = Vert(label)
      self.verts[label] = v
    return v

if __name__ == "__main__":
  edges = [Edge(1, 2, 1), Edge(1, 3, 2), Edge(2, 4, 2), Edge(3, 4, 1), Edge(4, 5, 1)]
  g = Graph(edges)
  for vert in g.verts.values():
    vert.printVert()
