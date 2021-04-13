#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.

define f = Character("Femmina", color="#f44000")
define m = Character("Maschio", color="#1363CC")

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
    "\"Citta brutta, 2021..\""

    f "Ugh.. Non capisco cosa non vada con la mia console"
    m "Ma che noiosa che seii! Ma staccati ogni tanto da questi computer e vieni fuori a giocare"
    

    return

