from easygui import *

victime = []

msg = "Informations concernnant l'appel"
title = "Secours"
fields = ("Nom", "Nombre de victimes")
mes_choix = multenterbox(msg, title, fields)
print("data : ", mes_choix)

nombre_victimes = mes_choix[1]

print("Nombre de victimes : " + str(nombre_victimes))

for i in range(int(nombre_victimes)):
    msg = "Informations concernnant la victime " + str(i + 1)
    title = "Secours"
    fields = ("Nom", "Lieu de la victime", "Etat de la ou les victime", "Obstacles potentiels")
    victime.append(multenterbox(msg, title, fields))

msg = "Récapitulaif des victimes :"
text = ""
for i in range(int(nombre_victimes)):
    text = text + "Victime " + str(i) + "\n"
    for j in range(len(victime[i])):
        text = text + victime[i][j] + "\n"
    text = text + "\n"
textbox(msg, title, text)

print(victime)