#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Bienvenue à mon calcul de facture à payer")
valeur = float(input("Qu'elle est le total de facture $"))
#valeur_fl = float(valeur)
tip = int(input("De combien veux-tu donner? 10, 12, 15 ? "))
personne = int(input("Combien de personnes se partageront la facture ?"))
valeur_et_tip = tip / 100 * valeur + valeur
valeur_par_personne = round(valeur_et_tip / personne, 2)
valeur_par_personne = "{:.2f}".format(valeur_par_personne)
print(f"Chaque personne devra payer: ${valeur_par_personne} ")