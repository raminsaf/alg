import turtle
from graph import Graph, Edge, Vert

drawnVerts = {}
VSIZE = 20
XMAX = 600
YMAX = 400
t = turtle.Turtle()

def drawVert(vert, x, y):
  print "Draw ", vert.label, x, y
  if drawnVerts.has_key(vert.label):
    print "ALREADY DRAWN %s" % str(vert.label)
    return drawnVerts[vert.label]

  t.color("black")
  t.down()
  t.write(str(vert.label), font=("Arial", 18, "bold"))
  t.circle(VSIZE)
  t.up()
  drawnVerts[vert.label] = x,y
  drawAdjacents(vert, x, y)
  return x,y

def drawAdjacents(u, ux, uy):
  count = len(u.adjacents)
  if count == 0:
    return
  toggle = 1
  vx = ux + VSIZE*6
  vy = YMAX - VSIZE#count
  for v in u.adjacents.values():
    toggle *= -1
    vy -= 2*YMAX/(count+1)
    vx += toggle*3*VSIZE
    x, y = drawEdge(u, v, vx, vy)
    t.down()
    t.color("green")
    t.goto(ux, uy)
    t.color("orange")
    t.up()

def drawEdge(u, v, x, y):
  #t.color("green")
  #t.down()
  t.up()
  t.goto(x, y)
  vx,vy = drawVert(v, x, y)
  t.up()
  t.color("blue")
  t.goto(vx, vy)
  return x,y

def main():
  t.up()
  gsize = 10
  myWin = turtle.Screen()
  myWin.screensize(XMAX+2*VSIZE, YMAX+2*VSIZE)
  t.goto(-XMAX/2, 0)
  edges = [Edge(1, 2, 1), Edge(1, 3, 2), Edge(2, 4, 2), Edge(3, 4, 1), Edge(4, 5, 1)]
  edges = [Edge(1, 2, 1), Edge(1, 3, 2), Edge(1, 4, 3), Edge(1, 5, 4), Edge(3, 6, 3), Edge(6, 1, -5), Edge(4, 2, -2)]
  g = Graph(edges)
  drawVert(g.verts[1], -XMAX/2, VSIZE)
  #t.color("green")
  myWin.exitonclick()

main()
