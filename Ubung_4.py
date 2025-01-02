x1=int(input("X Koordinate: "))
y1=int(input("Y Koordinate: "))
x2=int(input("X Ziel: "))
y2=int(input("Y Ziel: "))
deltaX=((x2-x1)**2)**(1/2)
deltaY=((y2-y1)**2)**(1/2)
if deltaX==2 and deltaY==1 :
  print("Ja")
elif deltaX==1 and deltaY==2 :
  print("Ja")
else :
    print("Nein")

