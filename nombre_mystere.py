import random

print("Choisis ton niveau :")
print("1 → Facile (1-50)")
print("2 → Normal (1-100)")
print("3 → Difficile (1-500)")

historique=[]
choix_niveau = int(input("Ton choix : "))

if choix_niveau == 1:
    limite = 50
    essais_max = 10
elif choix_niveau == 2:
    limite = 100
    essais_max = 7
else:
    limite = 500
    essais_max = 5

nombre_mystere = random.randint(1, limite)
compteur = 0

while True:
    essai = int(input(f"Saisis un nombre entre 1 et {limite} : "))
    historique.append(essai)  # ← la liste qui appelle append
    compteur += 1
    
    if compteur >= essais_max:
        print(f"Game Over ! Le nombre mystère était {nombre_mystere}")
        print(f"Tes essais : {historique}")  # ← avant le break
        break
    
    if essai > nombre_mystere:
        print("Trop grand !")
    elif essai < nombre_mystere:
        print("Trop petit !")
    else:
        print(f"Bravo ! Tu as trouvé en {compteur} essais !")
        print(f"Tes essais : {historique}")  # ← avant le break
        break