import turtle
from random import *

# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue à la course des tortues !")
ts.setup(width=1400, height=800, startx=0, starty=0)

# DÃ©clarez les 5 tortues et positionnez-les sur leurs hexagones respectifs
michelangelo = turtle.Turtle()
michelangelo.speed(10)
michelangelo.color("Orange")
michelangelo.shape("turtle")
michelangelo.up()
michelangelo.goto(-650, 300)

leonardo = turtle.Turtle()
leonardo.speed(10)
leonardo.color("Deep Sky Blue")
leonardo.shape("turtle")
leonardo.up()
leonardo.goto(-650, 150)

raphael = turtle.Turtle()
raphael.speed(10)
raphael.color("Red")
raphael.shape("turtle")
raphael.up()
raphael.goto(-650, 0)

splinter = turtle.Turtle()
splinter.speed(10)
splinter.color("Dark Slate Gray")
splinter.shape("turtle")
splinter.up()
splinter.goto(-650, -150)

donatello = turtle.Turtle()
donatello.speed(10)
donatello.color("purple")
donatello.shape("turtle")
donatello.up()
donatello.goto(-650, -300)

# Demander de saisir dans la console les prÃ©dictions des joeurus 1 et 2 dans le format 1,2,3

predictionJ1 = input('Votre predicition (1,2,3 sans espace !) ? (J1)')

tabJ1 = predictionJ1.split(',')

predictionJ2 = input('Votre predicition (1,2,3 sans espace !) ? (J2)')

tabJ2 = predictionJ2.split(',')

# A l'aide d'une boucle while, faire courir les tortues en tirant un nombre entre 0 et 5 qui reprÃ©sente le nombre de pixels du dÃ©placement vers la droite

arrives = []

continuer = True

t1 = True
t2 = True
t3 = True
t4 = True
t5 = True

while continuer:
    if t1 == False and t2 == False and t3 == False and t4 == False and t5 == False:
        continuer = False
    if michelangelo.position()[0] >= 670:
        if t1 != False:
            arrives.append('1')
            print('arrive 1')
            t1 = False
    else:
        michelangelo.forward(randint(0, 5))

    if leonardo.position()[0] >= 670:
        if t2 != False:
            arrives.append('2')
            print('arrive 2')
            t2 = False
    else:
        leonardo.forward(randint(0, 5))

    if raphael.position()[0] >= 670:
        if t3 != False:
            arrives.append('3')
            print('arrive 3')
            t3 = False
    else:
        raphael.forward(randint(0, 5))

    if splinter.position()[0] >= 670:
        if t4 != False:
            arrives.append('4')
            print('arrive 4')
            t4 = False
    else:
        splinter.forward(randint(0, 5))

    if donatello.position()[0] >= 670:
        if t5 != False:
            arrives.append('5')
            print('arrive 5')
            t5 = False
    else:
        donatello.forward(randint(0, 5))

# Comparer les rÃ©sultats de la course avec les pronostics des joueurs
# et afficher le rÃ©sultat de la course
# et le joueur gagnant avec la tortue arbitre et l'instruction turtle.Write Ã  la position 0,0
# A IMPLEMENTER

gagnant = ''

turtle_arbitre = turtle.Turtle()
turtle_arbitre.goto(0, 0)
turtle_arbitre.color("Black")

print(arrives)
print(arrives[:3])

if tabJ1 == arrives[:3]:
    turtle_arbitre.write("Le joueur 1 a gagné", move=True, align="left", font=("Arial", 16, "normal"))
elif tabJ2 == arrives[:3]:
    turtle_arbitre.write("Le joueur 2 a gagné", move=True, align="left", font=("Arial", 16, "normal"))
else:
    turtle_arbitre.write("Aucun joueur n'a gagné (Try again)", move=True, align="left", font=("Arial", 16, "normal"))

turtle_arbitre.up()
turtle_arbitre.goto(0, -40)
turtle_arbitre.down()
turtle_arbitre.write(arrives[:3], move=True, align="left", font=("Arial", 16, "normal"))

turtle.mainloop()
