kaal = int(input("Kui palju sa kaalud (kg)? "))    # kaal kilogrammides
pikkus = int(input("Kui pikk sa oled (cm)? "))/100 # pikkus meetrites
kmi = kaal/(pikkus*pikkus)                         # kehamassiindeks
print("indeks: " + str(kmi))
if kmi > 30:
    print("Võiksid kaalust alla võtta")
else:
    print("Suurt ülekaalu ei paista")
if kmi < 17:
    print("Võiksid kaalus juurde võtta")
else:
    print("Ebanormaalselt kõhn ei ole")

# Ülesanne: täpsusta veel mõned vahemikud ning väljasta neile sobivad soovitused.
