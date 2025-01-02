while True:
  z1=int(input("Geben Sie erste Zahl ein: "))
  z2=int(input("Geben Sie zweite Zahl ein: "))
  if z1<z2 :
    for i in range(z1,z2+1) :
      print(i)
  elif z2<z1 :
    for i in range(z2,z1+1) :
      print(i)