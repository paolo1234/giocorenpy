﻿#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define e = Character("Eileen", color="#f44")

image fem = im.Scale("fem.png", 392, 901)
image mas = "masfr.png"
# image mas = im.Scale("masfr.png", 400, 833)


# Il gioco comincia qui. 

label start:

    scene bg room

    show fem at center
    show mas:
        xalign 0.9
        yalign 1.0
    with fade

    # Questo mostra linee di dialogo.

    "Ciao raga"

    e "Hai creato un nuovo gioco Ren'py."

    e "Quando aggiungerai una storia, immagini e musica, potrai distribuirlo nel mondo!"

    return

