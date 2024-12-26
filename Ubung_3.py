Konto=1000
while True :
  Menu=int(input("Geben Sie 1 fürGeld abheben,2 fürGeld anlegen ein"))
  Geld=None
  if Menu==2 :
    Geld=int(input("Wie viel legen Sie Geld an"))
    Konto=Geld+Konto
    print(str(Konto) + " Karte entnehmen")
    break
  elif Menu==1 :
    Geld=int(input("Wie viel heben Sie Geld ab"))
    if Geld>Konto :
      print("Leider ungültig")
      continue
    Konto=Konto-Geld
    print(str(Konto) + " Karte entnehmen")
    break
  else :
    print("Ungultige Auswahl")
print("Ende")
  
  
  