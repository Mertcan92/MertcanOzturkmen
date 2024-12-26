Note=int(input("Geben Sie Ihre Note ein"))
Erfahrung=int(input("Geben Sie Ihre Erfahrung zwischen 1 und 5 ein"))
if  Note>90 or Note>=70 and Erfahrung==5 :
  print("direkt einstellen")
elif Note>70 or Erfahrung==4 and Note<70 :
  print("Zum Gespräch einladen")
else :
  print("ablehnen")