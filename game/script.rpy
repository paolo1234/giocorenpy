﻿#  Lo script di gioco va in questo file.

#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define e = Character("Eileen", color="#f44")

image fem = im.Scale("fem.png", 320, 680)
# Il gioco comincia qui.

label start:

    # Mostra uno sfondo. Al momento mostra una sagoma generica, ma puoi
    # aggiungere un file (chiamato "bg room.png" oppure "bg room.jpg")
    # alla directory 'images' per cambiarla.


    scene bg room

    # Mostra lo sprite di un personaggio.
    # Al momento mostra una sagoma generica, ma puoi aggiungere un file
    # (chiamato "eileen_happy.png") alla directory 'images' per cambiarla.

    show fem at true center

    # Questo mostra linee di dialogo.

    "Ciao raga"

    e "Hai creato un nuovo gioco Ren'py."

    e "Quando aggiungerai una storia, immagini e musica, potrai distribuirlo nel mondo!"

    # Questo finisce il gioco.

    return

