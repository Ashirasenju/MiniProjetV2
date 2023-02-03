import csv
from random import randint

#début de sélection aléatoire de 30 questions
def lecture_fichier(nom_fichier):
    with open(nom_fichier, "r") as fichier:
        return [ligne for ligne in csv.reader(fichier)]


qcm = lecture_fichier("QCM.txt")
select = []
questions = []

while len(select) < 30:
    e= randint(0,29)
    if e not in select:
        select.append(e)


for x in select:
    questions.append(qcm[x])

#fin de sélection.
#Les questions choisies sont stockées dans la liste 'questions'

#Commence à poser les questions, demander les réponses et calculer le score
score=0
nb=0
for quest in questions:
    nb+=1
    a = quest[0]
    a=a.split(';;')
    print('Question',nb,' : ',a[0])
    rep = input("Entrez votre réponse : ")
    if rep == a[1]:
        print('Bonne réponse')
        score+=1
    else:
        print('Mauvaise réponse')

#fin du questionnaire
print("Vous avez",score,"bonne réponses sur 30")
