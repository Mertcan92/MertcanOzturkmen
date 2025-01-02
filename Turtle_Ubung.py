import turtle
ninja=turtle.Turtle()
ninja.shape("turtle")
ninja.color("red")
seite=int=input("Seitenlaenge: ")
for i in range(4) :
  ninja.forward(seite)
  ninja.right(90)
for i in range(3) :
  ninja.forward(seite)
  ninja.left(120)
  