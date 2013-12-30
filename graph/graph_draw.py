import turtle
from graph import Graph, Edge, Vert

drawnVerts = {}
vsize = 20
XMAX = 600
YMAX = 400
t = turtle.Turtle()

def tree(branchLen,t):
  if branchLen > 5:
    t.forward(branchLen)
    t.right(20)
    tree(branchLen-15,t)
    t.left(40)
    tree(branchLen-15,t)
    t.right(20)
    t.backward(branchLen)

def drawVert(vert, x, y):
  if drawnVerts.has_key(vert.label):
    return drawnVerts[vert.label]

  t.down()
  t.write(str(vert.label), font=("Arial", 18, "bold"))
  t.circle(vsize)
  t.up()
  drawnVerts[vert.label] = x,y
  drawAdjacents(vert, x, y)
  return x,y

def drawAdjacents(u, ux, uy):
  count = len(u.adjacents)
  vx = ux + vsize*3
  vy = YMAX/2
  for v in u.adjacents.values():
    vy += YMAX/count
    drawEdge(u, v, vx, vy)
    t.goto(ux, uy)

def drawEdge(u, v, x, y):
  t.down()
  t.goto(x, y)
  x,y = drawVert(v, x, y)
  t.up()

def main():
  gsize = 10
  myWin = turtle.Screen()
  myWin.screensize(XMAX, YMAX)
  #maxx,maxy = myWin.screensize()
  #print maxx, maxy
  t.up()
  #t.setx(0)#maxx/gsize)
  #t.sety(0)#maxy/2)
  #t.goto(maxx/gsize - maxx/2, 0)
  t.goto(-XMAX/2, 0)
  edges = [Edge(1, 2, 1), Edge(1, 3, 2), Edge(2, 4, 2), Edge(3, 4, 1), Edge(4, 5, 1)]
  edges = [Edge(1, 2, 1), Edge(1, 3, 2), Edge(1, 4, 3), Edge(1, 5, 4)]
  g = Graph(edges)
  drawVert(g.verts[1], -XMAX/2, YMAX)
  #t.down()
  #t.circle(vsize)#, -XMAX/2, YMAX)
  #t.color("green")
  #t.circle(vsize)#, -XMAX/2, YMAX)
  #t.goto(-XMAX/2, YMAX/2)
  #t.circle(vsize)#, -XMAX/2, YMAX)
  #drawEdge(g.verts[1], g.verts[2])
  #t.up()
  #t.backward(100)
  #tree(75,t)
  myWin.exitonclick()

main()
