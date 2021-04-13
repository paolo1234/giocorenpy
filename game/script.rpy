#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define e = Character("Eileen", color="#f44")

image fem = im.Scale("fem.png", 392, 901)
# image fem = "fem.png"
image mas = im.Scale("mas.png", 400, 901)


# Il gioco comincia qui. 

label start:

    scene bg room

    show fem at center
    show mas:
        xalign 0.8
        yalign 1.0
    with fade

    # Questo mostra linee di dialogo.

    "Ciao raga"

    e "Hai creato un nuovo gioco Ren'py."

    e "Quando aggiungerai una storia, immagini e musica, potrai distribuirlo nel mondo!"

    return

